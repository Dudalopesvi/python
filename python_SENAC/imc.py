nome = input ("Qual seu nome? ")
peso = float(input ("Qual sua peso? "))
Altura = float(input ("Qual sua Altura? "))

imc =  peso/(Altura ** 2) 
print(f"IMC de {nome}: {imc:.2f} ")

baixo_peso = imc <= 18.5
Normal = (imc <= 18.5) and (imc < 25)
acima_do_peso = (imc <= 25) and (imc < 30)
obesidade = imc >= 30



print("Abaixo do peso? ", baixo_peso)
print("Normal" , Normal)
print("Acima do peso? ", acima_do_peso)
print("Obesidade?  ", obesidade)