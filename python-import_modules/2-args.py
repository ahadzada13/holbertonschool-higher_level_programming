#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # sys.argv[0] skriptin adıdır, onu çıxırıq ki, yalnız arqumentlər qalsın
    argv = sys.argv[1:]
    count = len(argv)

    # Birinci sətir: Arqument sayına görə formatlama
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))

    # İkinci hissə: Arqumentlərin siyahısı (əgər varsa)
    for i in range(count):
        print("{}: {}".format(i + 1, argv[i]))
