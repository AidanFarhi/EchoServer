from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    print({'status': 'alive'})
    return {'status': 'alive'}

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json(force=True)
    print(data)
    return {'received': data}

if __name__ == '__main__':
    app.run('0.0.0.0', 8080)
