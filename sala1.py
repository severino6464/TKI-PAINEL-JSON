from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# Carregar as configurações do arquivo JSON
def carregar_configuracoes():
    with open('config.json', 'r') as config_file:
        config_data = json.load(config_file)
    return config_data

# Salvar as configurações no arquivo JSON
def salvar_configuracoes(nova_configuracao):
    with open('config.json', 'w') as config_file:
        json.dump(nova_configuracao, config_file, indent=4)

@app.route('/')
def index():
    config_data = carregar_configuracoes()
    return render_template('index.html', config_data=config_data)

@app.route('/editar/<campo>', methods=['GET', 'POST'])
def editar(campo):
    config_data = carregar_configuracoes()

    if request.method == 'POST':
        nova_configuracao = dict(config_data)
        nova_configuracao[campo] = request.form[campo]
        salvar_configuracoes(nova_configuracao)
        return redirect('/')
    else:
        valor_atual = config_data.get(campo, '')
        return render_template('editar.html', campo=campo, valor_atual=valor_atual)

if __name__ == '__main__':
    app.run(debug=True)
