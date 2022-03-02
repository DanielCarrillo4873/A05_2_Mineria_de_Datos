# Se importan los módulos pandas (para abrir el archivo csv y poder realizar operaciones con este) y random para poder crear
# la descripción del modelo con Zero-R en caso de que haya un empate en la cantidad de instancias con el mismo valor de la clase
import pandas as pd
import random
# Se crea un string vacío el cual servirá para crear la descripción del modelo con Zero-R
value = ''
# Abrimos el archivo cancer.csv y lo asignamos a la variable df
df = pd.read_csv("cancer.csv")
# Imprimimos su contenido para verificar que se haya abierto correctamente
print(df)
# Reemplazamos los guiones medios por guiones bajos para poder manipular la información correctamente
df['recurrence'] = df['recurrence'] .str.replace('-', '_')
# Almacenamos en dos variables distintas la cantidad de veces que encontremos el valor de no_recurrence_events y recurrence_events
# en nuestra clase para poder llevar a cabo la descripción del modelo con Zero-R
no_recurrence_events = df.recurrence.value_counts().no_recurrence_events
recurrence_events = df.recurrence.value_counts().recurrence_events
# Imprimimos la cantidad de veces que se encontró cada uno de los dos posibles valores
print(no_recurrence_events)
print(recurrence_events)
# Dependiendo del valor más repetido asignamos un valor a la variable value
if no_recurrence_events > recurrence_events:
	value = 'no-recurrence-events'
elif recurrence_events > no_recurrence_events:
	value = 'recurrence_events'
else:
	decision = random.randint(0, 1)
	if decision == 0:
		value = 'no-recurrence-events'
	else:
		value = 'recurrence-events'
# Añadimos una nueva columna al archivo cancer.csv llamada "model" cuyos valores predeterminados serán el valor asignado para la
# descripción del modelo
df["model"]=value
# Sobreescribimos nuestro archivo para guardar los cambios agregados
df.to_csv ("cancer_zero_r.csv", index = False, header=True)
print('New file created')