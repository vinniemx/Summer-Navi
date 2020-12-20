def higher(dicio):
    h = 0
    for i in dicio:
        if dicio[i]>h:
            h=dicio[i]
        else:
            continue
    return h

dict = {}
for i in range(5):
    aluno=input("Nome do aluno: ")
    nota=float(input("Nota do aluno: "))
    dict[aluno]=nota
for i in dict:
    if dict[i]==higher(dict):
        print(i, dict[i])
    else:
        continue
