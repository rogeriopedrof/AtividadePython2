class Eldiano:
    def __init__(self, nome, nascionalidade, titan):
        self.nome = nome
        self.nascionalidade = nascionalidade
        self.titan = titan

    def transformar_em_titan(self):
        if self.titan:
            print(f"{self.nome} agora é um titã!")
        else:
            print(f"{self.nome} não possue o poder de se transformar em titã.")

    def regenerar(self):
        if self.titan:
            print(f"{self.nome} está se regenerando!")
        else:
            print(f"{self.nome} não pode regenerar, pois não é um titã.")
                   
    def endurecer(self):
        if self.titan:
            print(f"{self.nome} está usando o poder de endurecimento!")
        else:
            print(f"{self.nome} não pode usar o poder de endurecimento, pois não é um titã.")
