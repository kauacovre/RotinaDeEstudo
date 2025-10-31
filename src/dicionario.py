produto = {
    "tipo": input("Insira o tipo do produto: "),
    "esp": input("Insira as especificações: "),
    "preco": input("Insira o valor do produto: ")
}

print(f"O produto: {produto["tipo"]} {produto["esp"]} \n Valor R${produto["preco"]}")