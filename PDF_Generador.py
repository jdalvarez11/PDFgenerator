import os
import random
from fpdf import FPDF
from essential_generators import DocumentGenerator
from random_word import RandomWords

gen = DocumentGenerator()
r = RandomWords()

def generar_texto_aleatorio():
    texto = ""
    while len(texto.split()) < 500:
        oracion = generar_oracion_aleatoria()
        # Reemplaza los caracteres que no están en 'latin-1' con un signo de interrogación
        oracion = oracion.encode('latin-1', 'replace').decode('latin-1')
        texto += oracion + " "
    return texto

def generar_oracion_aleatoria():
    return gen.sentence()

def generar_nombre_documento(nombres_generados):
    tipos_documento = ["Diagram", "Lab_Report", "Summary", "Analysis"]
    nombre_documento = r.get_random_word() + "_" + random.choice(tipos_documento)
    while nombre_documento in nombres_generados:
        nombre_documento = r.get_random_word() + "_" + random.choice(tipos_documento)
    return nombre_documento

def generar_pdf(cantidad):
    if not os.path.exists('PDFs'):
        os.makedirs('PDFs')

    textos_generados = set()
    nombres_generados = set()
    i = 0
    while i < cantidad:
        texto = generar_texto_aleatorio()
        if texto not in textos_generados:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size = 15)
            pdf.multi_cell(0, 10, txt = texto)
            nombre_documento = generar_nombre_documento(nombres_generados)
            pdf.output(f'PDFs/{nombre_documento}.pdf')
            textos_generados.add(texto)
            nombres_generados.add(nombre_documento)
            i += 1

def main():
    cantidad = int(input("Introduce la cantidad de documentos a generar: "))
    generar_pdf(cantidad)
    print("PDFs Generados")

if __name__ == "__main__":
    main()
