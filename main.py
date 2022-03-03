# Se importan los archivos que se utilizarán para organizar el código, de manera que no se tenga todo en un solo archivo
# así como el módulo os para darle un aspecto estético más agradable al código al ejecutarse en consola
import Zero_r_creation, Create_dataframe
import os

# La variable end_program nos ayudará a mantener abierto el programa mientras el usuario lo desee
end_program = False

# Se crean dos funciones las cuales nos ayudarán a ejecutar un archivo u otro según el usuario lo desee
def create_new_zero_r_model():
    print('Creating new csv for zero-r')
    Zero_r_creation.open_and_create_csv()

# Se pasa el parámetro iterations para poder realizar las iteraciones que el usuario desee al momento de calcular
# el porcentaje de error de zero-r
def use_train_test_with_zero_r(iterations):
    print('Using train-test with zero-r')
    Create_dataframe.dataframe_zero_r(iterations)

# Se crea un ciclo while para mantener abierto el programa mientras el usuario lo desee
while(end_program == False):
    # Utilizamos try except para poder mantener abierto el programa en caso de que, al elegir una opción, el usuario
    # ingrese un valor distinto a un integer, evitando fallos en el código
    try:
        menu = int(input('What do you wanna do now?:\n1: Create cancer_zero_r.csv file\n2: Implement zero-r\n3: End programm\n'))
        if menu == 1:
            create_new_zero_r_model()
        elif menu == 2:
            iterations = int(input('Enter the number of iterations you want to make: '))
            use_train_test_with_zero_r(iterations)
        elif menu == 3:
            print('Bye bye')
            end_program = True 
        else:
            print('That is not an option. Try again')
            os.system('pause')
            os.system('cls')
    except ValueError:
        print('You must use integer to select an option. Try again')
        os.system('pause')
        os.system('cls')