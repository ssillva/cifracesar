def cifra(mensagem, dir):
    #variavel com mensagem cifrada
    m = ''
    #Percorre a mensagem e verifica os caracteres
    for c in mensagem:
        #caso mensagem contenha caracteres, armazena o índice do caracter na string
        if c in ALFABETO:
            c_index = ALFABETO.index(c)
            #Dependendo da direção, a mensagem será criptografada (1) ou descriptografada (-1)
            m += ALFABETO[(c_index + (dir * CHAVE)) % len(ALFABETO)]
        else:
            #caso o caractere não esteja no alfabeto, será armazenado sem alteração
            m += c
    return m

def encrypt(mensagem):
    return cifra(mensagem, 1)

def decrypt(mensagem):
    return cifra(mensagem, -1)

def main():
    ALFABETO = 'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ'
    CHAVE = 13
    original = 'a ligeira raposa marrom saltou sobre o cachorro cansado'
    print('  Original:', original)
    cifrada = encrypt(original, 1)
    print('Encriptada:', cifrada)
    plain = decrypt(cifrada, -1)
    print('Decriptada:', plain)
    
if __name__ == '__main__':
    main()
