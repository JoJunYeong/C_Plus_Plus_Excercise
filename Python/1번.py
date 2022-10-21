
import os
import platform

print(platform.system())

if platform.system() == "Windows":
    os.system("cls")
elif platform.system() == "Darwin":
    os.system("clear")

print(platform.system())