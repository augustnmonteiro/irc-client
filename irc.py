import socket
import sys

class irc:
    conn = False
    def connect(self, server):
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.connect((server, 6667))
        return self.conn 

    def auth_without_password(self):
        self.conn.send('PRIVMSG nickserv :iNOOPE\r\n')

    def join(self, channel):
        self.conn.send('JOIN ' + channel + '\n')

    def quote(self, quote):
        self.conn.send('QUOTE ' + quote)

    def auth(self, user, password):
        self.quote('auth ' + user + ' ' + password)

    def user(self, user):
        self.conn.send("USER "+ user +" "+ user +" "+ user +" :This is a fun bot!\n")

    def nick(self, nick):
        self.conn.send('NICK ' + nick + '\n')

    def get_text(self):
        text=self.conn.recv(2040)
        if text.find('PING') != -1:
            self.conn.send('PONG ' + text.split() [1] + '\r\n')
        return (True, text)
