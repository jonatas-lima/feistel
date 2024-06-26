from socket import socket, AF_INET, SOCK_STREAM
from feistel import Feistel

feistel_client = Feistel("./secrets/secret_key")

serverPort = 12000
# Cria o Socket TCP (SOCK_STREAM) para rede IPv4 (AF_INET)
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
# Socket fica ouvindo conexoes. O valor 1 indica que uma conexao pode ficar na fila
serverSocket.listen(1)

print("Servidor pronto para receber mensagens. Digite Ctrl+C para terminar.")

while 1:
    # Cria um socket para tratar a conexao do cliente
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    print("Recebido encryptado:", sentence)

    decrypted_message = feistel_client.decrypt(sentence.decode("ascii"))
    print("Mensagem desencriptada:", decrypted_message)

    capitalizedSentence = decrypted_message.upper()
    print("Mensagem transformada:", capitalizedSentence)

    encrypted_response = feistel_client.encrypt(capitalizedSentence)

    connectionSocket.send(encrypted_response.encode("ascii"))
    connectionSocket.close()
