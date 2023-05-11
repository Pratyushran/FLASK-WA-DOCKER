from flask import Flask

app = Flask(_name_)

@app.route('/')
def hello():
    return "Hello, Docker!"

if _name_ == '_main_':
    app.run(debug=True, host='0.0.0.0')
