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
- Proud Father!


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


What is circuits?
=================

.. rst-class:: build

- a Python (*lightweight*) Framework
- a Component Architecture
- is Event Driven
- has Asynchronous I/O
- has a Web Framework (``circuits.web``)
- plays nicely with others (*tornado, Twisted, etc*)


Why the name "circuits"?
========================

.. rst-class:: build

* Building Software with circuits is analageous to *Electronic Circuits*
* Components are registered together (*Breadboard*)
* Components cooperate and communicate via Event(s) (*Signals*)
* **Components are composable units of behavior.**


What does circuits look like? (#1)
==================================

.. code-block:: python
    
    from circuits import handler, Component, Debugger

    from circuits.net.events import write
    from circuits.net.sockets import TCPServer


    class EchoServer(Component):

        def init(self, bind):
            TCPServer(bind).register(self)

        @handler("read")
        def on_read(self, sock, data):
            self.fire(write(sock, data))


    app = EchoServer(("0.0.0.0", 10000))
    Debugger().register(app)
    app.run()


What does circuits look like? (#2)
==================================

.. graphviz:: examples/EchoServer.dot


What does circuits look like? (#3)
==================================

.. figure:: /examples/EchoServer.png


Demo!
=====

.. rst-class:: build

* Hello World!
* Echo Server
* Dynamic Runtime


Core API (#1)
=============

**Event Handling**:

.. rst-class:: build

* ``.fire()``
* ``.wait()``
* ``.call()``

**Component Registration:**

.. rst-class:: build

* ``.register()``
* ``.unregister()``


Core API (#2)
=============

**Startup and Shutdown:**

.. rst-class:: build

* ``.start()`` *Thread/Process Mode*
* ``.stop()``
* ``.run()``


Where we are now (#1)
=====================

.. rst-class:: build

* Core API

  - ``.fire()``, ``.wait()``, ``.call()``
  - ``.register()``, ``.unregister()``
  - ``.start()``, ``.stop()``, ``.run()``

* Core Components

  - Component
  - Debugger
  - Bridge
  - Worker
  - Timer


Where we are now (#2)
=====================

.. rst-class:: build

* Application

  - Daemon

* I/O

  - File
  - Serial
  - INotify


Where we are now (#3)
=====================

.. rst-class:: build

* Networking

  - TCPClient
  - UDPClient
  - UNIXClient
  
  - TCPServer
  - UDPServer
  - UNIXServer


Where we are now (#4)
=====================

.. rst-class:: build

* Protocols

  - WebSockets
  - Line
  - HTTP
  - IRC

* Pollers

  - Select
  - Poll
  - EPoll
  - KQueue


Where we are now (#5)
=====================

.. rst-class:: build

* Web

  - Server
  - Static
  - Logger
  - XMLRPC
  - JSONRPC
  - WebSockets
  - VirtualHosts
  - WSGI Gateway
  - WSGI Application


Where we want to be
===================

.. rst-class:: build

* More Protocols
* Better performance
* Improved documentation
* More Application components
* Improved ``circuits.node`` (*Experimental*)

* **A snazier website!!!**


How you can help
================

.. rst-class:: build

* Join our ``#circuits`` channel on FreeNode IRC!
* Start using circuits in your project(s)!
* Contribute Bug fixes and Improvements.
* Help us port/write new protocols.


Questions?
==========

.. image:: /_static/images/questions.png
   :align: center


Links
=====

* circuits Website: http://circuitsframework.com/
* circuits.web Website: http://circuitsweb.com/
* PyPi Page: https://pypi.python.org/pypi/circuits
* Bitbucket Team: https://bitbucket.org/circuits
* Bitbucket Repository: https://bitbucket.org/circuits/circuits
* Issue Tracker: https://bitbucket.org/circuits/circuits/issues
* Mailing List: https://groups.google.com/forum/#!forum/circuits-users
