import os
import argparse

parser = argparse.ArgumentParser(description="я пытаюсь понять что это")
parser.add_argument("-n", "--name", default="никто)", help="Имя пользователя")
args = parser.parse_args()
print(args)
print(f"Привет {args.name}")
