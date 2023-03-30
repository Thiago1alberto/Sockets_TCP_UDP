import socket

HOST = ''  # endereço do servidor (em branco indica que o servidor pode receber conexões em qualquer endereço)
PORT = 1234  # porta em que o servidor vai ouvir as conexões

# cria um objeto socket TCP/IP
servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# vincula o objeto socket à um endereço e porta específicos
servidor_socket.bind((HOST, PORT))

# inicia a escuta por conexões
servidor_socket.listen(1)

print('Servidor aguardando conexões na porta', PORT)

# aguarda a conexão de um cliente
conexao, endereco_cliente = servidor_socket.accept()

print('Conexão estabelecida com o cliente', endereco_cliente)

# envia a mensagem de boas-vindas ao cliente
mensagem_boas_vindas = 'Bem-vindo ao servidor TCP!'
conexao.sendall(mensagem_boas_vindas.encode())

while True:
    # espera por uma mensagem do cliente
    mensagem = conexao.recv(1024).decode()
    
    # se o cliente encerrou a conexão, encerra o loop
    if not mensagem:
        break
    
    print('Mensagem recebida do cliente:', mensagem)
    
    # envia uma resposta ao cliente
    resposta = 'Resposta do servidor: ' + mensagem
    conexao.sendall(resposta.encode())
    
    print('Mensagem enviada para o cliente:', resposta)

# fecha a conexão com o cliente
conexao.close()

# encerra o objeto socket do servidor
servidor_socket.close()
import socket

HOST = ''  # endereço do servidor (em branco indica que o servidor pode receber conexões em qualquer endereço)
PORT = 1234  # porta em que o servidor vai ouvir as conexões

# cria um objeto socket TCP/IP
servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# vincula o objeto socket à um endereço e porta específicos
servidor_socket.bind((HOST, PORT))

# inicia a escuta por conexões
servidor_socket.listen(1)

print('Servidor aguardando conexões na porta', PORT)

# aguarda a conexão de um cliente
conexao, endereco_cliente = servidor_socket.accept()

print('Conexão estabelecida com o cliente', endereco_cliente)

# envia a mensagem de boas-vindas ao cliente
mensagem_boas_vindas = 'Bem-vindo ao servidor TCP!'
conexao.sendall(mensagem_boas_vindas.encode())

while True:
    # espera por uma mensagem do cliente
    mensagem = conexao.recv(1024).decode()
    
    # se o cliente encerrou a conexão, encerra o loop
    if not mensagem:
        break
    
    print('Mensagem recebida do cliente:', mensagem)
    
    # envia uma resposta ao cliente
    resposta = 'Resposta do servidor: ' + mensagem
    conexao.sendall(resposta.encode())
    
    print('Mensagem enviada para o cliente:', resposta)

# fecha a conexão com o cliente
conexao.close()

# encerra o objeto socket do servidor
servidor_socket.close()
