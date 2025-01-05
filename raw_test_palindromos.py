from palindromo import palindromo

palindrom = "es un palíndromo"
not_palindrom = "no es palíndromo"

print("Testeando palíndromos...\n")
print("rodador")
assert(palindromo("rodador")==palindrom)
print("\nreconocer")
assert(palindromo("reconocer")==palindrom)
print("\nrotomotor")
assert(palindromo("rotomotor")==palindrom)

print("\n\nTesteando cuando no son palíndromos...\n")
print("roedor")
assert(palindromo("roedor")==not_palindrom)
print("\nconocer")
assert(palindromo("conocer")==not_palindrom)
print("\nservomotor")
assert(palindromo("servomotor")==not_palindrom)

print("\n\nTesteando casos especiales...\n(no debieran dar respuesta)\n")
print("Vacío.")
assert(palindromo("")==False)
print("Espacio en blanco.")
assert(palindromo(" ")==False)
print("coma, espacio, punto.")
assert(palindromo(", .")==False)

print("\n¡Pruebas finalizadas exitosamente!")