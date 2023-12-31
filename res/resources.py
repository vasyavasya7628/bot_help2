def text_bot_token() -> str:
    return ""


def text_parse_mode() -> str:
    return "HTML"


def text_tell_about_your_problem() -> str:
    return "Сообщить о неисправности/проблеме (Для специалистов)"


def text_register_for_admins() -> str:
    return "Зарегистрироваться(Для администраторов)"


def text_end_register_for_admins() -> str:
    return "Регистрация завершена!"


def text_choose_button() -> str:
    return "Выберите"


def text_incorrect_text() -> str:
    return "Если вы хотите сообщить о неполадках, следуйте кнопкам в меню"


def text_incorrect_image() -> str:
    return "Этот бот не для того, чтобы отправлять стикеры."


def text_incorrect_gif() -> str:
    return "Этот бот не для того, чтобы отправлять Гиф-файлы."


def text_write_to_it() -> str:
    return "Написать в IT-Отдел."


def text_admin_choose_district() -> str:
    return "Выберите ведомство из списка(Для It специалистов):"


def text_user_choose_district() -> str:
    return "Выберите ведомство из списка(Для специалистов c окно):"


def text_return_to_main_menu() -> str:
    return "Вернуться в главное меню"


def text_admin_login() -> str:
    return "Зарегистрироваться(для it специалистов)"


def text_order_list() -> str:
    return "Список заявок(для it специалистов)"


def text_orders() -> str:
    return "Выберите ведомство в котором вы хотите посмотреть заявки?"


def text_register_complete() -> str:
    return "Регистрация завершена!"


def text_greetings() -> str:
    return ("Здравствуйте, чем я могу вам помочь?\n"
            "Если вы специалист и у вас есть проблема, нажмите кнопку 'Написать в IT-Отдел'.\n")


def text_describe_your_problem() -> str:
    return "Опишите вашу проблему"


def text_message_correct() -> str:
    return "Вы уверены, что описали проблему правильно?"


def text_lower_case() -> str:
    return "_"


def text_order_send() -> str:
    return "Заявка успешно создана! Специалисты свяжутся с вами в ближайшее время."


def get_districts() -> list:
    districts = [
        "Институт Криминалистики",
        "1",
        "Институт Форреста Гампа",
        "2",
        "Клуб Бойцовских Исследований",
        "3",
        "Миля Зеленых Технологий",
        "4",
        "НИИ Престижных Технологий",
        "5",
        "Список Научных Достижений Шиндлера",
        "6",
        "Центр Исследований Побегов из Шоушенка",
        "7",
        "Лаборатория Бегущего по Лезвию",
        "8",
        "Институт Гладиаторских Боев",
        "9",
        "Центр Начальных Исследований",
        "10",
        "Институт Леона",
        "11",
        "Куш Больших Идей",
        "12",
        "Институт Безумного Макса: Дороги Ярости",
        "13",
        "НИИ Темного Рыцаря",
        "14",
        "Институт Матрицы",
        "15",
        "Интерстелларное НИИ",
        "16",
        "Остров Проклятых Исследований",
        "17",
        "Институт Поющих в Терновнике",
        "18",
        "Шестое Чувство НИИ",
        "19",
        "Институт Фарго",
        "20",
        "Титанический Институт",
        "21",
        "Институт Звездных Войн: Эпизод V – Империя Наносит Ответный Удар",
        "22",
        "Институт Парка Юрского Периода",
        "23",
        "Институт по Спасению Рядового Райана",
        "24",
        "Терминатор 2: Институт Судного Дня",
        "25",
        "Институт Однажды в Америке",
        "26",
        "Институт Призрака Оперы",
        "27",
        "Американский Институт Красоты",
        "28",
        "Институт Острова Сокровищ",
        "29",
        "Таксистское НИИ",
        "30",
        "Институт Славных Парней",
        "31",
        "Игровой Институт Престолов",
        "32",
        "Институт Властелина Колец: Возвращение Короля",
        "33",
        "Институт Жизни Прекрасна",
        "34",
        "Заводной Апельсин НИИ",
        "35",
        "Институт Изгоя",
        "36",
        "Институт Семи Самураев",
        "37",
        "Институт Дракулы",
        "38",
        "Институт Безумного Макса",
        "39",
        "Институт Горбатой Горы",
        "40",
        "Институт Кошмара на Улице Вязов",
        "41",
        "Сияние НИИ",
        "42",
        "Один Дома Институт",
        "43"
    ]

    return districts
