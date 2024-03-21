# Feistel Básico

O algoritmo de Feistel divide os dados em dois blocos, esquerdo e direito, e aplica funções de transformação repetidas vezes em um processo chamado de "rodada". Cada rodada usa uma chave diferente, que é derivada da chave de criptografia original (`./secrets/secret_key`). A decifragem da mensagem ocorre quase que da mesma forma que a cifragem, com a diferença de que as chaves serão aplicadas na ordem reversa.

A estrutura de Feistel permite a construção de uma ampla variedade de cifras de bloco e tem sido usada para desenvolver muitos sistemas de criptografia simétrica, incluindo DES (Data Encryption Standard) e muitos de seus sucessores.

## Executando

### Chave

A chave a ser usada para criptografar e decriptografar a mensagem está em `./secrets/secret_key`. Modifique o conteúdo como você quiser.

### Servidor

Para iniciar o servidor em background:

```sh
make server
```

> Depois dê um enter pra sair da mensagem.

Para parar o processo do servidor:

```sh
make kill
```

### Client

Para mandar uma mensagem:

```sh
make send message='minha mensagem'
```

Para mandar um arquivo de texto:

```sh
make send-file file=./caminho/do/meu/arquivo
```

### Testes

Para rodar os testes no arquivo `tests.py`:

```sh
make test
```
