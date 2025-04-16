import time

# Gramática en CNF
# Cada regla se representa como: parte_derecha -> parte_izquierda
# Ejemplo: S -> AB se representa como ('A', 'B'): ['S']
#          S -> a  se representa como ('a',): ['S']
grammar = {
    ('B', 'A'): ['S'],
    ('b',): ['B'],
    ('a',): ['A'],
}

def cyk_parser(word, grammar):
    n = len(word)
    table = [[set() for _ in range(n)] for _ in range(n)]

    # Rellenar la diagonal (reglas unitarias)
    for i, char in enumerate(word):
        for rule, lhs in grammar.items():
            if len(rule) == 1 and rule[0] == char:
                table[i][i].update(lhs)

    # Rellenar la tabla para substrings de longitud > 1
    for l in range(2, n + 1):  # longitud de la subcadena
        for i in range(n - l + 1):
            j = i + l - 1
            for k in range(i, j):
                for B in table[i][k]:
                    for C in table[k + 1][j]:
                        if (B, C) in grammar:
                            table[i][j].update(grammar[(B, C)])

    # Mostrar tabla (opcional)
    print("\nTabla CYK:")
    for row in table:
        print(['{' + ','.join(cell) + '}' for cell in row])

    # Verificar si la palabra puede ser generada por S
    return 'S' in table[0][n - 1]

# Entrada
cadena = input("Introduce una cadena (ej: baaba): ")

start = time.time()
resultado = cyk_parser(cadena, grammar)
end = time.time()

print("\nResultado:", "Cadena aceptada ✅" if resultado else "Cadena rechazada ❌")
print("Tiempo de ejecución CYK: {:.6f} segundos".format(end - start))

