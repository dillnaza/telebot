# Telegram bot

This Telegram bot is written in Python using the `telebot` library and provides the user with several useful functions, including calculating the age by year of birth, determining the symbol from the "Eastern Animal Calendar" by year of birth and determining the zodiac sign by date of birth.

## Table of contents

- [Start of work](#start of work)
- [Preparation](#preparation)
- [Functions](#functions)
- [Usage](#usage)
- [Code structure](#codestructure)
- [Contacts](#contacts)

- gmail: dilnazbaidakhanova@gmail.com
- telegram: @dillnazzza**

## Getting started

Follow these instructions to set up and run the Telegram bot on your local computer.

### Preparation

Before you start, make sure that you have the following dependencies:

- Python 3.x
- 'telebot` library (install it using `pip install pyTelegramBotAPI`)

### Functions

The bot provides the following commands:

1. `/start`: Getting started with the bot. The bot greets the user by name, if it is specified in the Telegram profile.

2. `/help`: Shows a list of all available commands and their descriptions.

3. `/find_age`: Calculates the user's age based on the year of birth.

4. `/find_animal`: Defines the symbol of the "Eastern Animal Calendar" based on the year of birth.

5. `/find_zodiac`: Determines the user's zodiac sign based on the date of birth.

### Usage

1. Launch the bot using your Telegram Bot API token.

2. Open Telegram and find your bot by its name or click `/start` to start using the bot.

3. Follow the instructions of the bot to calculate the age, determine the symbol from the "Eastern calendar of animals" or determine the zodiac sign.

## Code structure

The code is divided into several functional parts:

- `@bot.message_handler(commands=['start'])` and `@bot.message_handler(commands=['help'])`: Command handlers `/start` and `/help`, which output a welcome message and a list of commands, respectively.

- `@bot.message_handler(commands=['find_age'])` and `@bot.message_handler(commands=['find_animal'])`: Command handlers `/find_age` and `/find_animal`, which run processes to calculate the age and determine the symbol of the "Eastern Calendar of Animals".

- `get_year_for_age(message)` and `get_year(message)`: Functions for getting the user's year of birth and performing the corresponding calculations.

- `@bot.message_handler(commands=['find_zodiac'])`, `get_day(message)`, and `get_month(message)`: Handlers of the `/find_zodiac` command and functions for getting the user's date of birth and determining the zodiac sign.

## Contacts

- gmail: dilnazbaidakhanova@gmail.com
- telegram: @dillnazzza**
