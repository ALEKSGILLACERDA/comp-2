class Cachorro:
  def __init__(self, raca, nome, idade):
    self.raca = raca
    self.nome = nome
    self.idade = idade
  def latir(self):
    print(f'o cachorro {self.nome} da raça {self.raca} com {self.idade} anos de idade latiu')

meu_cachorro = Cachorro("Labrador", "Max", 1)
meu_cachorro2 = Cachorro("Poodle", "Enrico", 14)

meu_cachorro.latir()
meu_cachorro2.latir()