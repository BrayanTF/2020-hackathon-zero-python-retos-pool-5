#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    #Creamos una string con todos los caracteres para acceder aleatoriamente a ella 
    characters = string.ascii_letters + string.digits + string.punctuation

    token = ""
    #
    # Recorremos hasta la longitud del token y en cada iteracion cogemos 1 caracter random
    for x in range(passLen):
        token += characters[random.randint(0, len(characters) - 1)]
    
    #
    #

    return token
