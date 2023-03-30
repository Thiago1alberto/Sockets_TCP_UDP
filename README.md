# Exemplo de Sockets com TCP e UDP em Python
Este repositório contém dois exemplos de implementação de sockets em Python, um utilizando o protocolo TCP e outro utilizando o protocolo UDP.

# Protocolo TCP
- O protocolo TCP (Transmission Control Protocol) é um protocolo orientado a conexão e confiável, utilizado para garantir que os dados sejam entregues ao destino sem erros e na ordem correta.

- O exemplo de implementação de sockets com TCP é composto por duas classes: Cliente e Servidor. O cliente envia mensagens para o servidor e recebe as respostas correspondentes. O servidor recebe as mensagens do cliente e envia as respostas correspondentes.

# Resultado da execução
- Execute o servidor TCP:
 ``` python servidor_tcp.py  ``` 
- Execute o cliente TCP em outro terminal e envie as mensagens desejadas:
 ```  python cliente_tcp.py ``` 
- Digite uma mensagem: Olá, servidor!
- Mensagem enviada para o servidor: Olá, servidor!
- Resposta do servidor: Resposta do servidor: Olá, servidor!
# Protocolo UDP
- O protocolo UDP (User Datagram Protocol) é um protocolo sem conexão e não confiável, utilizado para enviar mensagens curtas com baixa latência.

- O exemplo de implementação de sockets com UDP é composto por duas classes: Cliente e Servidor. O cliente envia mensagens para o servidor e recebe as respostas correspondentes. O servidor recebe as mensagens do cliente e envia as respostas correspondentes.

# Resultado da execução
- Execute o servidor UDP:
 ``` python servidor_udp.py ``` 
- Execute o cliente UDP em outro terminal e envie as mensagens desejadas:
 ``` python cliente_udp.py  ``` 
- Digite uma mensagem: Olá, servidor!
- Mensagem enviada para o servidor: Olá, servidor!
- Resposta do servidor: Resposta do servidor: Olá, servidor!
# Conclusão
Este repositório apresentou dois exemplos de implementação de sockets em Python utilizando os protocolos TCP e UDP. Ambos os exemplos consistem em um cliente que envia mensagens para um servidor e recebe as respostas correspondentes. A escolha do protocolo a ser utilizado depende das necessidades do projeto em questão. Se é necessário confiabilidade e entrega de pacotes na ordem correta, o protocolo TCP é o mais indicado. Se, por outro lado, a latência é um fator crítico, o protocolo UDP pode ser mais adequado.
