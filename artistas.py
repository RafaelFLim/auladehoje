class Artista:
    def __init__(self, id, nome, genero_musical):
        self.id = id
        self.nome= nome
        self.genero_musical = genero_musical

    def get_id(self):
        return self.id
    
    def get_nome(self):
        return self.nome
    
    def get_genero_musical(self):
        return self.genero_musical
    