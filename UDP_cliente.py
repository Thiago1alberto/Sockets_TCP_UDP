import socket

HOST = 'localhost'  # Endereço IP do servidor
PORT = 1234         # Porta que o servidor está ouvindo

# cria um socket UDP
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    # envia mensagens para o servidor e recebe as respostas
    while True:
        mensagem = input("Digite uma mensagem: ")
        s.sendto(mensagem.encode(), (HOST, PORT))
        print('Mensagem enviada para o servidor:', mensagem)
        data, server = s.recvfrom(1024)
        print('Resposta do servidor:', data.decode())
