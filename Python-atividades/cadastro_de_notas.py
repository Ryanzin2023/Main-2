class Aluno:

    def __init__(self, nome: str, matricula: int, notas: list):
        self.nome = nome
        self.matricula = matricula
        self.notas = notas

    def calcular_media(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

    def exibir_informacoes(self):
        print(f"Nome do aluno: {self.nome}")
        print(f"Matrícula: {self.matricula}")
        print(f"Notas: {', '.join(map(str, self.notas))}")
        print(f"Média das notas: {self.calcular_media():.2f}")


aluno1 = Aluno("João", 12345, [7.5, 8.0, 6.5, 9.0, 7.0])
aluno2 = Aluno("Maria", 67890, [8.5, 9.0, 7.5, 8.0, 9.5])

aluno1.exibir_informacoes()
print("\n")
aluno2.exibir_informacoes()
