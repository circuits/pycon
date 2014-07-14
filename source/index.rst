=============================
 Building Blocks of Software
=============================

.. figure:: /_static/images/circuits.png

PyConAU -- 6/Aug/2014


Who am I?
=========

.. rst-class:: build

- James Mills / prologic
- Author of circuits
- Pythonista and Web Developer
- Open Source Enthusiast


What have I done?
=================

**Recently:**

.. rst-class:: build

- MyMinesOnlines (*QLD Govt*)
- TerraNova (*Griffith*)
- CCAV (*Griffith*)


**Other Things:**

.. rst-class:: build

- Various Wiki(s) and CMS(s)
- Various IRC Bot(s)
- Other Smaller Projects


What is circuits? (#1)
======================


.. rst-class:: build

- a Python (*lightweight*) Framework
- a Component Architecture
- is Event Driven
- has Asynchronous I/O


What is circuits? (#2)
======================


**circuits also:**

.. rst-class:: build

- has a Web Framework (``circuits.web``)
- plays nicely with others (*tornado, Twisted, etc*)


What does circuits look like?
=============================

.. code-block:: python
    
    from circuits import handler, Component, Debugger
    
    from circuits.net.events import write
    from circuits.net.sockets import TCPServer
    
    class EchoServer(TCPServer):
        
        def init(self, bind):
            TCPServer(bind).register(self)
            
        @handler("read")
        def on_read(self, sock, data):
            return data
    
    # Start and "run" the system.
    # Bind to port 0.0.0.0:9000
    app = EchoServer(9000)
    Debugger().register(app)
    app.run()
