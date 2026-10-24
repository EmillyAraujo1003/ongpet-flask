from flask import Flask, render_template, request

app = Flask(__name__)

animais = [
    {"id": 1, "nome": "Max", "especie": "Cão", "idade": "2 anos", "porte": "Médio", "foto": "https://placedog.net/500/400?id=12", "descricao": "Vacinado e muito brincalhão."},
    {"id": 2, "nome": "Luna", "especie": "Cão", "idade": "1 ano", "porte": "Pequeno", "foto": "https://placedog.net/500/400?id=13", "descricao": "Adora carinho e dá-se bem com gatos."},
    {"id": 3, "nome": "Thor", "especie": "Cão", "idade": "4 anos", "porte": "Grande", "foto": "https://placedog.net/500/400?id=14", "descricao": "Protetor e ótimo para casas com quintal."},
    {"id": 4, "nome": "Mia", "especie": "Gato", "idade": "6 meses", "porte": "Pequeno", "foto": "https://placecats.com/millie/500/400", "descricao": "Gatinha curiosa, já usa a caixa de areia."},
    {"id": 5, "nome": "Bob", "especie": "Cão", "idade": "3 anos", "porte": "Médio", "foto": "https://placedog.net/500/400?id=15", "descricao": "Resgatado recentemente, precisa de amor."},
    {"id": 6, "nome": "Nina", "especie": "Cão", "idade": "2 anos", "porte": "Pequeno", "foto": "https://placedog.net/500/400?id=16", "descricao": "Muito dócil, adora dormir no sofá."},
    {"id": 7, "nome": "Rex", "especie": "Cão", "idade": "5 anos", "porte": "Grande", "foto": "https://placedog.net/500/400?id=17", "descricao": "Cão de guarda reformado, super tranquilo."},
    {"id": 8, "nome": "Simba", "especie": "Gato", "idade": "1 ano", "porte": "Médio", "foto": "https://placecats.com/500/401", "descricao": "Gato brincalhão, caçador de bolinhas."}
]

@app.route('/')
def home():
    filtro = request.args.get('especie')
    if filtro:
        lista_filtrada = [pet for pet in animais if pet['especie'] == filtro]
    else:
        lista_filtrada = animais
    return render_template('index.html', lista_animais=lista_filtrada)

@app.route('/interesse/<int:id_animal>', methods=['GET', 'POST'])
def interesse(id_animal):
    animal_escolhido = next((pet for pet in animais if pet["id"] == id_animal), None)
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        return f"""
        <div style="text-align: center; margin-top: 50px; font-family: Arial;">
            <h1 style="color: green;">Pedido Recebido com Sucesso!</h1>
            <p>Obrigado, <b>{nome}</b>. A equipa entrará em contacto pelo número <b>{telefone}</b> sobre o/a <b>{animal_escolhido['nome']}</b>.</p>
            <a href="/" style="padding: 10px 20px; background: #0d6efd; color: white; text-decoration: none; border-radius: 5px;">Voltar ao Catálogo</a>
        </div>
        """
    return render_template('formulario.html', pet=animal_escolhido)

@app.route('/apadrinhar/<int:id_animal>', methods=['GET', 'POST'])
def apadrinhar(id_animal):
    animal_escolhido = next((pet for pet in animais if pet["id"] == id_animal), None)
    
    if request.method == 'POST':
        nome = request.form['nome']
        doacao = request.form['doacao']
        return f"""
        <div style="text-align: center; margin-top: 50px; font-family: Arial;">
            <h1 style="color: #0dcaf0;">Obrigado por apadrinhar!</h1>
            <p>Olá <b>{nome}</b>, a sua doação de <b>{doacao}</b> fará toda a diferença na vida do/a <b>{animal_escolhido['nome']}</b>.</p>
            <a href="/" style="padding: 10px 20px; background: #0d6efd; color: white; text-decoration: none; border-radius: 5px;">Voltar ao Catálogo</a>
        </div>
        """
        
    return render_template('apadrinhamento.html', pet=animal_escolhido)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')