import time
from datetime import datetime


def czas_wykonania(funkcja):
    """Dekorator mierzący czas wykonania funkcji"""

    def wrapper(*args, **kwargs):
        start = time.time()
        wynik = funkcja(*args, **kwargs)
        end = time.time()
        print(f"Funkcja '{funkcja.__name__}' wykonana w {end - start:.4f} sekundy")
        return wynik

    return wrapper


class Zadanie:
    """Klasa reprezentująca pojedyncze zadanie."""

    def __init__(self, tytul, opis, termin_wykonania):
        """
        Inicjalizuje zadanie.

        :param tytul: Tytuł zadania
        :param opis: Opis zadania
        :param termin_wykonania: Termin wykonania zadania w formacie YYYY-MM-DD
        """
        self.tytul = tytul
        self.opis = opis
        self.termin_wykonania = datetime.strptime(termin_wykonania, "%Y-%m-%d")
        self.wykonane = False

    def oznacz_jako_wykonane(self):
        self.wykonane = True

    def __str__(self):
        status = "Wykonane" if self.wykonane else "Niewykonane"
        return f"{self.tytul} - {self.opis} | Termin: {self.termin_wykonania.date()} | Status: {status}"


class ZadaniePriorytetowe(Zadanie):
    def __init__(self, tytul, opis, termin_wykonania, priorytet):
        super().__init__(tytul, opis, termin_wykonania)
        self.priorytet = priorytet

    def __str__(self):
        return super().__str__() + f" | Priorytet: {self.priorytet}"


class ZadanieRegularne(Zadanie):
    def __init__(self, tytul, opis, termin_wykonania, powtarzalnosc):
        super().__init__(tytul, opis, termin_wykonania)
        self.powtarzalnosc = powtarzalnosc

    def __str__(self):
        return super().__str__() + f" | Powtarzalność: {self.powtarzalnosc}"


class ManagerZadan:
    def __init__(self):
        self.zadania = []

    def dodaj_zadanie(self, zadanie):
        """Dodaje zadanie do listy. Obsługuje zarówno obiekty klasy Zadanie, jak i ich pochodne."""
        if isinstance(zadanie, Zadanie):
            self.zadania.append(zadanie)
        else:
            print("Błąd: Niepoprawny typ zadania!")

    def usun_zadanie(self, tytul):
        self.zadania = [zadanie for zadanie in self.zadania if zadanie.tytul != tytul]

    def oznacz_jako_wykonane(self, tytul):
        for zadanie in self.zadania:
            if zadanie.tytul == tytul:
                zadanie.oznacz_jako_wykonane()
                break

    def edytuj_zadanie(self, tytul, nowy_tytul, nowy_opis, nowy_termin):
        for zadanie in self.zadania:
            if zadanie.tytul == tytul:
                zadanie.tytul = nowy_tytul
                zadanie.opis = nowy_opis
                zadanie.termin_wykonania = datetime.strptime(nowy_termin, "%Y-%m-%d")
                break

    def __contains__(self, tytul):
        return any(zadanie.tytul == tytul for zadanie in self.zadania)

    @czas_wykonania
    def wyswietl_zadania(self):
        for zadanie in sorted(self.zadania, key=lambda z: z.termin_wykonania):
            print(zadanie)

    def zapisz_do_pliku(self, nazwa_pliku="zadania.txt"):
        with open(nazwa_pliku, "w", encoding="utf-8") as plik:
            for zadanie in self.zadania:
                plik.write(f"{zadanie.tytul}|{zadanie.opis}|{zadanie.termin_wykonania.date()}|{zadanie.wykonane}\n")

    @czas_wykonania
    def wczytaj_z_pliku(self, nazwa_pliku="zadania.txt"):
        try:
            with open(nazwa_pliku, "r", encoding="utf-8") as plik:
                for linia in plik:
                    tytul, opis, termin, wykonane = linia.strip().split("|")
                    zadanie = Zadanie(tytul, opis, termin)
                    zadanie.wykonane = wykonane == "True"
                    self.zadania.append(zadanie)
        except FileNotFoundError:
            print("Plik nie istnieje.")
