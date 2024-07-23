'''Como professor quero informar os dados dos alunos para saber o conceito final da turma.
 • Critério 01 – Dados de Entrada: matrícula e nota de 30 alunos.
 • Critério 02 – Condição: O sistema deve apresentar na tela: Digite a matrícula do Xº aluno. Onde X é o número do aluno. O usuário deve informar a matrícula.
 • Critério 03 – Condição: O sistema deve apresentar na tela: Digite a nota do Xº aluno. Onde X é número do aluno. O usuário deve informar a nota. 
 • Critério 04 – Validação 1: O sistema só pode receber como entrada notas maior ou igual a zero. Caso seja nota negativa mostrar a Mensagem 3. 
 • Critério 05 – Classificação: A turma deve ser classificada conforme a tabela abaixo:
 • Critério 06 – Mensagem 1: “O conceito final da turma é:”, conceito.
 • Critério 07 – Mensagem 2: “A média final da turma é:”, média.
 • Critério 08 – Mensagem 3: “Nota inválida!”'''

notasAluno = []
conceitoFinal = " "
mediaFinal = 0.0


for i in range(1,29):
    while True:
        try:
            matricula = input(f"Digite a matrícula do {i}º aluno: ")
            nota = float(input(f"Digite a nota do {i}º aluno (de 0 a 10): "))
            
            if nota < 0:
                print("Nota inválida! A nota deve ser maior ou igual a zero.")
                continue
            elif nota > 10:
                print("Nota inválida! A nota não pode ser maior que 10.")
                continue
            else:
                break
        
        except ValueError:
            print("Valor inválido! Digite uma nota válida.")

    notasAluno.append(nota)


if len(notasAluno) > 0:
    mediaFinal = sum(notasAluno) / len(notasAluno)


if 0 <= mediaFinal <= 4.9:
    conceitoFinal = 'D'
elif 5 <= mediaFinal <= 6.9:
    conceitoFinal = 'C'
elif 7 <= mediaFinal <= 8.9:
    conceitoFinal = 'B'
elif 9 <= mediaFinal <= 10:
    conceitoFinal = 'A'


print(f"O conceito final da turma é: {conceitoFinal}")
print(f"A média final da turma é: {mediaFinal:.2f}")
