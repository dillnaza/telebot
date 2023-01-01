import telebot

bot = telebot.TeleBot('5695792784:AAEPMFRgGwvHnqQpWzeAN_CLYKlL10WiwRk')


@bot.message_handler(commands=['start'])
def start(message):
    name = f'Hi, <b>{message.from_user.first_name}</b>'
    bot.send_message(message.chat.id, name, parse_mode='html')


@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, """
<b>/start</b> -> start bot
<b>/help</b> -> show all commands
<b>/find_age</b> -> enter year that you born to calculate your age
<b>/find_animal</b> -> enter year that you born to know your animal-symbol from "Eastern Animal Calendar" 
<b>/find_zodiac</b> -> enter day and month that you born and know who you are by zodiac sign
""", parse_mode='html')


year = 2003
date = 23
month = 5


@bot.message_handler(commands=['find_age'])
def find_age(message):
    bot.send_message(message.chat.id, "Enter year: ")
    bot.register_next_step_handler(message, get_year_for_age)


@bot.message_handler(commands=['find_animal'])
def find_animal(message):
    bot.send_message(message.chat.id, "Enter year: ")
    bot.register_next_step_handler(message, get_year)


def get_year_for_age(message):
    global year
    year = int(message.text)
    bot.send_message(message.chat.id, f'Your age: {2022 - year}', parse_mode='html')


def get_year(message):
    global year
    year = int(message.text)
    y = 11 - abs(2000 - year) % 11
    match y:
        case 11:
            s = 'Sheep'
        case 10:
            s = 'Horse'
        case 9:
            s = 'Snake'
        case 8:
            s = 'Dragon'
        case 7:
            s = 'Rabbit'
        case 6:
            s = 'Tiger'
        case 5:
            s = 'Bull'
        case 4:
            s = 'Rat'
        case 3:
            s = 'Wild boar'
        case 2:
            s = 'Dog'
        case 1:
            s = 'Rooster'
        case 0:
            s = 'Monkey'

    bot.send_message(message.chat.id,
                     f'{year} years`s animal-symbol from "Eastern Animal Calendar" is <b><i>{s}</i></b>',
                     parse_mode='html')


@bot.message_handler(commands=['find_zodiac'])
def find_zodiac(message):
    s = ''
    bot.send_message(message.chat.id, "Enter your birthday: ")
    bot.register_next_step_handler(message, get_day)


def get_day(message):
    global date
    date = int(message.text)
    bot.send_message(message.chat.id, "Enter the month of birth: ")
    bot.register_next_step_handler(message, get_month)


def get_month(message):
    global month
    month = int(message.text)
    if (21 <= date <= 31 and month == 3) or (month == 4 and 1 <= date <= 19):
        s = 'Aries'
    elif (20 <= date <= 30 and month == 4) or (month == 5 and 1 <= date <= 20):
        s = 'Taurus'
    elif (21 <= date <= 31 and month == 5) or (month == 6 and 1 <= date <= 21):
        s = 'Twins'
    elif (22 <= date <= 30 and month == 6) or (month == 7 and 1 <= date <= 22):
        s = 'Cancer'
    elif (23 <= date <= 31 and month == 7) or (month == 8 and 1 <= date <= 22):
        s = 'Leo'
    elif (23 <= date <= 31 and month == 8) or (month == 9 and 1 <= date <= 22):
        s = 'Maid'
    elif (23 <= date <= 30 and month == 9) or (month == 10 and 1 <= date <= 23):
        s = 'Scales'
    elif (24 <= date <= 31 and month == 10) or (month == 11 and 1 <= date <= 22):
        s = 'Scorpio'
    elif (23 <= date <= 30 and month == 11) or (month == 12 and 1 <= date <= 21):
        s = 'Sagittarius'
    elif (22 <= date <= 31 and month == 12) or (month == 1 and 1 <= date <= 20):
        s = 'Capricorn'
    elif (21 <= date <= 31 and month == 1) or (month == 2 and 1 <= date <= 18):
        s = 'Aquarius'
    elif (19 <= date <= 29 and month == 2) or (month == 3 and 1 <= date <= 20):
        s = 'Fishes'
    bot.send_message(message.chat.id, f'Your zodiac sign is <b><i>{s}</i></b>', parse_mode='html')


bot.polling(none_stop=True)
