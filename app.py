import base64
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    hostname = request.host.split(':')[0]
    hello = "SEVMTE9fV09STEQ="
    aloha = "QUxPSEFfR1JFRVRJTkc="
    if 'aloha' in hostname:
        aloha_byte = base64.b64decode(aloha)
        return aloha_byte.decode('utf-8')
    else: 
        hello_byte = base64.b64decode(hello)
        return hello_byte.decode('utf-8')

app.run(host="0.0.0.0", port=8080)
