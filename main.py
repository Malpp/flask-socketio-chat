from flask import Flask 
from flask_socketio import SocketIO, send
from threading import Thread

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

threads = []

def downloadImage(url):
    print("Hello")
    print(len(threads))
    pass

@app.route('/')
def hello_world():
    return 'Hello, World!'
    

@socketio.on('message')
def handleMessage(msg):
	print('Message: ' + msg)
	send(msg, broadcast=True)

@socketio.on('image')
def handleMessage(msg):
    print('URL: ' + msg)
    threads.append(Thread(target=downloadImage, args=(msg,)).start())
	#send(msg, broadcast=True)

if __name__ == '__main__':
	socketio.run(app)