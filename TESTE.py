from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    # Pega o valor enviado pelo formulário HTML
    senha_digitada = request.args.get('senha')

    # Se a pessoa acabou de abrir o site (sem parâmetro na URL), mostra o formulário
    if senha_digitada is None:
        return render_template('index.html')

    # Lógica de validação
    if senha_digitada == "12345":
        # Redireciona para a rota oficial do jogo
        return redirect(url_for('game'))
    else:
        # Retorna uma mensagem de erro simples
        return redirect(url_for('erro'))

@app.route('/game')
def game():
    # Esta função agora renderiza a página do jogo corretamente
    return render_template('game.html')

@app.route('/erro')
def erro():
    return render_template('erro.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)