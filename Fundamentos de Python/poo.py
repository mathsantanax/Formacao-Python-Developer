class bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("plim, plim")

    def parar(self):
        print("parou...")

    def andar(self):
        print("bicicleta está em movimento....")



caloi = bicicleta("preta", "caloi", 2024, 600)

caloi.andar()
caloi.parar()
caloi.buzinar()

print(caloi.cor, caloi.modelo, caloi.ano, caloi.valor)