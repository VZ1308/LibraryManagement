import asyncio

class BookRepository:
    """Verwaltet CRUD-Operationen für Bücher in der Datenbank."""
    def __init__(self, db_connector):
        self.db_connector = db_connector

    async def create_book(self, book):
        """Fügt ein Buch zur Datenbank hinzu."""
        conn = await self.db_connector.connect()
        if conn:
            cursor = conn.cursor()
            await asyncio.get_event_loop().run_in_executor(
                None,
                cursor.execute,
                'INSERT INTO Books (Title, Author, Year, Genre) VALUES (%s, %s, %s, %s)',
                (book.title, book.author, book.year, book.genre)
            )
            conn.commit()
            print(f"Das Buch '{book.title}' wurde hinzugefügt.")
            conn.close()

    async def get_all_books(self):
        """Ruft alle Bücher aus der Datenbank ab."""
        conn = await self.db_connector.connect()
        if conn:
            cursor = conn.cursor()
            await asyncio.get_event_loop().run_in_executor(None, cursor.execute, 'SELECT * FROM Books')
            books = cursor.fetchall()
            conn.close()
            return books
        return []

    async def update_book(self, book_id, updated_book):
        """Aktualisiert ein Buch in der Datenbank."""
        conn = await self.db_connector.connect()
        if conn:
            cursor = conn.cursor()
            await asyncio.get_event_loop().run_in_executor(
                None,
                cursor.execute,
                'UPDATE Books SET Title = %s, Author = %s, Year = %s, Genre = %s WHERE ID = %s',
                (updated_book.title, updated_book.author, updated_book.year, updated_book.genre, book_id)
            )
            conn.commit()
            print(f"Buch mit ID {book_id} wurde aktualisiert.")
            conn.close()

    async def delete_book(self, book_id):
        """Löscht ein Buch aus der Datenbank."""
        conn = await self.db_connector.connect()
        if conn:
            cursor = conn.cursor()
            await asyncio.get_event_loop().run_in_executor(
                None, cursor.execute, 'DELETE FROM Books WHERE ID = %s', (book_id,)
            )
            conn.commit()
            print(f"Buch mit ID {book_id} wurde gelöscht.")
            conn.close()

    async def search_books(self, keyword):
        conn = await self.db_connector.connect()
        if conn:
            cursor = conn.cursor()
            query = """
                SELECT * FROM Books WHERE Title LIKE %s OR Author LIKE %s OR Genre LIKE %s
            """
            keyword = f"%{keyword}%"
            await asyncio.get_event_loop().run_in_executor(
                None, cursor.execute, query, (keyword, keyword, keyword)
            )
            results = cursor.fetchall()
            conn.close()
            return results
        return []

    async def get_statistics(self):
        conn = await self.db_connector.connect()
        if conn:
            cursor = conn.cursor()

            await asyncio.get_event_loop().run_in_executor(None, cursor.execute, "SELECT COUNT(*) FROM Books")
            total_books = cursor.fetchone()[0]

            await asyncio.get_event_loop().run_in_executor(None, cursor.execute, "SELECT MIN(Year) FROM Books")
            oldest_book_year = cursor.fetchone()[0]

            conn.close()
            return {"total_books": total_books, "oldest_book_year": oldest_book_year}