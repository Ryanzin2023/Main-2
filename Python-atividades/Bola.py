class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        return f"Cor: {self.cor}"

    def mostraCircunferencia(self):
        return f"Circunferência: {self.circunferencia} cm"

    def mostraMaterial(self):
        return f"Material: {self.material}"

bola_exemplo = Bola(cor="Azul", circunferencia=30, material="Couro")

print("Informações da bola antes da troca:")
print(bola_exemplo.mostraCor())
print(bola_exemplo.mostraCircunferencia())
print(bola_exemplo.mostraMaterial())
print()

bola_exemplo.trocaCor("Vermelha")

print("Informações da bola depois da troca:")
print(bola_exemplo.mostraCor())
print(bola_exemplo.mostraCircunferencia())
print(bola_exemplo.mostraMaterial())

