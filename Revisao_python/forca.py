import random

palavrasseretas = ['batata', 'celular', 'brasil', 'lexeira']

secredo = random.choice(palavrasseretas).lower()
palavradescoberta = []
tentativas = 0
acerto = False

print(secredo)

while not acerto:
    letra = input("Digite uma letra? ").lower()
    tentativas += 1
    
    if letra in secredo:
        for i, l in secredo:
            if l == letra:
                palavradescoberta[i]=letra
                print("Letra descoberta")
            else:
                print("Letra incorreta")

print(f"Parabéns! Você descobriu a palavra '{palavradescoberta}' em {tentativas} tentativas.")





