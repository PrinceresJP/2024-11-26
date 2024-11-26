from flask import Flask, request
app = Flask(__name__)

# サーバールートへアクセスがあった時 --- (*1)
@app.route('/')
def index():
    # フォームを表示する --- (*2)
    return """
        <html><body>
        <form action="/hello" method="GET">
          <label>名前: </label><input type="text" name="name"><br>
          <label>一言: </label><input type="text" name="word"><br>
          <input type="submit" value="送信">
        </form>
        </body></html>
    """

# /hello へアクセスがあった時 --- (*3)
@app.route('/hello')
def hello():
    # nameのパラメータを得る --- (*4)
    name = request.args.get('name')
    word = request.args.get('word')
    
    if name is None: 
        name = '名無し'
    if word is None:
        word = '言無し'
    
    return """
    <h1>{0}さん、こんにちは！</h1>
    <h2>{1}</h2>
    """.format(name, word)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

