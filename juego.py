
import random  

intentos = 3        # numero de intentos totales.
intentos_restantes = 1    # cantidad de intentos restantes.


print("bienvenido al juego de matematicas")

numero = random.randint(1,10)     # llamo un numero random.

if intentos_restantes >= 2:
    print("te quedan 2 intentos")    #<>

elif intentos_restantes >= 1:
    print("te queda 1 intento")

else:
    print("te quedaste sin intentos")

seguir_jugando =  input("¿queres jugar otra ronda?: ")
print(seguir_jugando)


