from socket import AF_INET, SOCK_STREAM, socket

from feistel import Feistel
import sys


feistel_client = Feistel("./secrets/secret_key")
serverName = "127.0.0.1"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
args = sys.argv[1:]

# Conecta ao servidor
clientSocket.connect((serverName, serverPort))

# Recebe mensagem do usuario e envia ao servidor
if len(args) > 0:
    message = ' '.join(args)
else:
    message = input("Digite uma frase: ")

secret_message = feistel_client.encrypt(message)

print("Enviando mensagem encriptada:", secret_message)
clientSocket.send(secret_message.encode("ascii"))

# Aguarda mensagem de retorno e a imprime
modifiedMessage, addr = clientSocket.recvfrom(2048)
print("Mensagem recebida do servidor:", modifiedMessage)

decrypted_message = feistel_client.decrypt(modifiedMessage.decode("ascii"))
print("Retorno do Servidor desencriptado:", decrypted_message)

clientSocket.close()
