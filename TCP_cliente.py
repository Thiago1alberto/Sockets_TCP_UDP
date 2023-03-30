import socket

HOST = 'localhost'  # Endereço IP do servidor
PORT = 1234         # Porta que o servidor está ouvindo

# cria um socket TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # conecta ao servidor
    s.connect((HOST, PORT))
    print('Cliente conectado ao servidor na porta', PORT)

    # envia mensagens para o servidor e recebe as respostas
    while True:
        mensagem = input("Digite uma mensagem: ")
        s.sendall(mensagem.encode())
        print('Mensagem enviada para o servidor:', mensagem)
        data = s.recv(1024).decode()
        print('Resposta do servidor:', data)
