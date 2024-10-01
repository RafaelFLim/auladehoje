from flask import Flask, render_template
from artistas import Artista
from detalhes import Detalhes


app = Flask(__name__)


lista_artista = [
Artista(1, "John lennon", "Cantor"),
Artista(2, "Freddy Mercurie", "Cantor"),
Artista(3, "The rock", "Ator"),
Artista(4, "Luisa Sonza", "Cantor"),
Artista(5, "Chico moedas", "influencer"),
Artista(6,"Casimiro", "influencer"),


]

detalhes_lista = [
Detalhes(1, "20", "Salvador", "johnlennon.jpeg"),
Detalhes(2, "34", "Rio de janeiro", "johnlennon.jpeg"),
Detalhes(3, "98", "São paulo", "johnlennon.jpeg"),
Detalhes(4, "34", "Vassouras", "johnlennon.jpeg"),
Detalhes(5, "22", "Barra do pirai", "johnlennon.jpeg"),
Detalhes(6,"134", "Valença", "johnlennon.jpeg"),
]






@app.route('/')
def home():
    return render_template("index.html", lista_artista=lista_artista)

@app.route('/teste')
def teste():
    return render_template('teste.html', lista_artista=lista_artista)


@app.route('/detalhe')
def detalhes():
    return render_template('detalhes.html', lista_artista=lista_artista, detalhes_lista=detalhes_lista)


@app.route("/artista/<int:id>")
def artista(id):
    for artista in lista_artista:
        for detalhe in detalhes_lista:
            if detalhe.get_id() == artista.get_id():
                detalhe_artista = detalhe


        if artista.get_id() == id:
            return render_template("teste", artista=artista, detalhe_artista=detalhe_artista)
        
    return '<h1>Ops! Nenhum artista encontrado!</h1>'


@app.route("/detalhe/<int:id>")
def detalhe(id):
    for detalhe in detalhes_lista:
        if detalhe.get_id() == id:
            return render_template("detalhes.html", detalhe=detalhe )
        
    return "<h1>Ops! Nenhum artista encontrado!</h1>"