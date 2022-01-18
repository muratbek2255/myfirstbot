import telebot
from telebot import types


TOKEN = '2107091071:AAFVW-LSFwT2cz2jYvd9fuh2Tx3F1-KZaHk'

bot = telebot.TeleBot(TOKEN)

keyboard = types.ReplyKeyboardMarkup()

serial_url = 'https://www.ts.kg/'
brooklyn_9_9_url = 'https://www.ts.kg/show/brooklyn_nine_nine'
rick_and_morty_url = 'https://www.ts.kg/show/rick_and_morty'
south_park_url = 'https://www.ts.kg/show/south_park'
young_sheldon_url = 'https://www.ts.kg/show/young_sheldon'
the_boys_url = 'https://www.ts.kg/show/the_boys'
vikings_url = 'https://www.ts.kg/show/vikings'
the_witchen_url = 'https://www.ts.kg/show/the_witcher_2019'
flash_url = 'https://www.ts.kg/show/flash'
chernobyl_url = 'https://www.ts.kg/show/chernobyl'
marco_polo_url = 'https://www.ts.kg/show/marco_polo'
genius_url = 'https://www.ts.kg/show/genius'
the_peaky_blinders_url = 'https://www.ts.kg/show/peaky_blinders'
stranger_things_url = 'https://www.ts.kg/show/stranger_things'
the_walking_dead_url = 'https://www.ts.kg/show/the_walking_dead'
american_horror_story_url = 'https://www.ts.kg/show/american_horror_story'
black_mirror_url = 'https://www.ts.kg/show/black_mirror'
breaking_bad_url = 'https://www.ts.kg/show/breaking_bad'
sopranos_url = 'https://www.ts.kg/show/sopranos'
squid_game_url = 'https://www.ts.kg/show/squid_game'
supernatural_url = 'https://www.ts.kg/show/supernatural'
lost_url = 'https://www.ts.kg/show/lost'
the_mandalorian_url = 'https://www.ts.kg/show/the_mandalorian'
attack_on_titan_url = 'https://www.ts.kg/show/shingeki_no_kyojin'
smallville_url = 'https://www.ts.kg/show/smallville'
star_trek_url = 'https://www.ts.kg/show/star_trek'
mythbusters_url = 'https://www.ts.kg/show/mythbusters'
house_md_url = 'https://www.ts.kg/show/house_md'
fringe_url = 'https://www.ts.kg/show/fringe'
friends_url = 'https://www.ts.kg/show/friends'
himym_url = 'https://www.ts.kg/show/himym'
the_big_bang_theory_url = 'https://www.ts.kg/show/tbbt'
the_office_url = 'https://www.ts.kg/show/office'


