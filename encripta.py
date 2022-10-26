def encriptar_cesar(mensagem, chave):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    codigoEncriptado = ""

    for i in mensagem:
        numLetraEncriptada = (ord(i) - ord('a') + chave) % 26
        codigoEncriptado += alfabeto[numLetraEncriptada]

    return codigoEncriptado
