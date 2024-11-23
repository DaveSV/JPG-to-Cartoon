import cv2
import os

def process_image(filename):
    # Rutas de entrada y salida
    input_path = os.path.join("inputs", filename)
    output_path = os.path.join("outputs", f"cartoon_{filename}")

    # Cargar la imagen
    img = cv2.imread(input_path)
    if img is None:
        raise FileNotFoundError(f"La imagen '{filename}' no se pudo cargar.")

    # Convertir a RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Procesar la imagen
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9
    )
    color = cv2.bilateralFilter(img, 9, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    # Guardar la imagen procesada
    cartoon_bgr = cv2.cvtColor(cartoon, cv2.COLOR_RGB2BGR)
    cv2.imwrite(output_path, cartoon_bgr)

    return f"cartoon_{filename}"




