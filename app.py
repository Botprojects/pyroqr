
from pyzbar.pyzbar import decode
from PIL import Image
from telebot import TeleBot

bot = telebot.TeleBot('5143393598:AAHCWH-gV_con-vwEmc-QoFkD2oYp08fdnQ')

@bot.message_handler(commands=['start'])
def welcome_message(msg):
    bot.send_message(msg.chat.id,f'Hello {msg.from_user.first_name} this is qrcode generator bot!')

@bot.message_handler(func=lambda m:True)
def generateQr(msg):
    text = msg.text
    qrcode = segno.make(text)
    qrcode.save('qr.png',scale=3)
    with open('qr.png','rb') as qr:
        bot.send_photo(msg.chat.id,qr,reply_to_message_id=msg.message_id)

@bot.message_handler(func=lambda m:True,content_type=['photo'])
def scanqr(msg):
    img = msg.photo
    d = decode(Image.open(img))
    result = d[0].data.decode('ascii')
    text = '/read'
    if text.reply_to_message != None:
        bot.reply_to(msg,result)

bot.infinity_polling()
