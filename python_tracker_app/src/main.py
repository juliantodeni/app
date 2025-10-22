from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return '''
        <form method="POST" action="/post">
            <input name="message" placeholder="Type something" />
            <button type="submit">Send</button>
        </form>
    '''

@app.route('/post', methods=['POST'])
def handle_post():
    data = request.form.get('message')  # get form field named "message"
    return f"<h2>You posted: {data}</h2>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
