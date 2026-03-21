# 1. Criação do catálogo de produtos
catalogo = [
    (1, "Coca", 7.50),
    (2, "Pureza", 6.50),
    (3, "Doritos G", 19.0)
]

print("Catálogo Inicial:", catalogo)
print("Tipo:", type(catalogo))

estoque = {}

# 2. Processamento do catálogo
for produto in catalogo:
    id_produto = produto[0]
    nome_produto = produto[1]
    
    qtd = int(input(f"Digite a quantidade inicial para {nome_produto} (ID {id_produto}): "))
    estoque[id_produto] = qtd

print("-" * 20)
print("Estoque Inicial:", estoque)

# 3. Aplicação de desconto
id_busca = int(input("\nDigite o ID do produto para desconto: "))
percentual = float(input("Digite o percentual de desconto (ex: 15 para 15%): "))

for i in range(len(catalogo)):
    if catalogo[i][0] == id_busca:
        id_p, nome_p, preco_antigo = catalogo[i]
        preco_novo = preco_antigo * (1 - percentual / 100)
        
        
        catalogo[i] = (id_p, nome_p, preco_novo)
        
        print(f"Desconto aplicado! {nome_p}: R$ {preco_antigo:.2f} -> R$ {preco_novo:.2f}")
        break
else:
    print("Erro: ID não encontrado no catálogo.")

# 4. Simulação de compra
carrinho = []
print("\n--- Simulação de Compra ---")
id_desejado = int(input("Digite o ID do produto que deseja comprar: "))
qtd_desejada = int(input("Digite a quantidade desejada: "))

if id_desejado in estoque:
    if estoque[id_desejado] >= qtd_desejada:
        # Busca o preço atualizado no catálogo
        preco_unit_atual = 0
        for prod in catalogo:
            if prod[0] == id_desejado:
                preco_unit_atual = prod[2]
                break

        carrinho.append((id_desejado, qtd_desejada, preco_unit_atual))
        estoque[id_desejado] -= qtd_desejada
        print(f" Adicionado ao carrinho!")
    else:
        print(f"Estoque insuficiente! Disponível: {estoque[id_desejado]}")
else:
    print("Produto não existe.")

# 5. Remoção de item do carrinho
print("\n--- Remoção de Item ---")
id_remover = int(input("Digite o ID para remover do carrinho (ou 0 para pular): "))

if id_remover != 0:
    removido = False
    for i in range(len(carrinho)):
        if carrinho[i][0] == id_remover:
            item_removido = carrinho.pop(i)
            estoque[id_remover] += item_removido[1] # Devolve a quantidade
            print(f"♻️ Item {id_remover} removido e devolvido ao estoque.")
            removido = True
            break
    if not removido:
        print("ℹItem não estava no carrinho.")

# 6. Resumo Final e Ordenação
print("\n" + "="*40)
print(f"{'RESUMO DO FECHAMENTO':^40}")
print("="*40)

total_pagar = 0
if not carrinho:
    print("O carrinho está vazio.")
else:
    print(f"{'ID':<5} | {'QTD':<5} | {'PREÇO UNIT.':<12}")
    for id_c, qtd_c, preco_c in carrinho:
        print(f"{id_c:<5} | {qtd_c:<5} | R$ {preco_c:>10.2f}")
        total_pagar += (qtd_c * preco_c)

print("-" * 40)
print(f"TOTAL A PAGAR: R$ {total_pagar:.2f}")
print("-" * 40)

# Ordenação para visualização (por preço, índice 2 da tupla)
catalogo_ordenado = sorted(catalogo, key=lambda p: p[2])

print("\nSugestões (Catálogo ordenado por preço):")
for p_id, p_nome, p_preco in catalogo_ordenado:
    print(f"- {p_nome}: R$ {p_preco:.2f}")