class ControleRemoto:

    def __init__(self, televisao, comodo):
        self.televisao = televisao
        self.comodo = comodo

    def avancar_canal(self):
        print("Canal adiante")

    def voltar_canal(self):
        print("Canal anterior")

    def escolher_canal(self, canal):
        print(f"Alterado para o canal {canal}")


controle_sala = ControleRemoto("samsung", "sala")
print(controle_sala.comodo)
print(controle_sala.televisao)
controle_sala.avancar_canal()
controle_sala.escolher_canal(12)
