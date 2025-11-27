'''
Enunciado:
Implementa la función 'fibonacci(fibonacci_number)' que contenga el algoritmo
de Fibonacci y reciba como parámetro un valor numérico entero llamado 
'fibonacci_number'  y devuelva el valor de la serie Fibonacci en esa posición.
Asimismo, si el valor no es numérico, o es menor a cero, se debe lanzar 
una excepción ValueError("mensaje"), la cual puede incluir un mensaje que debería 
corresponder con el tipo de error durante la validación.

Parámetros:
- fibonacci_number: Número entero positivo mayor a 0 que representa la
posición en la serie Fibonacci.

Ejemplo:
    Entrada:
    fibonacci(10)

    Salida:
    55

Enunciat:
Implementa la funció 'fibonacci(fibonacci_number)' que contingui l'algorisme
de Fibonacci i rebi com a paràmetre un valor numèric enter anomenat
'fibonacci_number' i torneu el valor de la sèrie Fibonacci en aquesta posició.
Així mateix, si el valor no és numèric, o és menor a zero, cal llançar
una excepció ValueError("missatge"), la qual pot incloure un missatge que hi hauria de
correspondre amb el tipus d'error durant la validació.

Paràmetres:
- fibonacci_number: Nombre enter positiu superior a 0 que representa la
posició a la sèrie Fibonacci.

Exemple:
     Entrada:
     fibonacci(10)

     Sortida:
     55

'''

def fibonacci(fibonacci_number):
    # Write here your code
    # 1. VALIDACIÓN DE ERRORES 
    
    # Comprobar si no es un número entero 
    if not isinstance(fibonacci_number, int):
        # Lanzar la excepción ValueError con un mensaje descriptivo
        raise ValueError("El valor de la posición debe ser un número entero.")
        
    # Comprobar si el número es negativo o cero 
    if fibonacci_number <= 0:
        # Lanzar la excepción ValueError con un mensaje descriptivo
        raise ValueError("La posición de Fibonacci debe ser un número entero positivo mayor a cero.")
        
    # 2. CASOS BASE (F(1) y F(2))
    
    # F(1) es 1
    if fibonacci_number == 1:
        return 1
    
    # F(2) es 1
    if fibonacci_number == 2:
        return 1

    # 3. ALGORITMO ITERATIVO (Para N > 2)
    
    # Inicializar los dos primeros valores de la serie.
    # 'a' representa F(n-2) y 'b' representa F(n-1)
    a = 1
    b = 1
    
    # Usamos un bucle FOR para iterar desde la posición 3 hasta la posición deseada.
    for _ in range(3, fibonacci_number + 1):
        # Calcular el siguiente número de Fibonacci (el nuevo F(n))
        next_fib = a + b
        
        # Actualizar 'a' y 'b' para la siguiente iteración (desplazamiento)
        a = b
        b = next_fib
        
    # El valor final en 'b' es el resultado en la posición 'fibonacci_number'
    return b
    pass

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
print(fibonacci(10))
