import pandas as pd

def create_blood_test_dataframe(dates, tests, units, reference_values):
    # Crear un DataFrame para almacenar los datos
    data = {
        'Fecha': dates,
        'Prueba': [test[0] for test in tests],
        'Resultado': [test[1] for test in tests],
        'Unidad': units,
        'Valores de referencia': reference_values
    }

    df = pd.DataFrame(data)
    return df

# Crear DataFrame con los datos extraídos
df = create_blood_test_dataframe(dates, tests, units, reference_values)

# Mostrar el DataFrame
print(df)

# Guardar el DataFrame en un archivo Excel
df.to_excel("blood_tests_results.xlsx", index=False)
