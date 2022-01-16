#Daníel Þór Bókhald 2020-present

import math

import csv

import sys

class Bokhald():
    def __init__(self,manudur,innkoma,utgjold,hagnadur):
        self.manudur = manudur
        self.innkoma = innkoma
        self.utgjold = utgjold
        self.hagnad = hagnadur

    def hagnadur(self):
        return int(self.innkoma) - int(self.utgjold)

    def __str__(self):
        return self.manudur+self.innkoma+self.utgjold+self.hagnad

def skrifaSkra(skjal,listi):
    with open(skjal, "w+", newline='',encoding="utf-8")as bokhaldSkra:
        skrifari = csv.writer(bokhaldSkra, delimiter=";")
        for x in listi:
            skrifari.writerow((str(x.manudur), str(x.innkoma), str(x.utgjold), str(x.hagnad)))

def lesaSkra(skjal,listi):
    try:
        with open(skjal,"r",newline='',encoding="utf-8")as bokhaldSkra:
            lesari = csv.reader(bokhaldSkra, delimiter=";")
            for rod in lesari:
                manudur = Bokhald(rod[0],rod[1],rod[2],rod[3])
                listi.append(manudur)
    except:
        print("villa", sys.exc_info())

def haldaBokhald(man,talaM,listi,skjal):
    try:
        kveikt = True
        while kveikt == True:
            seinastaFaersla = ""
            print()
            for x in listi:
                if x.manudur == "Seinasta":
                    if x.innkoma == "1" or x.innkoma == 1:
                        seinastaFaersla = "Bætt við innkomu, ",x.utgjold,"kr"
                    elif x.innkoma == "2" or x.innkoma == 2:
                        seinastaFaersla = "Bætt við útgjöld, ",x.utgjold,"kr"
                    elif x.innkoma == "3" or x.innkoma == 3:
                        seinastaFaersla = "Dregið frá innkomu, ",x.utgjold,"kr"
                    elif x.innkoma == "4" or x.innkoma == 4:
                        seinastaFaersla = "Dregið frá útjöldum, ",x.utgjold,"kr"
            print("Seinasta færsla var:")
            for x in seinastaFaersla:
                print(x,end="")
            print()
            print()
            print("1. Bæta við innkomu")
            print("2. Bæta við útgjöld")
            print("3. Skoða mánuð")
            print("4. Leiðrétta innkomu")
            print("5. Leiðrétta útgjöld")
            print("6. Hætta")
            val = int(input("Sláðu inn nr"))
            if val == 1:
                tala = int(input("Sláðu inn töluna sem bætist við innkomu"))
                for x in listi:
                    summa = x.innkoma
                    if x.manudur == man:
                        summa = int(summa) + tala
                        x.innkoma = summa
                    if x.manudur == "Seinasta":
                        x.innkoma = 1
                        x.utgjold = tala
                skrifaSkra(skjal,listi)
            elif val == 2:
                tala = int(input("Sláðu inn töluna sem bætist við útgjöld"))
                for x in listi:
                    summa = x.utgjold
                    if x.manudur == man:
                        summa = int(summa) + tala
                        x.utgjold = summa
                    if x.manudur == "Seinasta":
                        x.innkoma = 2
                        x.utgjold = tala
                skrifaSkra(skjal,listi)
            elif val == 3:
                for x in listi:
                    if x.manudur == man:
                        h = listi[talaM]
                        hagnast = h.hagnadur()
                        print("---",man,"---")
                        print("Innkoma:", x.innkoma)
                        print("Útgjöld:", x.utgjold)
                        print("Hagnaður:", hagnast)
                        print("------------")
                        x.hagnad = hagnast
                skrifaSkra(skjal,listi)
            elif val == 4:
                tala = int(input("Sláðu inn töluna sem á að draga frá innkomu"))
                for x in listi:
                    if x.manudur == man:
                        summa = x.innkoma
                        summa = int(summa) - tala
                        x.innkoma = summa
                    if x.manudur == "Seinasta":
                        x.innkoma = 3
                        x.utgjold = tala
                skrifaSkra(skjal,listi)
            elif val == 5:
                tala = int(input("Sláðu inn töluna sem á að draga frá útgjöld"))
                for x in listi:
                    if x.manudur == man:
                        summa = x.utgjold
                        summa = int(summa) - tala
                        x.utgjold = summa
                    if x.manudur == "Seinasta":
                        x.innkoma = 4
                        x.utgjold = tala
                skrifaSkra(skjal,listi)
            elif val == 6:
                kveikt = False
    except:
        print("Villa kom upp", sys.exc_info())

