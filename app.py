from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from process import process_image

app = Flask(__name__)

# Definición de rutas absolutas
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'inputs')  # Ruta completa para 'inputs'
OUTPUT_FOLDER = os.path.join(os.getcwd(), 'outputs')  # Ruta completa para 'outputs'

# Configuración en Flask
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

# Crear las carpetas si no existen
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    # Listar las imágenes en el directorio 'outputs'
    recent_images = os.listdir(app.config['OUTPUT_FOLDER'])

    # Opcional: Filtrar para asegurarte de que solo cargue archivos de imagen
    recent_images = [img for img in recent_images if img.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    # Puedes inicializar processed_image como None si no se necesita aquí
    processed_image = None

    # Pasar las variables al renderizado de la plantilla
    return render_template('index.html', recent_images=recent_images, processed_image=processed_image)

@app.route('/upload', methods=['POST'])
def upload():
    # Verificar si el formulario tiene un archivo
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    # Si no se seleccionó un archivo, devolver el formulario
    if file.filename == '':
        return redirect(request.url)

    # Guardar el archivo en la carpeta 'inputs'
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    # Procesar la imagen usando el script 'process.py'
    processed_image_path = process_image(file.filename)

    # Obtener el nombre de la imagen procesada
    processed_image_filename = os.path.basename(processed_image_path)
    print(processed_image_filename)

    # Redirigir a la página de resultados con la imagen procesada
    return redirect(url_for('results', filename=processed_image_filename))

@app.route('/results/<filename>')
def results(filename):
    return render_template('results.html', filename=filename)

# Servir imágenes procesadas
@app.route('/outputs/<filename>')
def serve_output(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)



