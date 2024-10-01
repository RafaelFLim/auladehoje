class Detalhes:
    def __init__(self, id, idade, proximo_show, imagem):
        self.id = id
        self.idade = idade
        self.proximo_show = proximo_show
        self.imagem = imagem

    def get_id(self):
        return self.id
    
    def get_idade(self):
        return self.idade
    
    def get_proximo_show(self):
        return self.proximo_show
    
    def get_imagem(self):
        return self.imagem