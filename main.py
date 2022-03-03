# Se importan los archivos que se utilizarán para organizar el código, de manera que no se tenga todo en un solo archivo
# así como el módulo os para darle un aspecto estético más agradable al código al ejecutarse en consola
import Zero_r_creation, Create_dataframe
import os

# La variable end_programm nos ayudará a mantener abierto el programa mientras el usuario lo desee
end_programm = False

# Se crean dos funciones las cuales nos ayudarán a ejecutar un archivo u otro según el usuario lo desee
def create_new_zero_r_model():
    print('Creating new csv for zero-r')
    Zero_r_creation.open_and_create_csv()

def use_train_test_with_zero_r():
    print('Using train-test with zero-r')
    Create_dataframe.dataframe_zero_r()

# Se crea un ciclo while para mantener abierto el programa mientras el usuario lo desee
while(end_programm == False):
    # Utilizamos try except para poder mantener abierto el programa en caso de que, al elegir una opción, el usuario
    # ingrese un valor distinto a un integer, evitando fallos en el código
    try:
        menu = int(input('What do you wanna do now?:\n1: Create new csv for zero-r\n2: Implement zero-r\n3: End programm\n'))
        if menu == 1:
            create_new_zero_r_model()
        elif menu == 2:
            use_train_test_with_zero_r()
        elif menu == 3:
            print('Bye bye')
            end_programm = True 
        else:
            print('That is not an option. Try again')
            os.system('pause')
            os.system('cls')
    except ValueError:
        print('You must use integer to select an option. Try again')
        os.system('pause')
        os.system('cls')