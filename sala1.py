import telebot
import time
import datetime
import random
import json

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8"  # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1001974131994'

links = [
    "https://exemplo1.com",
]

# Carregar as configurações do arquivo JSON
with open('config.json', 'r', encoding='latin-1') as config_file:
    config_data = json.load(config_file)

possibilidades_minas = config_data["possibilidades_minas"]
texto4 = config_data["texto4"]
mensagem = config_data["mensagem"]

print("BOT-aff104-nuts")
possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
link_aleatorio = random.choice(links)
validade = datetime.datetime.now() + datetime.timedelta(minutes=5)
hora_validade = validade.strftime("%H:%M")
mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
mensagem_formatada = mensagem_formatada.replace("LINK_PLATAFORMA_CORRETA", link_aleatorio)
mensagem_formatada = mensagem_formatada.replace("LINK_JOGO", link_aleatorio)

bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='Markdown')
time.sleep(5)
