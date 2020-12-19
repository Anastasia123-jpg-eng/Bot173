import telebot
import config

# Инициализация бота
bot = telebot.TeleBot('1482360295:AAHWOpLT-bENhqg6wLO0i6IHgJFq45NXNIE')

# Создание клавиатур
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Помоги с поступлением!', 'Расскажи о себе!')
country_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
country_keyboard.row(config.flag_usa + 'США', config.flag_gb + 'Англия', config.flag_ge + 'Германия',
                     config.flag_fr + 'Франция')
language_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
language_keyboard.row('Да', 'Нет')
usa_universities_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
usa_universities_keyboard.row('American University', 'Adelphi University', 'Aubum University')
gb_universities_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
gb_universities_keyboard.row('The University of Sheffield', 'University of Sussex', 'Kingston University London')
ge_universities_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
ge_universities_keyboard.row('University of Jena', 'JUBH', 'Jacobs University')
fr_universities_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
fr_universities_keyboard.row('Universite de Lille', 'Sorbonne Universite', 'University of Bordeaux')
speciality_keyboard = telebot.types.ReplyKeyboardMarkup()
speciality_keyboard.row('Экономика и бизнес', 'Социальные науки', 'Дизайн', 'Техническая специальность', 'Естественные науки')
speciality = ['Экономика и бизнес', 'Социальные науки', 'Дизайн', 'Техническая специальность', 'Естественные науки']


# Создание класса для отслеживания состояний
class Answer:

    def __init__(self):
        self.country = ''
        self.language = False
        self.university = ''
        self.speciality = ''
        self.language_mark = False
        self.cv_mark =False


# Инициализация класса
answer = Answer()


# Функция для подсчета результата
def calculate(answers):
    if answers.language_mark is False and answers.cv_mark is False:
        return 'great'
    elif answers.language_mark is True and answers.cv_mark is False:
        return 'lang'
    elif answers.language_mark is False and answers.cv_mark is True:
        return 'cv'
    else:
        return 'bad'


# Описание действий бота на комнду /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     f'Привет, {message.from_user.username}, я бот который поможет тебе с поступлением!',
                     reply_markup=keyboard1)


