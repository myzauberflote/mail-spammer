import smtplib
import random
from time import sleep

toadress = str(input('Digite o destinatário: ')) # Type e-mail adress that we want to receive the message

dicio = {} # Initialize dict that will store the mail address as key and password as value

message = '''
Type your message here!
You can type multiple lines.
'''

with open('emails.txt') as f:
    lista = f.readlines() # File reading and list creation containing all the line infos

for string in lista:
    '''
    Here we separate mail adress and password in the string and store them on the dict
    '''
    pos_virgula = string.find(',')
    email = string[:pos_virgula]
    senha = string[pos_virgula+1:].replace('\n','')
    dicio[email] = senha

while True:
    fromadress, password = random.choice(list(dicio.items())) # Inside the loop, the random choice from the dict
    username = fromadress

    server = smtplib.SMTP('smtp.gmail.com',587) # Starting connection to gmail server
    server.ehlo()
    server.starttls()
    server.login(username,password) # Login with username and password

    server.sendmail(fromadress,toadress,message)
    print('Mail sent!')
    sleep(1) # One second wait before another sending

server.quit()
