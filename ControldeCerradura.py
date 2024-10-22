import sys
# Entradas independientes para la segunda cerradura
A2 = True  # Presencia de llave
B2 = False # Coincidencia de llave
C2 = False # Manija en posición de apertura
msg1=str("UN4 LL4V3 QU3 48R3 CU4LQU13R C4ND4D0 35 UN4 LL4V3 M4357R4, P3R0 CU4ND0 353 C4ND4D0 L0 48R3 CU4LQU13R LL4V3, 53 D353CH4.")

def neg(p:bool)-> bool:
    """ La negacion de una proposicion devuelve el valor de verdad opuesto a p.
    """
    if p:
        return False
    else:
        return True

def y(p:bool, q:bool)-> bool:
    """ Conjunción
            Devuelve True cuando ambas proposiciones son True,
            devuelve False en cualquier otro caso.
    """
    if p:
        return q
    else:
        return False
    
def o(p:bool, q:bool)-> bool:
    """ Disyunción de dos proposiciones:
        Devuelve True cuando al menos una de las proposiciones es True,
        si ambas proposiciones son False, entonces devuelve False.
    """
    if p:
        return True
    else:
        return q

def control_cerradura_1(A, B, C, D):
    AB=y(A,B)
    _C=neg(C)
    _CAB=y(neg(_C),AB)
    DAB_C=y(neg(_C),y(D,AB))
    ABo_CAB=o(AB,_CAB)
    ABo_CABoDAB_C=o(ABo_CAB,DAB_C)
    return ABo_CABoDAB_C, msg1

def control_cerradura_2(A, B, C):
    _B=neg(B)
    _C=neg(C)
    D=y(A,y(_B,_C))
    return D

def controlador(cerradura, A, B, C, D=None):

    if cerradura == 2:
        
        D = control_cerradura_2(A, B, C)
        print(f"Cerradura 2: {D}")
        # Solo pasamos a la cerradura 1 si la cerradura 2 está liberada (D = True)
        if D:
            print("Pasando a la Cerradura 1...")
            # Entradas independientes para la cerradura 1
            A1 = True  # Ejemplo de entrada independiente para A en cerradura 1
            B1 = True  # Ejemplo de entrada independiente para B en cerradura 1
            C1 = False # Ejemplo de entrada independiente para C en cerradura 1
            controlador(1, A1, B1, C1, D)  # Aquí ahora se pasa D como el cuarto argumento opcional
        else:
            print("No se pasa a la Cerradura 1, la Cerradura 2 está bloqueada.")
    elif cerradura == 1:
        # La función recibe D desde la cerradura 2
        D,mgs1 = control_cerradura_1(A, B, C, D)
        print(f"Cerradura 1: {mgs1}")
    else:
        print("Error: Cerradura inválida.")


def main():
    #lista de ejecucion
    controlador(2, A2, B2, C2)
    return 0


if __name__=="__main__":
    sys.exit(main())