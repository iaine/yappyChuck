'''
yappyChuck - yet another python pyChuck
File to stop and start service
'''

import os
import subprocess

from pythonosc import udp_client

class Server():

    def __init__(self, port_number) -> None:
        self.port = port_number
        self.process = None

    def start(self, command_string):
        try:
            cwd = os.getcwd()

            self.process = subprocess.Popen(["`which chuck` {}".format(cwd + "/sound/" + command_string)], shell=True, \
                                        stderr=subprocess.PIPE, stdout= subprocess.PIPE)
            if not self.process.pid:
                raise Exception('No server')
            print(self.process.pid)
        except Exception as e:
            print("Server Error {}".format(e))

    def stop(self):
        pid =  self.process.pid

        self.process.terminate()

        #let's catch any zombies
        try:
            os.kill(pid, 0)
            self.process.kill()
            print("Forced kill")
        except OSError as e:
            print ("Terminated gracefully")

class Client():

    def __init__(self, host, port) -> None:
        self.host = host
        self.port = port

    def send_once(self, channel, message) -> None:
        '''
           Function to send the message
        '''
        try:
            client = udp_client.SimpleUDPClient(self.host, self.port)
            client.send_message("/{}".format(channel), message)
        except Exception as e:
            print("Client Exception {}".format(e))

    def request_response(self, channel, message) -> bytes:
        '''
           Function to send the message and receive a response
        '''
        recv_msg = ""
        try:
            client = udp_client.SimpleUDPClient(self.host, self.port)
            client.send_message("/{}".format(channel), message)
            recv_msg = client.receive("/{}".format(channel))
        except Exception as e:
            print("Client Exception {}".format(e))
        return recv_msg
