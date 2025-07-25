import telebot
from datetime import datetime

TOKEN = 'your_token_here'
bot = telebot.TeleBot(TOKEN)

current_year = datetime.now().year

@bot.message_handler(commands=['start'])
def start(message):
    name = f'Hi, <b>{message.from_user.first_name}</b>!'
    bot.send_message(message.chat.id, name, parse_mode='html')


@bot.message_handler(commands=['help'])
def help_handler(message):
    bot.send_message(message.chat.id, """
<b>/start</b> - Start the bot  
<b>/help</b> - Show all commands  
<b>/find_age</b> - Calculate your age  
<b>/find_animal</b> - Find your Eastern calendar animal  
<b>/find_zodiac</b> - Find your Zodiac sign
""", parse_mode='html')


@bot.message_handler(commands=['find_age'])
def ask_birth_year(message):
    bot.send_message(message.chat.id, "Enter your birth year:")
    bot.register_next_step_handler(message, calculate_age)


def calculate_age(message):
    try:
        birth_year = int(message.text)
        age = current_year - birth_year
        if 0 < age < 150:
            bot.send_message(message.chat.id, f'Your age is <b>{age}</b>', parse_mode='html')
        else:
            bot.send_message(message.chat.id, "Are you a vampire? Please enter a realistic year.")
    except ValueError:
        bot.send_message(message.chat.id, "Please enter a valid number.")


@bot.message_handler(commands=['find_animal'])
def ask_animal_year(message):
    bot.send_message(message.chat.id, "Enter your birth year:")
    bot.register_next_step_handler(message, calculate_animal)


def calculate_animal(message):
    try:
        year = int(message.text)
        animals = [
            'Monkey', 'Rooster', 'Dog', 'Wild boar', 'Rat', 'Bull',
            'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Sheep'
        ]
        index = (year - 2000) % 12
        symbol = animals[index]
        bot.send_message(message.chat.id,
                         f'Your Eastern calendar animal for {year} is <b><i>{symbol}</i></b>',
                         parse_mode='html')
    except ValueError:
        bot.send_message(message.chat.id, "Please enter a valid year.")


@bot.message_handler(commands=['find_zodiac'])
def ask_zodiac_day(message):
    bot.send_message(message.chat.id, "Enter your birth day (1-31):")
    bot.register_next_step_handler(message, get_zodiac_day)


def get_zodiac_day(message):
    try:
        day = int(message.text)
        if 1 <= day <= 31:
            message.chat_data = {'day': day}
            bot.send_message(message.chat.id, "Enter your birth month (1-12):")
            bot.register_next_step_handler(message, get_zodiac_month, day)
        else:
            bot.send_message(message.chat.id, "Please enter a valid day between 1 and 31.")
    except ValueError:
        bot.send_message(message.chat.id, "Please enter a valid number.")


def get_zodiac_month(message, day):
    try:
        month = int(message.text)
        if not (1 <= month <= 12):
            raise ValueError

        zodiac_sign = get_zodiac_by_date(day, month)
        if zodiac_sign:
            bot.send_message(message.chat.id,
                             f'Your Zodiac sign is <b><i>{zodiac_sign}</i></b>',
                             parse_mode='html')
        else:
            bot.send_message(message.chat.id, "Invalid date. Try again.")
    except ValueError:
        bot.send_message(message.chat.id, "Please enter a valid month (1-12).")


def get_zodiac_by_date(day, month):
    zodiac_dates = [
        ((3, 21), (4, 19), 'Aries'),
        ((4, 20), (5, 20), 'Taurus'),
        ((5, 21), (6, 20), 'Gemini'),
        ((6, 21), (7, 22), 'Cancer'),
        ((7, 23), (8, 22), 'Leo'),
        ((8, 23), (9, 22), 'Virgo'),
        ((9, 23), (10, 22), 'Libra'),
        ((10, 23), (11, 21), 'Scorpio'),
        ((11, 22), (12, 21), 'Sagittarius'),
        ((12, 22), (1, 19), 'Capricorn'),
        ((1, 20), (2, 18), 'Aquarius'),
        ((2, 19), (3, 20), 'Pisces')
    ]
    for start, end, sign in zodiac_dates:
        if (month == start[0] and day >= start[1]) or (month == end[0] and day <= end[1]):
            return sign
    return None


bot.polling(none_stop=True)
