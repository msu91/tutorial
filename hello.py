from flask import Flask, render_template, request, json, jsonify
app = Flask(__name__)


@app.route('/')
def root():
    return 'root'


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

# rest test
@app.route('/hello', methods=['POST'])
def hello_post():
    response_dict = dict(hoge="post")
    response = jsonify(response_dict)
    return response


if __name__ == '__main__':
    app.run()
