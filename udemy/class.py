class MinhaClasse:
    
    def  __init__(self, att):
        self.meu_atributo = "Olá Mundo"
        self.meu_atributo_2 = att
    
    def meu_metodo(self):
        print(self.meu_atributo)
        print(self.meu_atributo_2)
        
    def meu_metodo_2(self, num, mult):
        return num * mult
    
objeto = MinhaClasse("Karmine")
# result = objeto.meu_metodo_2(3, 2)
# print(result)
# objeto.meu_metodo()
# print(objeto.meu_atributo)
# att = objeto.meu_atributo
# print(att)
objeto.meu_metodo()