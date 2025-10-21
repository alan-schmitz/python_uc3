estoque = {"teclado": 5, "mouse": 10, "monitor": 3}
listadeprodutos=[]

for produto in estoque:
    quantidade = estoque[produto]
    listadeprodutos.append(f"Protuto: {produto}, Quantidade: {str(quantidade)}")

print(listadeprodutos)