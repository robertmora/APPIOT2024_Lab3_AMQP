import optparse
from proton.handlers import MessagingHandler
from proton.reactor import Container


class Recv(MessagingHandler):
    def __init__(self, url, count):
        super(Recv, self).__init__()
        self.url = url
        self.expected = count
        self.received = 0

    def on_start(self, event):
        event.container.create_receiver(self.url)

    def on_message(self, event):
        if event.message.id and event.message.id < self.received:
            # ignore duplicate message
            return
        if self.expected == 0 or self.received < self.expected:
            print(f"Received message: {event.message.body}")
            #print(event.message.body)
            self.received += 1
            #if self.received == self.expected:
            #    event.receiver.close()
                #event.connection.close()


parser = optparse.OptionParser(usage="usage: %prog [options]")
parser.add_option("-a", "--address", default="localhost:5672/examples",
                  help="address from which messages are received (default %default)")
parser.add_option("-m", "--messages", type="int", default=100,
                  help="number of messages to receive; 0 receives indefinitely (default %default)")
opts, args = parser.parse_args()

try:
    Container(Recv(opts.address, opts.messages)).run()
except KeyboardInterrupt:
    pass
