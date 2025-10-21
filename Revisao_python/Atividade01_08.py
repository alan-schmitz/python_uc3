# E1

compras =['pão', 'leite', 'ovo']
compras.append('queijo')
print(compras)

#E2

numeros =[10, 20, 30, 40, 50]
del numeros [2]
print(numeros[1])

#E3

cores = ["vermelho", "verde", "azul"]
cores[1] = 'amarelo'
print(cores)

#E4

pontocartesiano = (5, 8)
print(f"primeiro elemento e {pontocartesiano[0]}")
print(f"Segundo elemento e {pontocartesiano[1]}")

#5

dados = ("Maria", 25, "Engenharia")
nome, idade, curso = dados
print(f"O Nome e: {nome}")

#6

fichaaluno = {}
fichaaluno["RA"] = "12345"
fichaaluno["Nota"] = 9.5
print(fichaaluno)

#7

configuracao = {"volume": 80, "brilho": 50, "modo": "claro"}
configuracao["brilho"] = 75
print(configuracao) 

#8

usuario = {"username": "dev_python", "email": "dev@exemplo.com"}
print(usuario.get("telefone", "Não informado"))


