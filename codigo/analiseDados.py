nome = input("Digite o nome do Aluno: ")
nota1= float(input("Digite a primeira nota do aluno: "))
nota2= float(input("Digite a segunda nota do aluno: "))
if nota1 >= 7 and nota2 >= 7:
    print(f"{nome} foi aprovado com as notas {nota1} e {nota2}.")
elif nota1 >= 7 or nota2 >= 7:
    print(f"{nome} está em recuperação com as notas {nota1} e {nota2}.")
else:
    print(f"{nome} foi reprovado com as notas {nota1} e {nota2}.")