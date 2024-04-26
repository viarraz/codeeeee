from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Hello, World!</h1> <a href="/random_fact">View a random fact!</a> <h5> play a coin flip game! : <a href="/coinflip">Random coin flip!</a>'

@app.route("/random_fact")
def facts():
    facts_list = [
        "Menurut sebuah penelitian yang dilakukan pada tahun 2018, lebih dari 50% orang berusia 18 hingga 34 tahun menganggap diri mereka ketergantungan pada ponsel pintar mereka.",
        "Jejaring sosial memiliki sisi positif dan negatif, dan kita harus menyadari keduanya saat menggunakan platform ini.",
        "Studi tentang kecanduan teknologi adalah salah satu bidang penelitian ilmiah modern yang paling relevan."
    ]
    return f'<p>{random.choice(facts_list)}</p> <a href="/">Back to Home</a>'

@app.route("/coinflip")
def coin_flip():
    result = "Heads!" if random.randint(0, 1) == 0 else "Tails!"
    return f"<h1>Coin Flipped... It's {result}</h1> <a href='/'>Back to Home</a>"

app.run(debug=True)