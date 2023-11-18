from flask import Flask

app = Flask(__name__)

#测试API
@app.route('/test')
def index():
    return 'success'

#聊天API
@app.route('/chat')
def index():
    return 'success'

if __name__ == '__main__':
    # 指定host和port
    app.run(host='0.0.0.0', port=3096)
