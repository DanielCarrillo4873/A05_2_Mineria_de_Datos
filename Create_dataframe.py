# Se importa train_test_split del módulo sklearn el cual nos ayudará a dividir nuestro dataframe en el porcentaje deseado.
# En este caso se opta por 70:30. A su vez se importa pandas para abrir nuestros archivos y os para refrescar la terminal
# y darle un aspecto más estético
from sklearn.model_selection import train_test_split
import pandas as pd
import os

# Se crea la función dataframe_zerro_r la cual nos servirá para dividir nuestro archivo específico para zero-r en un
# porcentaje de 70:30. Siendo 70% para entrenamiento y 30% para prueba
def dataframe_zero_r(iterations):
    # Utilizamos try except para evitar fallos por falta del archivo requerido para funcionar
    try:
        iteration = 1
        while(iteration <= iterations):
            print('Iteration number: '+str(iteration))
            df = pd.read_csv("cancer_zero_r.csv")
            # Las variables train y test se asignan a la función train_test_split la cual recibe nuestro archivo y una variable
            # con el porcentaje que deseamos para cada uno de los subconjuntos. En este caso indicamos un tamaño de 0.3 para que
            # divida el conjunto en 70:30. A su vez, el conjunto entero se aleatoriza antes de dividrse
            train, test = train_test_split(df, test_size=0.3)
            # Se imprime el subconjunto train y test para poder visualizar la cantidad de filas y verificar que se realizaran
            # correctamente ambos subconjuntos
            print(train)
            print(test)
            print('\n\n')
            os.system('pause')
            iteration += 1
        os.system('cls')
    except FileNotFoundError:
        print("The file 'cancer_zero_r.csv' wasn't found. Check that it is in the right directory or create it first")
        os.system('pause')
        os.system('cls')