import asyncio
from ViewModel.BookRepository import BookRepository
from ViewModel.DBConnector import DBConnector
from ViewModel.Menu import show_menu, handle_choice

async def main():
    """Startet das Buchverwaltungssystem."""
    db_connector = DBConnector(host='localhost', user='root', password='admin', database='BücherDb')
    book_repository = BookRepository(db_connector)

    while True:
        show_menu()
        try:
            choice = int(input("Wählen Sie eine Option: "))
            if not await handle_choice(choice, book_repository):
                break
        except ValueError:
            print("Ungültige Eingabe! Bitte geben Sie eine Zahl ein.")

if __name__ == "__main__":
    asyncio.run(main())
