from channel import Channel
from controller import Controller
from hello_pb2 import HelloService_Stub
from hello_pb2 import HelloRequest

def main():
    channel = Channel()
    sock = channel.connect("127.0.0.1", 8888)
    stub = HelloService_Stub(channel)
    controller = Controller()
    controller.sock = sock
    request = HelloRequest()
    response = stub.Hello(controller, request, None).get()
    print "response:", response
    print "meta:", controller.meta_data

if __name__ == "__main__":
    main()