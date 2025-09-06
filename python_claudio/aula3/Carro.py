
class Carro:
    #Configuração inicial do Objeto
    def __init__(self, nome, cor, modelo, ano, marca):
        # Definir atributo
        self.nome = nome
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.marca = marca

    def correr(self):
        print("correndo muito ........")

    def frear(self):
        print("freiando .... pastilha esta ruim ....")

    def ligar(self):
        print("ligando o carro ...", self.nome)

passatiCarro = Carro("Passati", "Preto", "V1", "2025", "BMW")
passatiCarro.ligar()
passatiCarro.correr()
passatiCarro.frear()
