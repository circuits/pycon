#!/usr/bin/env python


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
