from irc import irc

irc = irc()

irc.connect('irc.freenode.com')
irc.user('augustomna201000')
irc.nick('augustomna201000')
irc.auth_without_password()
irc.join('##linux')
irc.join('##javascript')

while True:
    (status, text) = irc.get_text();
    print ('Ok' if status else 'ERR') + ' - ' + text
