import pdfplumber

# Leer texto de pdf
def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Ejemplo de uso
pdf_text = extract_text_from_pdf("path/to/your/file.pdf")
print(pdf_text)


# Extraer informacion relevante
import re

def extract_blood_test_data(pdf_text):
    # Expresión regular para extraer la fecha
    date_pattern = r"Fecha: (\d{2}/\d{2}/\d{4})"  # Ajusta el formato según tu PDF
    dates = re.findall(date_pattern, pdf_text)

    # Expresión regular para extraer los parámetros y los resultados
    # Suponiendo que los parámetros siguen la palabra 'Prueba' y los resultados siguen la palabra 'Resultado'
    test_pattern = r"Prueba:\s*([\w\s]+)\s+Resultado:\s*([\d.]+)\s+Unidad:\s*([\w/]+)\s+Valores de referencia:\s*([\d\-]+)"
    tests = re.findall(test_pattern, pdf_text)

    # Extraer unidades y valores de referencia
    unit_pattern = r"Unidad:\s*([\w/]+)"
    reference_pattern = r"Valores de referencia:\s*([\d\-]+)"
    units = re.findall(unit_pattern, pdf_text)
    reference_values = re.findall(reference_pattern, pdf_text)

    return dates, tests, units, reference_values

# Ejemplo de uso
dates, tests, units, reference_values = extract_blood_test_data(pdf_text)

# Mostrar los resultados
print(f"Fechas: {dates}")
print(f"Pruebas y Resultados: {tests}")
print(f"Unidades: {units}")
print(f"Valores de referencia: {reference_values}")
