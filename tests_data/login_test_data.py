import random
import string

from faker.proxy import Faker

from models.login_data import LoginData

fake = Faker()


def create_valid_password(length=8):
    if not 8 <= length <= 15:
        raise ValueError("Password length suppose to be between 8 and 15 chars")

    password_characters = [random.choice(string.ascii_uppercase),
                           random.choice(string.ascii_lowercase),
                           random.choice(string.digits),
                           random.choice("@$#^&*!"),
                           ]

    allowed_characters = (string.ascii_letters + string.digits + "@$#^&*!")

    password_characters += random.choices(allowed_characters, k = length - 4)

    random.shuffle(password_characters)

    return "".join(password_characters)

VALID_LOGIN_DATA_1 = LoginData(
    "ksadfa@gmail.com",
    "Qwerty@13223")

VALID_LOGIN_DATA = [
    LoginData("ksadfa@gmail.com",
         "Qwerty@13223",),

    LoginData("zavod_slavere@gmail.com",
         "GSHerqw@342",
         )
]

INVALID_EMAIL_DATA = [
    LoginData("", "Test123!"),                  # T1, T2
    LoginData("   ", "Test123!"),               # T2
    LoginData("userexample", "Test123!"),        # T3: нет @
    LoginData("user@@example", "Test123!"),      # T3: два @
    LoginData("@example", "Test123!"),           # T4
    LoginData("user@", "Test123!"),              # T5
    LoginData("пользователь@mail", "Test123!"),  # T6
    LoginData("user@почта", "Test123!"),         # T6
]

INVALID_PASSWORD_DATA = [
    LoginData("user@example", ""),                  # T7, T8
    LoginData("user@example", "        "),          # T8
    LoginData("user@example", "Test1234"),          # T9
    LoginData("user@example", "Test123%"),          # T9
    LoginData("user@example", "Пароль1!"),          # T10
    LoginData("user@example", "test123!"),          # T11
    LoginData("user@example", "TEST123!"),          # T12
    LoginData("user@example", "TestPass!"),         # T13
    LoginData("user@example", "Abcd1@x"),           # T14: 7 символов
    LoginData("user@example", "Abcdefghijkl12@#"),  # T15: 16 символов
]

UNREGISTERED_VALID_LOGIN_DATA = [
    LoginData(fake.unique.email(), create_valid_password())
    for _ in range(5)

]
