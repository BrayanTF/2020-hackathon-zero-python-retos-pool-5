from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    player = player.lower()
    ai = ai.lower()
    if player == ai:
        return "Empate!"
    elif player == "piedra" and ai == "tijeras":
        return "Ganaste!"
    elif player == "tijeras" and ai == "papel":
        return "Ganaste!"
    elif player == "papel" and ai == "piedra":
        return "Ganaste!"
    else:
        return "Perdiste!"
        

# Entry Point
def Game():
    print("********* Bienvenido a Piedra, Papel y Tijeras *********")
    # 
    # Entrada del usuario
    player = options[int(input("Escoge una opcion 1:Piedra 2:Papel 3:Tijeras ")) - 1]
    
    #
    # Numero aleatorio de la ia
    ai = options[randint(0, 2)]
    winner = quienGana(player, ai)
    print("La IA selecciono " + ai)
    print(winner)