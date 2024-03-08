from flask import Flask, request, jsonify
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# Configuración de Flask-Mail para enviar correos electrónicos
app.config['MAIL_SERVER'] = 'smtp.office365.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'sinteg@efesur.cl'
app.config['MAIL_PASSWORD'] = 'Efesur..2023#'
app.config['MAIL_DEFAULT_SENDER'] = ('SINTEG', 'sinteg@efesur.cl') 

mail = Mail(app)

@app.route('/enviar_correo', methods=['GET'])
def enviar_correo():
    try:
        # Obtener datos del request
        # data = request.json
        destinatarios = ['elizama@alumnos.ubiobio.cl','eduardo.lizama@efesur.cl']
        asunto = 'correo de prueba'
        cuerpo = f'<html><head><style>{get_css_styles()}</style></head><body><b>esto es un correo de prueba</b></body><br><br></html>'
        archivos_adjuntos = ['C:/Users/Eduardo/Desktop/send_mail/archivo_prueba.txt']

        # Enviar correo electrónico
        message = Message(subject=asunto, bcc=destinatarios, html=cuerpo)

        for ruta_archivo in archivos_adjuntos:
            nombre_archivo = os.path.basename(ruta_archivo)
            with app.open_resource(ruta_archivo) as adjunto:
                message.attach(filename=nombre_archivo, content_type='application/octet-stream', data=adjunto.read())

        mail.send(message)

        return jsonify({'mensaje': 'Correo enviado'})
    except Exception as e:
        return jsonify({'error': f'Error al enviar el correo: {str(e)}'})
    
def get_css_styles():
    # Define aquí tus estilos CSS
    css_styles = """
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            color: #333;
        }
        /* Agrega más estilos según sea necesario */
    """
    return css_styles

if __name__ == '__main__':
    app.run(debug=True)
