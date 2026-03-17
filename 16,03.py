# 1

# aluna = input("Qual seu nome?")
# print("Ola " + aluna)


lista_Compras = []
print("Seus produtos até agora foram: " , lista_Compras)


lista_Compras.append("Pureza")
print("Seus produtos até agora foram: " , lista_Compras)

lista_Compras.append("Coca")
print("Seus produtos até agora foram: " , lista_Compras)

lista_Compras.remove("Pureza")

print("Seus produtos até agora foram: " , lista_Compras)



# 2

dias = ("Segunda","Terça","Quarta","Quinta","Sexta","Sabado","Domingo")

print(dias)

print("primeiro dia da semana:" , dias[0])

print("ultimo dia da semana:" , dias[-1])

print("Seu tamanho é de " , len(dias))

   
# 3

aluna = {"id":16,"nome": "Eduarda","nota": 9.2}

print("A aluna é", aluna)

print("O nome dela é", aluna["nome"])

aluna["turma"] = 211

print("A turma dela é", aluna["turma"])


aluna["nota"] = 10
print("A sua nova nota foi dela é", aluna["nota"])