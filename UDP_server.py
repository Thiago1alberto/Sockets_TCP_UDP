import socket

HOST = ''  # endereço do servidor (em branco indica que o servidor pode receber conexões em qualquer endereço)
PORT = 1234  # porta em que o servidor vai ouvir as conexões

# cria um objeto socket UDP/IP
servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# vincula o objeto socket à um endereço e porta específicos
servidor_socket.bind((HOST, PORT))

print('Servidor aguardando conexões na porta', PORT)

while True:
    # espera por uma mensagem do cliente
    mensagem, endereco_cliente = servidor_socket.recvfrom(1024).decode()
    
    print('Mensagem recebida do cliente', endereco_cliente, ':', mensagem)
    
    # envia uma resposta ao cliente
    resposta = 'Resposta do servidor: ' + mensagem
    servidor_socket.sendto(resposta.encode(), endereco_cliente)
    
    print('Mensagem enviada para o cliente', endereco_cliente, ':', resposta)

# encerra o objeto socket do servidor
servidor_socket.close()

