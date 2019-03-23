# python3, modulos~> chatterbot e telepot

import telepot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# criar bot do telegram com o token
botTelegram = telepot.Bot('793409273:AAEIgTdcBJFutNhHj-mfEft0NHZZjAdyYyw')
# criar bot principal
botThamara = ChatBot('thamara_bot')

# interações entre usuario e bot
conversas = [
    'oi',
    'iae',
    'como vc está?',
    'de boa kkk',
    'blz?',
    'sim e com vc?'
]

# treinar o bot com as conversas
treinar = ListTrainer(botThamara)
treinar.train(conversas)

# pegar mensagens e responder
def receberMensagens(mensagem):
    content_type, chat_type, chat_id = telepot.glance(mensagem)
    print(mensagem)
    print(mensagem['text'])
    if(content_type == 'text'):
        resposta = botThamara.get_response(mensagem['text'])
        botTelegram.sendMessage(chat_id, str(resposta))
        print(resposta)
    


# loop para receber mensages e imprimir na linha de comando 
botTelegram.message_loop(receberMensagens)



# para o bot não parar
while True:
    pass