# simple behaviour testing
import pytest

from yappyChuck import Client, Server

port = 5005
client = Client("127.0.0.1", port)
server = Server(port)

def test_start_server():
    '''
    test handling server start
    '''
    server.start('server.ck')

def test_client_left():
    '''
    testing against
    '''
    numbers = [[12,34]]

    client.send('tsne', "tsne:" + str(numbers[0][0]) + "," + str(numbers[0][1]))

def test_client_right():
    '''
    testing against
    '''
    numbers = [[-12,-34]]

    client.send('tsne', str(numbers[0][0])  + "," + str(numbers[0][1]))

def test_client_many():
    '''
    testing against
    '''
    numbers = [[-12,-34], [78,94]]

    for number in numbers:
        client.send('tsne', str(number[0])  + "," + str(number[1]))

def test_stop_server():
    '''
    test handling server start
    '''
    server.stop()
