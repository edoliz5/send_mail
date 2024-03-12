from flask import Flask
from flask_mail import Mail, Message

app= Flask(__name__)

@app.route('/')
def index():
    return "hola"

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)