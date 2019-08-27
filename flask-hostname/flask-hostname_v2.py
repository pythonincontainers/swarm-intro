from flask import Flask, request
app = Flask(__name__)

import socket
hostname = socket.gethostname()

@app.route('/')
def hello_world():
    return 'Flask Hello world! This is Version 2 and I am running on '+hostname

@app.route('/test')
def test():
    message = 'Testing hidden functionality ;) \n'
    message += 'request.host='+request.host+'\n'
    message += 'request.remote_addr='+request.remote_addr+'\n'
    try:
        secret_file = open("/run/secrets/my_password", "r")
    except:
        pass
    else:
        message += 'my_password is '+secret_file.read()+'\n'
    return message

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
