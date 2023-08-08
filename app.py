from flask import Flask, request
app = Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/get-hook',methods=['POST','GET'])
def get_hook():
    if request.method == 'POST':
        print(request.json.head_commit.message)
    return 'Hello, World!'