def uppgjor(ar,listi,skjal):
    kveikt = True
    while kveikt == True:
        print("1. Heildarinnkoma á árinu")
        print("2. Heildarútjöld á árinu")
        print("3. Hagnaður á árinu")
        print("4. Hætta")
        val = int(input("Veldu hvað þú vilt skoða"))
        if val == 1:
            summa = 0
            for x in listi:
                if x.manudur != "Seinasta" and x.manudur != "Uppgjör":
                    summa = summa+int(x.innkoma)
            for x in listi:
                if x.manudur == "Uppgjör":
                    x.innkoma = summa
            skrifaSkra(skjal,listi)
            print()
            print("Heildarinnkoma ársins",ar,"er",summa,"kr")
            print()
        elif val == 2:
            summa = 0
            for x in listi:
                if x.manudur != "Seinasta" and x.manudur != "Uppgjör":
                    summa = summa+int(x.utgjold)
            for x in listi:
                if x.manudur == "Uppgjör":
                    x.utgjold = summa
            skrifaSkra(skjal,listi)
            print()
            print("Heildarútgjöld ársins", ar, "eru", summa, "kr")
            print()
        elif val == 3:
            summa = 0
            for x in listi:
                if x.manudur != "Seinasta" and x.manudur != "Uppgjör":
                    summa = summa + int(x.hagnad)
            for x in listi:
                if x.manudur == "Uppgjör":
                    x.hagnad = summa
            skrifaSkra(skjal,listi)
            print()
            print("Heildarhagnaður ársins",ar,"var",summa,"kr")
            print()
        elif val == 4:
            kveikt = False

bokhald2020 = []
bokhald2021 = []
bokhald2022 = []

lesaSkra("bokhald_2020.csv",bokhald2020)
lesaSkra("bokhald_2021.csv",bokhald2021)
lesaSkra("bokhald_2022.csv",bokhald2022)

