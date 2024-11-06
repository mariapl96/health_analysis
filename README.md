# health_analysis
Health analysis based on proprietary analytics. Extraction of information from PDFs and subsequent analysis.


my_pdf_project/
│
├── src/                       # Código principal del proyecto
│   ├── pdf_extractor.py        # Extracción de datos de PDFs
│   ├── db_manager.py           # Funciones para base de datos
│   ├── excel_exporter.py       # Exportación a Excel
│   ├── data_analysis.py        # Análisis de datos
│   └── __init__.py             # Define src como paquete
│
├── scripts/                   # Scripts auxiliares
│   ├── run_extraction.py       # Ejecuta el proceso completo de extracción
│   ├── setup_database.py       # Inicializa la base de datos (crear tablas, etc.)
│   ├── export_to_excel.py      # Script para ejecutar la exportación a Excel
│   └── analyze_data.py         # Ejecuta el análisis de datos
│
├── data/                       # Directorio para almacenar datos temporales
│   ├── input_pdfs/             # PDFs a procesar
│   ├── output_excel/           # Exportaciones de Excel
│   └── database/               # Almacén de base de datos o dumps de datos
│
├── tests/                      # Pruebas del proyecto
│   ├── test_pdf_extractor.py    # Pruebas unitarias para pdf_extractor.py
│   ├── test_db_manager.py       # Pruebas para la base de datos
│   ├── test_excel_exporter.py   # Pruebas para exportación a Excel
│   └── test_data_analysis.py    # Pruebas para análisis de datos
│
├── requirements.txt            # Lista de dependencias para instalar
├── README.md                   # Documentación general del proyecto
└── .gitignore                  # Archivos a ignorar por Git (p.ej., archivos de datos)



1. Crear venv
python -m venv nombre_del_entorno
nombre_del_entorno\Scripts\activate

Paso 1: Leer y Extraer Texto del PDF
Lo primero es leer el contenido del PDF. Como los PDFs que contienen tablas o datos estructurados pueden tener problemas con la extracción directa del texto, pdfplumber puede ser una buena opción para extraer tanto texto como tablas.

Paso 2: Uso de pdfplumber para Extraer Texto y Tablas

Paso 3: Filtrar la Información Específica (Fecha, Parámetros, Resultados)
Ahora que tienes el texto del PDF, puedes usar expresiones regulares para extraer las partes clave del análisis de sangre. Las expresiones regulares son útiles para identificar patrones específicos, como la fecha, los parámetros de la prueba, los resultados, las unidades y los valores de referencia.

Ejemplo de Extracción con Expresiones Regulares
El siguiente es un ejemplo básico para filtrar estos campos en el texto del PDF. Este es un punto de partida y necesitarás adaptarlo según cómo se estructuren los datos en el PDF.

Paso 4: Formatear y Almacenar los Datos
Una vez que hayas extraído la información clave (fecha, parámetros, resultados, unidades y valores de referencia), puedes almacenar estos datos en un formato estructurado, como un DataFrame de pandas. Esto te permitirá manipular los datos y exportarlos a Excel o bases de datos más fácilmente.