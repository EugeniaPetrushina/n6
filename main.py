import os
import argparse

na = input("Ведите имя: ")

parser = argparse.ArgumentParser(description="я пытаюсь понять что это")
parser.add_argument("-n", "--name", default=na, help="Имя пользователя")
parser.add_argument("-p", "--place", default=os.getcwd(), help="Расположение")
parser.add_argument("-noQ", "--noQuest", action="store_true", help="Подавление вопросов")
args = parser.parse_args()
with open("text.txt", "w+", encoding="utf16") as f:
    print(f"{args}\n{na}", file=f)
print(f"Привет, {args.name}!")
q = input("Удалить файл с именем? ")
if q !="" and q !="нет" and q !="no":
    os.remove("text.txt")
