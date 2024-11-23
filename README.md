# JPG-to-Cartoon 
 
# **Aplicación Web para Procesamiento de Imágenes**

Esta es una aplicación web desarrollada con **Flask**, diseñada para permitir a los usuarios cargar imágenes, procesarlas mediante un script Python, y visualizar y descargar los resultados. La aplicación es completamente funcional, con un enfoque en simplicidad y escalabilidad. Además, puede ser fácilmente contenedorizada usando Docker para facilitar su despliegue.
![image](https://github.com/user-attachments/assets/716168f4-997f-4d23-80b3-83e69a775228)

---

## **Características**

- **Subida de Imágenes**: Los usuarios pueden cargar imágenes desde sus dispositivos.
- **Procesamiento Personalizado**: Las imágenes cargadas son procesadas mediante un script Python (`process.py`) que aplica transformaciones específicas.
- **Visualización de Resultados**: Las imágenes procesadas se muestran en una galería junto con la opción de descarga.
- **Historial de Imágenes**: Muestra las imágenes procesadas más recientes en la página principal.
- **Compatibilidad Docker**: La aplicación puede ejecutarse en un contenedor Docker, lo que facilita su implementación en entornos productivos.

---

## **Requisitos Previos**

Asegúrate de tener las siguientes herramientas instaladas:

- **Python 3.8+**
- **pip** (gestor de paquetes de Python)
- **Docker** (opcional, para contenedores)

---

## **Estructura del Proyecto**

```plaintext
├── app.py                # Archivo principal de la aplicación Flask
├── process.py            # Script para procesar imágenes
├── templates/            # Archivos HTML para las vistas (index y results)
│   ├── index.html
│   └── results.html
├── static/               # Archivos estáticos (CSS, JS, imágenes)
├── inputs/               # Carpeta para almacenar imágenes cargadas
├── outputs/              # Carpeta para almacenar imágenes procesadas
├── requirements.txt      # Dependencias de Python
├── Dockerfile            # Archivo para construir la imagen Docker
└── README.md             # Documentación del proyecto
```

## **Instalación y Configuración**
1. Clonar el Repositorio
"git clone https://github.com/tu-usuario/tu-repositorio.git"
"cd tu-repositorio"

## **2. Crear un Entorno Virtual**
"python -m venv venv"
"source venv/bin/activate"   # En Windows: venv\Scripts\activate

## **3. Instalar Dependencias**
"pip install -r requirements.txt"

## **4. Ejecutar la Aplicación**
"python app.py"
La aplicación estará disponible en http://127.0.0.1:5000.

**Uso**
Abre la aplicación en tu navegador (http://127.0.0.1:5000).
Carga una imagen desde tu dispositivo.
Visualiza la imagen procesada en la sección de resultados.
Descarga la imagen procesada si lo deseas.

**Uso con Docker**
Construir la Imagen
"docker build -t image-processor ."
Ejecutar el Contenedor
"docker run -p 5000:5000 -v $(pwd)/inputs:/app/inputs -v $(pwd)/outputs:/app/outputs image-processor"
La aplicación estará disponible en http://127.0.0.1:5000.

**Mejoras Futuras**
Incorporar una interfaz para que los usuarios configuren parámetros personalizados para el procesamiento de imágenes.
Agregar autenticación para proteger el acceso a la galería de imágenes procesadas.
Soporte para más formatos de archivo y transformaciones de imágenes.
Integración con servicios en la nube para almacenamiento y procesamiento escalable.

