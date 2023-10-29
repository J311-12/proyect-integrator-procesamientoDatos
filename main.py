import numpy as np
import pandas as pd

def limpiar_datos(df):
 

  # Verificando que no existan valores faltantes

  if df.isnull().values.any():
    raise ValueError("El DataFrame contiene valores faltantes")

  # Verificando que no existan filas repetidas

  if df.duplicated().values.any():
    raise ValueError("El DataFrame contiene filas repetidas")

  # Verificando si existen valores atípicos y los eliminamos

  for col in df.columns:
    if df[col].dtype.name == "float32":
      # Calculando los límites inferior y superior del 99% de los datos
      Q1 = df[col].quantile(0.25)
      Q3 = df[col].quantile(0.75)
      IQR = Q3 - Q1

      # Eliminando los valores que se encuentran fuera de los límites
      df = df.loc[(df[col] >= Q1 - 1.5 * IQR) & (df[col] <= Q3 + 1.5 * IQR)]

  # Creando una columna que categorice por edades

  def edad_categoria(edad):
    if edad <= 12:
      return "Niño"
    elif edad <= 19:
      return "Adolescente"
    elif edad <= 39:
      return "Jóvenes adulto"
    elif edad <= 59:
      return "Adulto"
    else:
      return "Adulto mayor"

  df["edad_categoria"] = df["age"].apply(edad_categoria)

  return df


# Cargando los datos
df = pd.read_csv("datos.csv")

# Limpiando los datos
df = limpiar_datos(df)

# Guardando los datos limpios
df.to_csv("datos_limpios.csv", index=False)
