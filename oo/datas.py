class Data:

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatadata(self):
        print(f"{self.dia}/{self.mes}/{self.ano}")
