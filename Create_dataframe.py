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
        # Se declaran tres variables. aux_train  y aux_test nos ayudarán a calcular la exactitud total de todas las
        # iteraciones. iteration nos ayudará a llevar un control de la cantidad de iteraciones realizadas
        aux_train = 0
        aux_test = 0
        iteration = 1
        df = pd.read_csv("cancer_zero_r.csv")
        df['model'] = df['model'] .str.replace('-', '_')
        while(iteration <= iterations):
            print('Iteration number: '+str(iteration))
            print(df.shape[0])
            # Las variables train y test se asignan a la función train_test_split la cual recibe nuestro archivo y una variable
            # con el porcentaje que deseamos para cada uno de los subconjuntos. En este caso indicamos un tamaño de 0.3 para que
            # divida el conjunto en 70:30. A su vez, el conjunto entero se aleatoriza antes de dividrse
            train, test = train_test_split(df, test_size=0.3)
            # Se imprime el subconjunto train y test para poder visualizar la cantidad de filas y verificar que se realizaran
            # correctamente ambos subconjuntos
            print(train)
            print(test)
            print('\n')
            # En ambos subconjuntos se crean nuevas columnas en cada iteración la cual contendrá el valor True o False,
            # dependiendo de si el valor deñ atributo recurrence es igual al del atributo model
            train["errors"] = train["recurrence"] == train["model"]
            test["errors"] = test["recurrence"] == test["model"]
            # Como los valores del nuevo atributo son booleanos se intercambian estos valores por otros de tipo string
            mask = train.applymap(type) != bool
            d = {True: 'TRUE', False: 'FALSE'}
            train = train.where(mask, train.replace(d))
            mask = test.applymap(type) != bool
            d = {True: 'TRUE', False: 'FALSE'}
            test = test.where(mask, test.replace(d))
            # Una vez convertidos a tipo string podemos contabilizar la cantidad de veces que el algoritmo funcionó en
            # ambos subconjuntos para poder calcular la exactitud
            hits_train = train.errors.value_counts().TRUE
            hits_test = test.errors.value_counts().TRUE
            print('Total hits in train subset: '+str(hits_train))
            print('Accuracy in test subset: '+str(hits_test)+'\n')
            # Para calcular la exactitud de Zero-R en la iteración en cuestión se divide la cantidad de aciertos entre
            # la cantidad de sentencias del subconjunto y este resultado se multiplica por 100
            print('Accuracy in train subset: '+str("{:.2f}".format((hits_train/train.shape[0])*100))+'%')
            print('Accuracy in test subset: '+str("{:.2f}".format((hits_test/test.shape[0])*100))+'%')
            print('\n\n')
            # Se suma el porcentaje obtenido en la iteración a nuestras variables auxiliares
            aux_train += (hits_train/train.shape[0])*100
            aux_test += (hits_test/test.shape[0])*100
            os.system('pause')
            iteration += 1
        os.system('cls')
        # Obtenemos la exactitud total dividiendo nuestras variables auxiliares entre la cantidad de iteraciones realizadas
        total_accuracy_train = aux_train/iterations
        total_accuracy_test = aux_test/iterations
        print('The total accuracy of Zero-R with a train subset is: '+str("{:.2f}".format(total_accuracy_train))+'%')
        print('The total accuracy of Zero-R with a test subset is: '+str("{:.2f}".format(total_accuracy_test))+'%')
        os.system('pause')
        os.system('cls')
    except FileNotFoundError:
        print("The file 'cancer_zero_r.csv' wasn't found. Check that it is in the right directory or create it first")
        os.system('pause')
        os.system('cls')