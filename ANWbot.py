import pyowm
import telebot

bot = telebot.TeleBot("805109911:AAFKRfLmIH1WZIecQsGMPfbB9_fSX3KcB0E")
owm = pyowm.OWM('2f4915cb1c4515ef18508375d19c50e6', language="ru")

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Введите город, где хотите узнать погоду:")

@bot.message_handler(content_types=['text'])
def weather(message):
    observation = owm.weather_at_place(message.text)
    w = observation.get_weather()

    temp = round(w.get_temperature('celsius')["temp"])
    
    answer = "В городе " + message.text + " сейчас " + w.get_detailed_status() + "." + "\n"
    answer += "Температура сейчас в районе " + str(temp) + " °C." + '\n'

    if temp < 0:
        answer += "Зубрек - чмо. Никита - хуй, какой не скажу. Саня - хуй соси. Пасейдон - на бутылке от спрайта."
    elif temp < 10:
        answer += "ППЦ как холодно, одевайся как танк!"
    elif temp < 15:
        answer += "Холодно, одевайся потеплее."
    elif temp < 15:
        answer += "Тепло, одевайся майкой и курткой."
    else:
        answer += "Жарко, одевай что угодно."

    bot.send_message(message.chat.id, answer)

bot.polling( none_stop=True )