# Основная логика общения с пользователем
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'помоги с поступлением!':
        bot.send_message(message.chat.id, 'Выбирай страну :', reply_markup=country_keyboard)

    elif message.text.lower() == config.flag_usa + 'сша':
        answer.country = 'сша'
        bot.send_message(message.chat.id,
                         'У Вас есть диплом на знание языка (TOEFL/IELTS/Duolingotest/Cambridgecertificate)?',
                         reply_markup=language_keyboard)
    elif message.text.lower() == config.flag_gb + 'англия':
        answer.country = 'англия'
        bot.send_message(message.chat.id,
                         'У Вас есть диплом на знание языка (TOEFL/IELTS/Duolingotest/Cambridgecertificate)?',
                         reply_markup=language_keyboard)
    elif message.text.lower() == config.flag_ge + 'германия':
        answer.country = 'германия'
        bot.send_message(message.chat.id, 'У Вас есть диплом на знание языка (TestDAF/TestDSH)?',
                         reply_markup=language_keyboard)
    elif message.text.lower() == config.flag_fr + 'франция':
        answer.country = 'франция'
        bot.send_message(message.chat.id, 'У Вас есть диплом на знание языка (DELF/DALF)?',
                         reply_markup=language_keyboard)

    elif message.text.lower() == 'да' and answer.country == 'сша' and answer.language is False:
        answer.language = True
        bot.send_message(message.chat.id, 'Какой университет вас интересует?', reply_markup=usa_universities_keyboard)
    elif message.text.lower() == 'да' and answer.country == 'англия' and answer.language is False:
        answer.language = True
        bot.send_message(message.chat.id, 'Какой университет вас интересует?', reply_markup=gb_universities_keyboard)
    elif message.text.lower() == 'да' and answer.country == 'германия' and answer.language is False:
        answer.language = True
        bot.send_message(message.chat.id, 'Какой университет вас интересует?', reply_markup=ge_universities_keyboard)
    elif message.text.lower() == 'да' and answer.country == 'франция' and answer.language is False:
        answer.language = True
        bot.send_message(message.chat.id, 'Какой университет вас интересует?', reply_markup=fr_universities_keyboard)
    elif message.text.lower() == 'нет' and answer.country == 'сша' and answer.language is False:
        answer.language = True
        answer.language_mark = True
        bot.send_message(message.chat.id, 'Какой университет вас интересует?', reply_markup=usa_universities_keyboard)
    elif message.text.lower() == 'нет' and answer.country == 'англия' and answer.language is False:
        answer.language = True
        answer.language_mark = True
        bot.send_message(message.chat.id, 'Какой университет вас интересует?', reply_markup=gb_universities_keyboard)
    elif message.text.lower() == 'нет' and answer.country == 'германия' and answer.language is False:
        answer.language = True
        answer.language_mark = True
        bot.send_message(message.chat.id, 'Какой университет вас интересует?', reply_markup=ge_universities_keyboard)
    elif message.text.lower() == 'нет' and answer.country == 'франция' and answer.language is False:
        answer.language = True
        answer.language_mark = True
        bot.send_message(message.chat.id, 'Какой университет вас интересует?', reply_markup=fr_universities_keyboard)

    elif message.text == 'American University':
        answer.university = message.text
        bot.send_message(message.chat.id, 'В каком направлении Вы заинтересованы?', reply_markup=speciality_keyboard)
    elif message.text == 'Adelphi University':
        answer.university = message.text
        bot.send_message(message.chat.id, 'В каком направлении Вы заинтересованы?', reply_markup=speciality_keyboard)
    elif message.text == 'Aubum University':
        answer.university = message.text
        bot.send_message(message.chat.id, 'В каком направлении Вы заинтересованы?', reply_markup=speciality_keyboard)
    elif message.text == 'The University of Sheffield':
        answer.university = message.text
        bot.send_message(message.chat.id, 'В каком направлении Вы заинтересованы?', reply_markup=speciality_keyboard)
    elif message.text == 'University of Sussex':
        answer.university = message.text
        bot.send_message(message.chat.id, 'В каком направлении Вы заинтересованы?', reply_markup=speciality_keyboard)
    elif message.text == 'Kingston University London':
        answer.university = message.text
        bot.send_message(message.chat.id, 'В каком направлении Вы заинтересованы?', reply_markup=speciality_keyboard)
    elif message.text == 'University of Jena':
        answer.university = message.text
        bot.send_message(message.chat.id, 'В каком направлении Вы заинтересованы?', reply_markup=speciality_keyboard)
    elif message.text == 'JUBH':
        answer.university = message.text
        bot.send_message(message.chat.id, 'В каком направлении Вы заинтересованы?', reply_markup=speciality_keyboard)
    elif message.text == 'Jacobs University':
        answer.university = message.text
        bot.send_message(message.chat.id, 'В каком направлении Вы заинтересованы?', reply_markup=speciality_keyboard)
    elif message.text == 'Universite de Lille':
        answer.university = message.text
        bot.send_message(message.chat.id, 'В каком направлении Вы заинтересованы?', reply_markup=speciality_keyboard)
    elif message.text == 'Sorbonne Universite':
        answer.university = message.text
        bot.send_message(message.chat.id, 'В каком направлении Вы заинтересованы?', reply_markup=speciality_keyboard)
    elif message.text == 'University of Bordeaux':
        answer.university = message.text
        bot.send_message(message.chat.id, 'В каком направлении Вы заинтересованы?', reply_markup=speciality_keyboard)

    elif message.text in speciality and answer.university == 'American University':
        answer.speciality = message.text
        bot.send_message(message.chat.id, 'Ваше портфолио содержит GMAT или GRE?', reply_markup=language_keyboard)
    elif message.text in speciality and answer.university == 'Adelphi University':
        answer.speciality = message.text
        bot.send_message(message.chat.id, 'Ваше портфолио содержит GMAT или GRE; Учебные отчеты и справки (язык обучения + англ. яз), с печатью учебного заведения/ либо отправленные учебным заведением; Диплом?', reply_markup=language_keyboard)
    elif message.text in speciality and answer.university == 'Aubum University':
        answer.speciality = message.text
        bot.send_message(message.chat.id, 'Ваше портфолио содержит GMAT или GRE?', reply_markup=language_keyboard)
    elif message.text in speciality and answer.university == 'The University of Sheffield':
        answer.speciality = message.text
        bot.send_message(message.chat.id, 'Ваше портфолио содержит диплом бакалавра из высокорейтингового университета?', reply_markup=language_keyboard)
    elif message.text in speciality and answer.university == 'University of Sussex':
        answer.speciality = message.text
        bot.send_message(message.chat.id, 'Ваше портфолио содержит более низкую степень бакалавра с отличием второго класса (2.2) или выше (включая средний балл не менее 57%)?', reply_markup=language_keyboard)
    elif message.text in speciality and answer.university == 'Kingston University London':
        answer.speciality = message.text
        bot.send_message(message.chat.id, 'Ваше портфолио содержит диплом с отличием (или их эквивалентом) в любой соответствующей дисциплине или профессиональная квалификация, обучение или опыт работы в соответствующей области?', reply_markup=language_keyboard)
    elif message.text in speciality and answer.university == 'University of Jena':
        answer.speciality = message.text
        bot.send_message(message.chat.id, 'Ваше портфолио содержит форму регистрации, CV, мотивационное письмо, аттестат об окончании школы?', reply_markup=language_keyboard)
    elif message.text in speciality and answer.university == 'JUBH':
        answer.speciality = message.text
        bot.send_message(message.chat.id, 'Ваше портфолио содержит CV, копию университетского диплома, копию удостоверения личности, TOEFL/IELTS/Duolingo test/Cambridge certificat?', reply_markup=language_keyboard)
    elif message.text in speciality and answer.university == 'Jacobs University':
        answer.speciality = message.text
        bot.send_message(message.chat.id, 'Ваше портфолио содержит мотивационное письмо, CV, два письма с рекомендациями, диссертация на степень бакалавра, переведенная на английский или немецкий язык, сертификат на степень бакалавра на английском или немецком языке?', reply_markup=language_keyboard)
    elif message.text in speciality and answer.university == 'Universite de Lille':
        answer.speciality = message.text
        bot.send_message(message.chat.id, 'Ваше портфолио содержит копию университетского диплома и мотивационное письмо?', reply_markup=language_keyboard)
    elif message.text in speciality and answer.university == 'Sorbonne Universite':
        answer.speciality = message.text
        bot.send_message(message.chat.id, 'Ваше портфолио содержит копию университетского диплома и мотивационное письмо?', reply_markup=language_keyboard)
    elif message.text in speciality and answer.university == 'University of Bordeaux':
        answer.speciality = message.text
        bot.send_message(message.chat.id, 'Ваше портфолио содержит копию университетского диплома и мотивационное письмо?', reply_markup=language_keyboard)

    elif message.text.lower() == 'да' and answer.speciality != '':
        mark = calculate(answer)
        if mark == 'great':
            bot.send_message(message.chat.id, 'Вы полностью готовы, удачи в поступлении!', reply_markup=keyboard1)
        elif mark == 'lang':
            bot.send_message(message.chat.id, 'Вам стоит обратить внимание на знание языка!', reply_markup=keyboard1)
        elif mark == 'cv':
            bot.send_message(message.chat.id, 'Вам стоит обратить внимание на портфолио!', reply_markup=keyboard1)
        elif mark == 'bad':
            bot.send_message(message.chat.id, 'Вам стоит обратить внимание на знание языка и портфолио!', reply_markup=keyboard1)
        answer.country = ''
        answer.language = False
        answer.university = ''
        answer.speciality = ''
        answer.language_mark = False
        answer.cv_mark = False

    elif message.text.lower() == 'нет' and answer.speciality != '':
        answer.cv_mark = True
        mark = calculate(answer)
        if mark == 'great':
            bot.send_message(message.chat.id, 'Вы полностью готовы, удачи в поступлении!', reply_markup=keyboard1)
        elif mark == 'lang':
            bot.send_message(message.chat.id, 'Вам стоит обратить внимание на знание языка!', reply_markup=keyboard1)
        elif mark == 'cv':
            bot.send_message(message.chat.id, 'Вам стоит обратить внимание на портфолио!', reply_markup=keyboard1)
        elif mark == 'bad':
            bot.send_message(message.chat.id, 'Вам стоит обратить внимание на знание языка и портфолио!', reply_markup=keyboard1)
        answer.country = ''
        answer.language = False
        answer.university = ''
        answer.speciality = ''
        answer.language_mark = False
        answer.cv_mark = False

    elif message.text.lower() == 'расскажи о себе!':
        bot.send_message(message.chat.id, 'Я просто бот!', reply_markup=keyboard1)

    else:
        bot.send_message(message.chat.id, 'Используй кнопки!', reply_markup=keyboard1)


# Запуск бота
bot.polling()
