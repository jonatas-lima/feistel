test:
	python3 tests.py

server:
	python3 TCPServer.py &

kill:
	pkill -f TCPServer.py

send:
	python3 TCPClient.py $(message)
