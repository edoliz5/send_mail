from flask import Flask, request, jsonify, render_template
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# Configuración de Flask-Mail para enviar correos electrónicos
app.config['MAIL_SERVER'] = 'smtp.office365.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'sinteg@efesur.cl'
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_DEFAULT_SENDER'] = ('SINTEG', 'sinteg@efesur.cl') 

mail = Mail(app)

@app.route('/')
def index():
    return "Hello, world"

@app.route('/enviar_correo', methods=['GET'])
def enviar_correo():
    try:
        # Obtener datos del request
        # data = request.json
        destinatarios = ['elizama@alumnos.ubiobio.cl']
        asunto = 'correo de prueba'
        
        # Enviar correo electrónico
        message = Message(subject=asunto, bcc=destinatarios)
        message.html = render_template('mail.html', username='Eduardo')
       
        mail.send(message)
        return jsonify({'mensaje': 'Correo enviado'})
        #return render_template('mail.html', username='Eduardo')
    except Exception as e:
        return jsonify({'error': f'Error al enviar el correo: {str(e)}'})
    
if __name__ == '__main__':
    app.run(debug=True)
