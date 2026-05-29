import requests
from flask import Flask, render_template, request
from pyswip import Prolog

app = Flask(__name__)

LASTFM_API_KEY = "66fb98de4915671549efaf41c040c508"

prolog = Prolog()
prolog.consult("reglas.pl")

def consultar_prolog(vibra_limpia):
    query_str = f"obtener_genero('{vibra_limpia}', Genero)"
    try:
        resultados = list(prolog.query(query_str))
        return list(set([str(res["Genero"]) for res in resultados]))
    except:
        return []

def consultar_lastfm(genero):
    url = "http://ws.audioscrobbler.com/2.0/"
    params = {
        "method": "tag.gettoptracks",
        "tag": genero,
        "api_key": LASTFM_API_KEY,
        "format": "json",
        "limit": 30,
    }
    r = requests.get(url, params=params)
    data = r.json()
    if "tracks" in data:
        return [{"titulo": t["name"], "artista": t["artist"]["name"]} for t in data["tracks"]["track"]]
    return []

@app.route("/", methods=["GET", "POST"])
def index():
    resultados = []
    vibra_escrita = ""
    if request.method == "POST":
        vibra_escrita = request.form.get("vibra").lower().strip()
        generos = consultar_prolog(vibra_escrita)
        for g in generos:
            resultados.extend(consultar_lastfm(g))
    return render_template("index.html", canciones=resultados, vibra=vibra_escrita)

if __name__ == "__main__":
    app.run(debug=True)