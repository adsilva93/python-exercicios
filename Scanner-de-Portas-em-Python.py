print('='*5,'SCANNER DE PORTAS','='*5)
import socket
host = input('Digite o Site ou IP que deseja scannear: ')
portas = int(input('Digite a quantidades de portas a ser scannear: '))
x = 1
ports = []
while x <= portas:
    ports.append(int(input('Digite a porta: ')))
    x += 1


for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.0)
    conexao = s.connect_ex(('host', port))
    if(conexao == 0):
        print (f'Porta aberta {port}')
    else:
        print(f'A porta está fechada:{port}')