### Programa de control lógico, para habilitar el seguro del pasador de dos cerraduras electromecánicas
**Descripción:**

Se tiene 2 cerraduras las cuales tienen tablas de verdad o condiciones para que estas se puedan desbloquear, la primer cerradura electomecánica tiene CUATRO entradas {A,B,C,D} y una salida {Seguro} pero para que esta se abra, necesitamos  la segunda cerradura pues la segunda cerradura electromecánica tiene: TRES entradas {A,B,C} y una salida {D}, la cual la primer cerradura tomará la salida de la segunda para que esta misma se pueda desbloquear.

**Table of Contents**

[TOCM]

[TOC]

##Desarrollo
Se tiene que cada cerradura tiene:

La primer cerradura electomecánica tiene CUATRO entradas {A,B,C,D} y una salida {Seguro}.
Proposiciones de entrada:

- La entrada (A) activa en ALTO, cuando la cerradura detecta la presencia de la llave en el interior del cilindro de la cerradura.

- La entrada (B) activa en ALTO, indica la COINCIDENCIA de combinaciones mecánicas de la llave y la cerradura electromecánica.  

- La entrada (C) activa en BAJO, indica perilla/manija en posición de apertura.

- La entrada (D) activa en ALTO, indica la validación de liberación del pasador de la  segunda cerradura electrónica.

Predicado de salida: "Libera/bloquea el pasador de la cerradura electromecánica."

La segunda cerradura electromecánica tiene TRES entradas {A,B,C} y una salida {D}.

Parámetros:

- La entrada (A) activa en ALTO, cuando la cerradura detecta la presencia de la llave en el interior del cilindro.

- La entrada (B) activa en BAJO, indica la COINCIDENCIA de combinaciones mecánicas de la llave y la cerradura electromecánica.  

- La entrada (C) activa en BAJO, indica perilla/manija en posición de apertura.	

Por lo que: "Se libera el pasador de la cerradura electromecánica y se asegura el valor de 
verdad en CIERTO para la entrada (D) de la primer cerradura".

----
####Fragmento de código

Utilizaremos la biblioteca `<sys>` 

    import sys
    
----
Variables globales y el mensaje a mostrar en caso de que ambas cerraduras esten abiertas :

    A2 = True  # Presencia de llave
    B2 = False # Coincidencia de llave
    C2 = False # Manija en posición de apertura
    msg1=str("UN4 LL4V3 QU3 48R3 CU4LQU13R C4ND4D0 35 UN4 LL4V3 M4357R4, P3R0 CU4ND0 353 C4ND4D0 L0 48R3 CU4LQU13R LL4V3, 53 D353CH4.")
----
####Python

```javascript
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
```
----
 ####Main

```Main
def main():
    #lista de ejecucion
    controlador(2, A2, B2, C2)
    return 0


if __name__=="__main__":
    sys.exit(main())
```


----

#########Espero que te ayude este programa, gracias por leerme
