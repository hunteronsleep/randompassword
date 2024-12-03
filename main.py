from random import randint, choice, shuffle

password = ""
list_book = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
list_cyfr = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
list_unichar = ["!", "$", "&", "_", "?", "~", "+", "-", "="]
print(
    "пароль должен содержать от 8 до 64 символов\nДолжна быть хотябы 1 заглавная буква\nдолжна быть хотябы одна цыфра\nхотябы 1 спец символ"
)
lenth_password = int(input("Введите какого размера вам нужен пароль: "))
password_ch = ""
password_bo = ""
password_char = ""


def cyfra(password_ch, list_cyfr: list, lenth_password: int) -> str:
    password_ch = ""
    shuffle(list_cyfr)
    kol_chis = randint(3, lenth_password // 2)
    for i in range(kol_chis):
        password_ch += str(choice(list_cyfr))
    return password_ch


def book(password_bo, list_book: list, lenth_password: int) -> str:
    len_cyfra = len(cyfra(password_ch, list_cyfr, lenth_password))
    password_bo = ""
    shuffle(list_book)
    kol_book = randint(4, lenth_password - (len_cyfra + (randint(1, 2))))
    for i in range(kol_book):
        password_bo += str(choice(list_book))
    return password_bo


def unichar(password_char: str, list_unichar: list, lenth_password: int) -> str:
    password_char = ""
    len_book = len(book(password_bo, list_book, lenth_password))
    len_cyfra = len(cyfra(password_ch, list_cyfr, lenth_password))
    shuffle(list_unichar)
    for i in range(lenth_password - (len_book + len_cyfra)):
        password_char += str(choice(list_unichar))
    return password_char


def result(password: str) -> str:
    kol_shaf = randint(0, 100)
    c = cyfra(password_ch, list_cyfr, lenth_password)
    b = book(password_bo, list_book, lenth_password)
    uc = unichar(password_char, list_unichar, lenth_password)
    password = c + b + uc
    password = list(password)
    for i in range(kol_shaf):
        shuffle(password)
    list_password = "".join(password)
    str_password = str(list_password)
    return str_password


def println():
    print("Сколько вариантов паролей хотите получить?")
    dfdfgds = int(input())
    for i in range(dfdfgds):
        passw = result(password)
        print(passw)
    print("все!")


println()
