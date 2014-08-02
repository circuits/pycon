=======================
Component Architectures
=======================

.. figure:: /_static/images/circuits.png

PyConAU -- 2nd August 2014


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

- TerraNova and CCAV (*Griffith*)
- MyMinesOnlines (*QLD Govt*)

**Other Things:**

- Various Wiki(s) and CMS(s)
- Various IRC Bot(s)
- Other Smaller Projects


What is circuits?
=================

.. rst-class:: build

- a Python (*lightweight*) Framework

  - with no external dependencies

- a Component Architecture
- is Event Driven
- supports Asynchronous I/O and Coroutines
- has a Web Framework (``circuits.web``)
- plays nicely with others (*tornado, Twisted, etc*)


Component Architectures (#1)
============================

* an object that provides a certain type of service
* typically singletons
* can declare "extension points" that other components can “plug in” to

*Borrowed from Trac:*

  This allows one component to enhance the functionality of the component
  it extends, without the extended component even knowing that the extending
  component exists.


Component Architectures (#2)
============================

.. figure:: /_static/images/xtnpt.png

Similar Frameworks/Projects:

* `Trac <http://trac.edgewall.org/>`_
* `Zope <http://www.zope.org/>`_
* `Kamaelia <http://www.kamaelia.org/>`_
* `pypes <https://pypi.python.org/pypi/pypes>`_
* *But seriously just use circuits!*


Why the name "circuits"?
========================

.. rst-class:: build

* Building Software with circuits is analogous to *Electronic Circuits*
* Components are registered together (*Breadboard*)
* Components cooperate and communicate via Event(s) (*Signals*)
* **Components are composable units of behavior.**


circuits' History
=================


.. rst-class:: build

* Inspired by the late Prof. Geoff Dromery
  and Genetic Software Engineering
* First prototypes were written in Java
* In development since ~2004 (*10+ years*)
* Has seen 30+ contributors and counting.


circuits' Contributors
======================

.. rst-class:: build

* James Mills (**Me!**)
* Alessio Deiana
* Dariusz Suchojad
* Michael Lipp
* Justin Giorgi
* Tim Miller
* Edwin Marshall
* Alex Mayfield
* Toni Alatalo
* Holger Krekel


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

Old graphviz output:

.. graphviz:: examples/EchoServer.dot


What does circuits look like? (#3)
==================================

New networkx + matplotlib output:

.. figure:: /examples/EchoServer.png


Demos!
======

.. code-block:: python

    from circuits import Component, Event


    class hello(Event):
        """hello Event"""


    class App(Component):

        def hello(self):
            print("Hello World!")

        def started(self, component):
            self.fire(hello())
            raise SystemExit(0)


    App().run()


Core API (#1)
=============

**Event Handling**:

.. rst-class:: build

* ``.fire(event, *channels, **kwargs)``
* ``.wait(event, *channels, **kwargs)``
* ``.call(event, *channels, **kwargs)``

**Component Registration:**

.. rst-class:: build

* ``.register(parent)``
* ``.unregister()``


Core API (#2)
=============

**Startup and Shutdown:**

.. rst-class:: build

* ``.start(process=False, link=None)``
* ``.stop()``
* ``.run(socket=None)``


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
  - Notify


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
* More Application Components
* Improved ``circuits.node`` (*Experimental*)

* **A snazzier website!!!**


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
* circuits Documentation: http://circuits.readthedocs.org/
* PyPi Page: https://pypi.python.org/pypi/circuits
* Bitbucket Team: https://bitbucket.org/circuits
* Bitbucket Repository: https://bitbucket.org/circuits/circuits
* Issue Tracker: https://bitbucket.org/circuits/circuits/issues
* Mailing List: https://groups.google.com/forum/#!forum/circuits-users
