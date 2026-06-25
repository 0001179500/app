from flask import Flask, request

app = Flask(__name__)

USUARIO = "hotmotors"
SENHA = "hotmotors2026"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")

        if usuario == USUARIO and senha == SENHA:
            return """
            <h1>Login realizado com sucesso!</h1>
            <p>Bem-vindo ao sistema.</p>
            """
        else:
            return """
            <h1>Login inválido</h1>
            <a href="/">Tentar novamente</a>
            """

    return """
    <html>
    <head>
        <title>Login</title>
    </head>
    <body>
        <h2>Área de Baguga</h2>
        <form method="post">
            <input type="text" name="usuario" placeholder="Usuário" required><br><br>
            <input type="password" name="senha" placeholder="Senha" required><br><br>
            <button type="submit">Entrar</button>
        </form>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