@bot.message_handler(commands=['website'])
def open_website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("You luck", serial_url))
    bot.send_message(message.chat.id, "Very great genres", parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    global final_message, markup
    get_message_bot = message.text.strip().lower()

    if get_message_bot == "comedy":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        serial1 = types.KeyboardButton("Brooklyn 9-9")
        serial2 = types.KeyboardButton("Rick and Morty")
        serial3 = types.KeyboardButton("South Park")
        serial4 = types.KeyboardButton("Young Sheldon")
        serial5 = types.KeyboardButton("Comeback")
        markup.add(serial1, serial2, serial3, serial4, serial5)
        final_message = 'Choose:'
        bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)
    else:
        if get_message_bot == "brooklyn 9-9":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            final_message = brooklyn_9_9_url

        if get_message_bot == "rick and morty":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            final_message = rick_and_morty_url

        if get_message_bot == "south park":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            final_message = south_park_url

        if get_message_bot == "young sheldon":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            final_message = young_sheldon_url

        if get_message_bot == "comeback":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            genres1 = types.KeyboardButton("Comedy")
            genres2 = types.KeyboardButton("Action")
            genres3 = types.KeyboardButton("History")
            genres4 = types.KeyboardButton("Horror")
            genres5 = types.KeyboardButton("Drama")
            genres6 = types.KeyboardButton("Adventure")
            genres7 = types.KeyboardButton("Science")
            genres8 = types.KeyboardButton("Sitcom")
            markup.add(genres1, genres2, genres3, genres4, genres5, genres6, genres7, genres8)
            final_message = 'OK'

    if get_message_bot == "action":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        serial6 = types.KeyboardButton("The Boys")
        serial7 = types.KeyboardButton("Vikings")
        serial8 = types.KeyboardButton("The Witcher")
        serial9 = types.KeyboardButton("Flash")
        serial10 = types.KeyboardButton("Comeback")
        markup.add(serial6, serial7, serial8, serial9, serial10)
        final_message = 'Choose:'
        bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)
    else:
        if get_message_bot == "the boys":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            final_message = the_boys_url

        if get_message_bot == "vikings":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            final_message = vikings_url

        if get_message_bot == "the witchen":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            final_message = the_witchen_url

        if get_message_bot == "flash":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            final_message = flash_url

        if get_message_bot == "comeback":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            genres1 = types.KeyboardButton("Comedy")
            genres2 = types.KeyboardButton("Action")
            genres3 = types.KeyboardButton("History")
            genres4 = types.KeyboardButton("Horror")
            genres5 = types.KeyboardButton("Drama")
            genres6 = types.KeyboardButton("Adventure")
            genres7 = types.KeyboardButton("Science")
            genres8 = types.KeyboardButton("Sitcom")
            markup.add(genres1, genres2, genres3, genres4, genres5, genres6, genres7, genres8)
            final_message = 'OK'

    if get_message_bot == "history":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        serial11 = types.KeyboardButton("Chernobyl")
        serial12 = types.KeyboardButton("Marco Polo")
        serial13 = types.KeyboardButton("Genius")
        serial14 = types.KeyboardButton("Peaky Blinders")
        serial15 = types.KeyboardButton("Comeback")
        markup.add(serial11, serial12, serial13, serial14, serial15)
        final_message = 'Choose:'
        bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)
    else:
        if get_message_bot == "chernobyl":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            final_message = chernobyl_url

        if get_message_bot == "marco polo":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            final_message = marco_polo_url

        if get_message_bot == "genius":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            final_message = genius_url

        if get_message_bot == "peaky blinders":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            final_message = the_peaky_blinders_url

        if get_message_bot == "comeback":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            genres1 = types.KeyboardButton("Comedy")
            genres2 = types.KeyboardButton("Action")
            genres3 = types.KeyboardButton("History")
            genres4 = types.KeyboardButton("Horror")
            genres5 = types.KeyboardButton("Drama")
            genres6 = types.KeyboardButton("Adventure")
            genres7 = types.KeyboardButton("Science")
            genres8 = types.KeyboardButton("Sitcom")
            markup.add(genres1, genres2, genres3, genres4, genres5, genres6, genres7, genres8)
            final_message = 'OK'

    if get_message_bot == "horror":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        serial16 = types.KeyboardButton("Stranger Things")
        serial17 = types.KeyboardButton("The Walking Dead")
        serial18 = types.KeyboardButton("American horror story")
        serial19 = types.KeyboardButton("Black Mirror")
        serial20 = types.KeyboardButton("Comeback")
        markup.add(serial16, serial17, serial18, serial19, serial20)
        final_message = 'Choose:'
        bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)
    else:
        if get_message_bot == "stranger things":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            final_message = stranger_things_url

        if get_message_bot == "the walking dead":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            final_message = the_walking_dead_url

        if get_message_bot == "american horror story":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            final_message = american_horror_story_url

        if get_message_bot == "black mirror":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            final_message = black_mirror_url

        if get_message_bot == "comeback":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            genres1 = types.KeyboardButton("Comedy")
            genres2 = types.KeyboardButton("Action")
            genres3 = types.KeyboardButton("History")
            genres4 = types.KeyboardButton("Horror")
            genres5 = types.KeyboardButton("Drama")
            genres6 = types.KeyboardButton("Adventure")
            genres7 = types.KeyboardButton("Science")
            genres8 = types.KeyboardButton("Sitcom")
            markup.add(genres1, genres2, genres3, genres4, genres5, genres6, genres7, genres8)
            final_message = 'OK'

    if get_message_bot == "drama":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        serial21 = types.KeyboardButton("Breaking Bad")
        serial22 = types.KeyboardButton("Sopranos")
        serial23 = types.KeyboardButton("Squid game")
        serial24 = types.KeyboardButton("Supernatural")
        serial25 = types.KeyboardButton("Comeback")
        markup.add(serial21, serial22, serial23, serial24, serial25)
        final_message = 'Choose:'
        bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)
    else:
        if get_message_bot == "breaking bad":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            final_message = breaking_bad_url

        if get_message_bot == "sopranos":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            final_message = sopranos_url

        if get_message_bot == "squid game":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            final_message = squid_game_url

        if get_message_bot == "supernatural":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            final_message = supernatural_url

        if get_message_bot == "comeback":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            genres1 = types.KeyboardButton("Comedy")
            genres2 = types.KeyboardButton("Action")
            genres3 = types.KeyboardButton("History")
            genres4 = types.KeyboardButton("Horror")
            genres5 = types.KeyboardButton("Drama")
            genres6 = types.KeyboardButton("Adventure")
            genres7 = types.KeyboardButton("Science")
            genres8 = types.KeyboardButton("Sitcom")
            markup.add(genres1, genres2, genres3, genres4, genres5, genres6, genres7, genres8)
            final_message = 'OK'

    if get_message_bot == "adventure":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        serial26 = types.KeyboardButton("Lost")
        serial27 = types.KeyboardButton("The Mandalorian")
        serial28 = types.KeyboardButton("Attack on Titan")
        serial29 = types.KeyboardButton("Smallville")
        serial30 = types.KeyboardButton("Comeback")
        markup.add(serial26, serial27, serial28, serial29, serial30)
        final_message = 'Choose:'
        bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)
    else:
        if get_message_bot == "lost":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            final_message = lost_url

        if get_message_bot == "the mandalorian":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            final_message = the_mandalorian_url

        if get_message_bot == "attack on titan":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            final_message = attack_on_titan_url

        if get_message_bot == "smallville":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            final_message = smallville_url

        if get_message_bot == "comeback":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            genres1 = types.KeyboardButton("Comedy")
            genres2 = types.KeyboardButton("Action")
            genres3 = types.KeyboardButton("History")
            genres4 = types.KeyboardButton("Horror")
            genres5 = types.KeyboardButton("Drama")
            genres6 = types.KeyboardButton("Adventure")
            genres7 = types.KeyboardButton("Science")
            genres8 = types.KeyboardButton("Sitcom")
            markup.add(genres1, genres2, genres3, genres4, genres5, genres6, genres7, genres8)
            final_message = 'OK'

    if get_message_bot == "science":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        serial26 = types.KeyboardButton("House, M.D")
        serial27 = types.KeyboardButton("Fringe")
        serial28 = types.KeyboardButton("MythBusters")
        serial29 = types.KeyboardButton("Star trek")
        serial30 = types.KeyboardButton("Comeback")
        markup.add(serial26, serial27, serial28, serial29, serial30)
        final_message = 'Choose:'
        bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

    else:
        if get_message_bot == "house, m.d":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            final_message = house_md_url

        if get_message_bot == "fringe":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            final_message = fringe_url

        if get_message_bot == "mythbusters":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            final_message = mythbusters_url

        if get_message_bot == "star trek":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            final_message = star_trek_url

        if get_message_bot == "comeback":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            genres1 = types.KeyboardButton("Comedy")
            genres2 = types.KeyboardButton("Action")
            genres3 = types.KeyboardButton("History")
            genres4 = types.KeyboardButton("Horror")
            genres5 = types.KeyboardButton("Drama")
            genres6 = types.KeyboardButton("Adventure")
            genres7 = types.KeyboardButton("Science")
            genres8 = types.KeyboardButton("Sitcom")
            markup.add(genres1, genres2, genres3, genres4, genres5, genres6, genres7, genres8)
            final_message = 'OK'

    if get_message_bot == "sitcom":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        serial26 = types.KeyboardButton("Friends")
        serial27 = types.KeyboardButton("HIMYM")
        serial28 = types.KeyboardButton("The big bang theory")
        serial29 = types.KeyboardButton("The Office")
        serial30 = types.KeyboardButton("Comeback")
        markup.add(serial26, serial27, serial28, serial29, serial30)
        final_message = 'Choose:'
        bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)
    else:
        if get_message_bot == "friends":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            final_message = fringe_url

        if get_message_bot == "himym":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            final_message = himym_url

        if get_message_bot == "the big bang theory":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            final_message = the_big_bang_theory_url

        if get_message_bot == "the office":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            final_message = the_office_url

        if get_message_bot == "comeback":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            genres1 = types.KeyboardButton("Comedy")
            genres2 = types.KeyboardButton("Action")
            genres3 = types.KeyboardButton("History")
            genres4 = types.KeyboardButton("Horror")
            genres5 = types.KeyboardButton("Drama")
            genres6 = types.KeyboardButton("Adventure")
            genres7 = types.KeyboardButton("Science")
            genres8 = types.KeyboardButton("Sitcom")
            markup.add(genres1, genres2, genres3, genres4, genres5, genres6, genres7, genres8)
            final_message = 'OK'


    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    genres1 = types.KeyboardButton("Comedy")
    genres2 = types.KeyboardButton("Action")
    genres3 = types.KeyboardButton("History")
    genres4 = types.KeyboardButton("Horror")
    genres5 = types.KeyboardButton("Drama")
    genres6 = types.KeyboardButton("Adventure")
    genres7 = types.KeyboardButton("Science")
    genres8 = types.KeyboardButton("Sitcom")
    markup.add(genres1, genres2, genres3, genres4, genres5, genres6, genres7, genres8)
    welcome_text = "Hello,how are you?Please choose your favorite serial!"
    bot.send_message(message.chat.id, welcome_text, parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)
