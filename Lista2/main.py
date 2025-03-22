from zadania import ManagerZadan, ZadaniePriorytetowe, ZadanieRegularne, Zadanie

if __name__ == "__main__":
    manager = ManagerZadan()

    while True:
        print(
            "\n1. Dodaj zadanie\n"
            "2. Usuń zadanie\n"
            "3. Oznacz jako wykonane\n"
            "4. Edytuj zadanie\n"
            "5. Wyświetl zadania\n"
            "6. Wyjście\n"
            "7. Zapisz do pliku\n"
            "8. Wczytaj z pliku")
        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            tytul = input("Tytuł: ").strip()
            opis = input("Opis: ").strip()
            termin = input("Termin (YYYY-MM-DD): ").strip()
            typ = input("Czy to zadanie priorytetowe (p) czy regularne (r)? ").strip()

            if not tytul or not termin:
                print("Tytuł i termin są wymagane!")
                continue

            if typ == "p":
                priorytet = input("Priorytet (1-5): ").strip()
                if priorytet.isdigit() and 1 <= int(priorytet) <= 5:
                    manager.dodaj_zadanie(ZadaniePriorytetowe(tytul, opis, termin, int(priorytet)))
                else:
                    print("Nieprawidłowy priorytet! Wprowadź liczbę od 1 do 5.")
            elif typ == "r":
                powtarzalnosc = input("Powtarzalność (np. co tydzień): ").strip()
                manager.dodaj_zadanie(ZadanieRegularne(tytul, opis, termin, powtarzalnosc))
            else:
                manager.dodaj_zadanie(Zadanie(tytul, opis, termin))


        elif wybor == "2":
            tytul = input("Podaj tytuł zadania do usunięcia: ").strip()
            if tytul in manager:
                manager.usun_zadanie(tytul)
                print(f"Zadanie '{tytul}' zostało usunięte.")
            else:
                print(f"Nie znaleziono zadania o tytule '{tytul}'.")

        elif wybor == "3":
            tytul = input("Podaj tytuł zadania do oznaczenia jako wykonane: ").strip()
            if tytul in manager:
                manager.oznacz_jako_wykonane(tytul)
                print(f"Zadanie '{tytul}' oznaczono jako wykonane.")
            else:
                print(f"Nie znaleziono zadania o tytule '{tytul}'.")

        elif wybor == "4":
            tytul = input("Podaj tytuł zadania do edycji: ").strip()
            if tytul in manager:
                nowy_tytul = input("Nowy tytuł: ").strip()
                nowy_opis = input("Nowy opis: ").strip()
                nowy_termin = input("Nowy termin (YYYY-MM-DD): ").strip()
                if not nowy_tytul or not nowy_termin:
                    print("Nowy tytuł i termin są wymagane!")
                    continue
                manager.edytuj_zadanie(tytul, nowy_tytul, nowy_opis, nowy_termin)
                print(f"Zadanie '{tytul}' zostało zaktualizowane.")
            else:
                print(f"Nie znaleziono zadania o tytule '{tytul}'.")

        elif wybor == "5":
            manager.wyswietl_zadania()

        elif wybor == "6":
            print("Zamykanie programu...")
            break

        elif wybor == "7":
            manager.zapisz_do_pliku()

        elif wybor == "8":
            manager.wczytaj_z_pliku()

        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")
