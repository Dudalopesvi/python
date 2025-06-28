def main():
    # Coleta dos dados
    nome = input("Digite o nome: ")
    endereco = input("Digite o endereço: ")
    sexo = input("Digite o sexo (M/F): ").upper()
    idade = int(input("Digite a idade: "))
    
    # Verificação da idade
    if idade >= 18:
        status_idade = "maior ou igual a 18 anos"
    else:
        status_idade = "menor que 18 anos"
    
    # Exibição dos resultados
    print("\n--- INFORMAÇÕES DA PESSOA ---")
    print(f"Nome: {nome}")
    print(f"Endereço: {endereco}")
    print(f"Sexo: {sexo}")
    print(f"Status: {status_idade}")

if __name__ == "__main__":
    main()