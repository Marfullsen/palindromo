def palindromo(word):
    """ Función Palíndromo, 
    se ingresa una cadena de caracteres, 
    devuelve False si no es un palíndromo,
    de lo contrario devuelve la cadena ingresada. """

    # Se inicializa la respuesta.
    res = "no es palíndromo"

    # Se limpia la entrada de espacios, puntos y comas.
    aux = word.replace(" ","").replace(".","").replace(",","")

    # Se cambian todos los caracteres a mayúsculas.
    aux = word.upper()

    # En caso de no tener caracteres válidos devuelve False.
    if aux == "": return False

    # Se analiza si es un palíndromo.
    if isPalindromic(aux):
        res = "es un palíndromo"
    
    # Se responde en panatalla el resultado.
    print(f"{word}",res)

    return res;

def isPalindromic(word):
    if word == word[::-1]:
        return True
    return False

if __name__ == "__main__":
    while True:
       palindromo(input("\n\nIngrese palabra: "))