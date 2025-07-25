# Telegram bot
This Telegram bot is written in Python using the `telebot` library and provides the user with several useful functions, including calculating the age by year of birth, determining the symbol from the "Eastern Animal Calendar" by year of birth and determining the zodiac sign by date of birth.

## Table of contents
- [Preparation](#preparation)
- [Functions](#functions)
- [Usage](#usage)
- [Code structure](#code-structure)

## Getting started
Follow these instructions to set up and run the Telegram bot on your local computer.

## Preparation
Before you start, make sure that you have the following dependencies:
- Python 3.x
- `telebot` library (install it using `pip install pyTelegramBotAPI`)

## Functions
The bot provides the following commands:
1. `/start`: Getting started with the bot. The bot greets the user by name, if it is specified in the Telegram profile.
2. `/help`: Shows a list of all available commands and their descriptions.
3. `/find_age`: Calculates the user's age based on the year of birth.
4. `/find_animal`: Defines the symbol of the "Eastern Animal Calendar" based on the year of birth.
5. `/find_zodiac`: Determines the user's zodiac sign based on the date of birth.

## Usage
1. Launch the bot using your Telegram Bot API token.
2. Open Telegram and find your bot by its name or click `/start` to start using the bot.
3. Follow the instructions of the bot to calculate the age, determine the symbol from the "Eastern calendar of animals" or determine the zodiac sign.

## Code structure
The code is divided into several functional parts:
- `/start` and `/help`: Handlers that greet the user and show available commands.
- `/find_age`: Asks for the user's birth year, validates input, and calculates age.
- `/find_animal`: Asks for the user's birth year and determines their Eastern calendar animal symbol.
- `/find_zodiac`: Asks for day and month of birth, validates the input, and determines the zodiac sign.
- Utility functions like calculate_age(), calculate_animal(), get_zodiac_by_date() are used for input validation and processing.
