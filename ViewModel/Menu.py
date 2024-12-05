import os
from datetime import datetime
from Model.Book import Book


def show_menu():
    """Zeigt das Hauptmenü an."""
    print("\nBuchverwaltungssystem")
    print("1. Ein Buch hinzufügen")
    print("2. Alle Bücher anzeigen")
    print("3. Ein Buch aktualisieren")
    print("4. Ein Buch löschen")
    print("5. Bücher speichern")
    print("6. Bücher durchsuchen")
    print("7. Statistiken anzeigen")
    print("8. Beenden")


async def handle_choice(choice, book_repository):
    """Behandelt die Auswahlmöglichkeiten des Benutzers."""
    if choice == 1:
        # Buch hinzufügen
        title = input("Buchtitel: ").strip()
        author = input("Buchautor: ").strip()
        year = int(input("Buchjahr: ").strip())
        genre = input("Buchgenre: ").strip()
        book = Book(title, author, year, genre)
        await book_repository.create_book(book)

    elif choice == 2:
        # Alle Bücher anzeigen
        books = await book_repository.get_all_books()
        if books:
            print("Alle Bücher:")
            for book in books:
                print(f"ID: {book[0]}, Titel: {book[1]}, Autor: {book[2]}, Jahr: {book[3]}, Genre: {book[4]}")
        else:
            print("Keine Bücher gefunden.")

    elif choice == 3:
        # Buch aktualisieren
        book_id = int(input("Buch-ID zum Aktualisieren: ").strip())
        title = input("Neuer Titel: ").strip()
        author = input("Neuer Autor: ").strip()
        year = int(input("Neues Jahr: ").strip())
        genre = input("Neues Genre: ").strip()
        updated_book = Book(title, author, year, genre)
        await book_repository.update_book(book_id, updated_book)

    elif choice == 4:
        # Buch löschen
        book_id = int(input("Buch-ID zum Löschen: ").strip())
        await book_repository.delete_book(book_id)

    elif choice == 5:
        # Bücher speichern
        books = await book_repository.get_all_books()
        save_books_to_file(books)

    elif choice == 6:
        # Suchfunktion
        keyword = input("Suchbegriff (Titel, Autor oder Genre): ").strip()
        results = await book_repository.search_books(keyword)
        if results:
            print("Suchergebnisse:")
            for book in results:
                print(f"ID: {book[0]}, Titel: {book[1]}, Autor: {book[2]}, Jahr: {book[3]}, Genre: {book[4]}")
        else:
            print("Keine Bücher gefunden.")

    elif choice == 7:
        # Statistiken anzeigen
        stats = await book_repository.get_statistics()
        print(f"Gesamtanzahl der Bücher: {stats['total_books']}")
        print(f"Ältestes Buch Jahr: {stats['oldest_book_year']}")

    elif choice == 8:
        print("Programm wird beendet.")
        return False  # Beenden

    else:
        print("Ungültige Wahl! Bitte wählen Sie eine gültige Option.")

    return True


def save_books_to_file(books):
    """Speichert die Bücher in einer Datei auf dem Desktop."""
    if not books:
        print("Keine Bücher zum Speichern vorhanden.")
        return

    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "Books")
    os.makedirs(desktop_path, exist_ok=True)
    filename = f"books_{datetime.now().strftime('%Y-%m-%d')}.txt"
    file_path = os.path.join(desktop_path, filename)

    with open(file_path, "w", encoding="utf-8") as file:
        for book in books:
            file.write(f"ID: {book[0]}, Titel: {book[1]}, Autor: {book[2]}, Jahr: {book[3]}, Genre: {book[4]}\n")

    print(f"Bücher wurden erfolgreich in '{file_path}' gespeichert.")
