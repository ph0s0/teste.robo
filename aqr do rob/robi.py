import time as t
import sys as y

print("OPEN-SYS : Yes/No?")
start=(input("> "))
if start.casefold() not in ["ye","yes","no"]:
    print("WRONG COMMA : Type again [yes/no]")
    start=(input("> "))
elif start.casefold() in ["ye","yes"]:
    print("Loading...")
elif start.casefold() in ["no"]:
    print("end.")