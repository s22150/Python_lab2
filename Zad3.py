def choose_option(options):
    print(options[0]+"\n")
    for x in range(1,len(options)):
        print(x , ". " + options[x] + "\n")
    print("odpowiedz: " + options[int(input("Podaj odpowiedz "))])
    print()

print("odpowiedz " + input("Jak masz na imie? "))
print("odpowiedz " + input("Jakie masz nazwisko? " + "\n"))
print()

choose_option(["Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:",
               "oglądanie telewizji/filmów/seriali ",
               "czytanie książek/czasopism",
               "słuchanie muzyki",
               "spotkania z rodziną/przyjaciółmi"])


choose_option(["W jakich okolicznościach czytasz książki najczęściej?",
               "podczas podróży ",
               "w czasie wolnym (po pracy, na urlopie)",
               "podczas pracy/nauki (to ich element)",
               "w ogóle nie czytam"])

choose_option(["Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru??",
               "czytanie mnie relaksuje/odpręża ",
               "fakt, że czytanie jest modne",
               "czytanie to moje hobby",
               "konieczność nauki w związku z wykonywaną pracą/studiami"])


choose_option(["Ile książek czytasz średnio w ciągu roku?",
               "żadnej w całości - jedynie fragmenty",
               "2 lub 3",
               "4-10",
               "powyżej 10"])

choose_option(["Jak często średnio czytasz książki?",
               "codziennie",
               "raz w tygodniu",
               "raz w miesiacu",
               "raz na kilka miesięcy"])