on = True
while on == True:
    print("- 2020")
    print("- 2021")
    print("- 2022")
    print("- Hætta (til þess að hætta)")
    val = input("Veldu hvaða ár þú vilt skoða")
    if val == "2020":
        print("1. Janúar")
        print("2. Febrúar")
        print("3. Mars")
        print("4. Apríl")
        print("5. Maí")
        print("6. Júní")
        print("7. Júlí")
        print("8. Ágúst")
        print("9. September")
        print("10. Október")
        print("11. Nóvember")
        print("12. Desember")
        print("13. Uppgjör árs")
        manudur = input("Sláðu inn mánuð eða nr mánaðar")
        if manudur == "1" or manudur == "janúar" or manudur == "Janúar":
            haldaBokhald("Janúar",1,bokhald2020,"bokhald_2020.csv")
        elif manudur == "2" or manudur == "febrúar" or manudur == "Febrúar":
            haldaBokhald("Febrúar",2,bokhald2020,"bokhald_2020.csv")
        elif manudur == "3" or manudur == "mars" or manudur == "Mars":
            haldaBokhald("Mars",3,bokhald2020,"bokhald_2020.csv")
        elif manudur == "4" or manudur == "apríl" or manudur == "Apríl":
            haldaBokhald("Apríl", 4,bokhald2020,"bokhald_2020.csv")
        elif manudur == "5" or manudur == "maí" or manudur == "Maí":
            haldaBokhald("Maí", 5,bokhald2020,"bokhald_2020.csv")
        elif manudur == "6" or manudur == "júní" or manudur == "Júní":
            haldaBokhald("Júní", 6,bokhald2020,"bokhald_2020.csv")
        elif manudur == "7" or manudur == "júlí" or manudur == "Júlí":
            haldaBokhald("Júlí", 7,bokhald2020,"bokhald_2020.csv")
        elif manudur == "8" or manudur == "ágúst" or manudur == "Ágúst":
            haldaBokhald("Ágúst", 8,bokhald2020,"bokhald_2020.csv")
        elif manudur == "9" or manudur == "september" or manudur == "September":
            haldaBokhald("September", 9,bokhald2020,"bokhald_2020.csv")
        elif manudur == "10" or manudur == "október" or manudur == "Október":
            haldaBokhald("Október", 10,bokhald2020,"bokhald_2020.csv")
        elif manudur == "11" or manudur == "nóvember" or manudur == "Nóvember":
            haldaBokhald("Nóvember", 11,bokhald2020,"bokhald_2020.csv")
        elif manudur == "12" or manudur == "desember" or manudur == "Desember":
            haldaBokhald("Desember", 12,bokhald2020,"bokhald_2020.csv")
        elif manudur == "13" or manudur == "uppgjör" or manudur == "Uppgjör":
            uppgjor("2020",bokhald2020,"bokhald_2020.csv")
        else:
            print("Ekki réttur innsláttur, reyndu aftur")
    elif val == "2021":
        print("1. Janúar")
        print("2. Febrúar")
        print("3. Mars")
        print("4. Apríl")
        print("5. Maí")
        print("6. Júní")
        print("7. Júlí")
        print("8. Ágúst")
        print("9. September")
        print("10. Október")
        print("11. Nóvember")
        print("12. Desember")
        print("13. Uppgjör árs")
        manudur = input("Sláðu inn mánuð eða nr mánaðar")
        if manudur == "1" or manudur == "janúar" or manudur == "Janúar":
            haldaBokhald("Janúar", 1,bokhald2021,"bokhald_2021.csv")
        elif manudur == "2" or manudur == "febrúar" or manudur == "Febrúar":
            haldaBokhald("Febrúar", 2,bokhald2021,"bokhald_2021.csv")
        elif manudur == "3" or manudur == "mars" or manudur == "Mars":
            haldaBokhald("Mars", 3,bokhald2021,"bokhald_2021.csv")
        elif manudur == "4" or manudur == "apríl" or manudur == "Apríl":
            haldaBokhald("Apríl", 4,bokhald2021,"bokhald_2021.csv")
        elif manudur == "5" or manudur == "maí" or manudur == "Maí":
            haldaBokhald("Maí", 5,bokhald2021,"bokhald_2021.csv")
        elif manudur == "6" or manudur == "júní" or manudur == "Júní":
            haldaBokhald("Júní", 6,bokhald2021,"bokhald_2021.csv")
        elif manudur == "7" or manudur == "júlí" or manudur == "Júlí":
            haldaBokhald("Júlí", 7,bokhald2021,"bokhald_2021.csv")
        elif manudur == "8" or manudur == "ágúst" or manudur == "Ágúst":
            haldaBokhald("Ágúst", 8,bokhald2021,"bokhald_2021.csv")
        elif manudur == "9" or manudur == "september" or manudur == "September":
            haldaBokhald("September", 9,bokhald2021,"bokhald_2021.csv")
        elif manudur == "10" or manudur == "október" or manudur == "Október":
            haldaBokhald("Október", 10,bokhald2021,"bokhald_2021.csv")
        elif manudur == "11" or manudur == "nóvember" or manudur == "Nóvember":
            haldaBokhald("Nóvember", 11,bokhald2021,"bokhald_2021.csv")
        elif manudur == "12" or manudur == "desember" or manudur == "Desember":
            haldaBokhald("Desember", 12,bokhald2021,"bokhald_2021.csv")
        elif manudur == "13" or manudur == "uppgjör" or manudur == "Uppgjör":
            uppgjor("2021",bokhald2021,"bokhald_2021.csv")
        else:
            print("Ekki réttur innsláttur, reyndu aftur")
    elif val == "2022":
        print("1. Janúar")
        print("2. Febrúar")
        print("3. Mars")
        print("4. Apríl")
        print("5. Maí")
        print("6. Júní")
        print("7. Júlí")
        print("8. Ágúst")
        print("9. September")
        print("10. Október")
        print("11. Nóvember")
        print("12. Desember")
        print("13. Uppgjör árs")
        manudur = input("Sláðu inn mánuð eða nr mánaðar")
        if manudur == "1" or manudur == "janúar" or manudur == "Janúar":
            haldaBokhald("Janúar", 1,bokhald2022,"bokhald_2022.csv")
        elif manudur == "2" or manudur == "febrúar" or manudur == "Febrúar":
            haldaBokhald("Febrúar", 2,bokhald2022,"bokhald_2022.csv")
        elif manudur == "3" or manudur == "mars" or manudur == "Mars":
            haldaBokhald("Mars", 3,bokhald2022,"bokhald_2022.csv")
        elif manudur == "4" or manudur == "apríl" or manudur == "Apríl":
            haldaBokhald("Apríl", 4,bokhald2022,"bokhald_2022.csv")
        elif manudur == "5" or manudur == "maí" or manudur == "Maí":
            haldaBokhald("Maí", 5,bokhald2022,"bokhald_2022.csv")
        elif manudur == "6" or manudur == "júní" or manudur == "Júní":
            haldaBokhald("Júní", 6,bokhald2022,"bokhald_2022.csv")
        elif manudur == "7" or manudur == "júlí" or manudur == "Júlí":
            haldaBokhald("Júlí", 7,bokhald2022,"bokhald_2022.csv")
        elif manudur == "8" or manudur == "ágúst" or manudur == "Ágúst":
            haldaBokhald("Ágúst", 8,bokhald2022,"bokhald_2022.csv")
        elif manudur == "9" or manudur == "september" or manudur == "September":
            haldaBokhald("September", 9,bokhald2022,"bokhald_2022.csv")
        elif manudur == "10" or manudur == "október" or manudur == "Október":
            haldaBokhald("Október", 10,bokhald2022,"bokhald_2022.csv")
        elif manudur == "11" or manudur == "nóvember" or manudur == "Nóvember":
            haldaBokhald("Nóvember", 11,bokhald2022,"bokhald_2022.csv")
        elif manudur == "12" or manudur == "desember" or manudur == "Desember":
            haldaBokhald("Desember", 12,bokhald2022,"bokhald_2022.csv")
        elif manudur == "13" or manudur == "uppgjör" or manudur == "Uppgjör":
            uppgjor("2022",bokhald2022,"bokhald_2022.csv")
        else:
            print("Ekki réttur innsláttur, reyndu aftur")
    elif val == "Hætta" or val == "hætta":
        on = False