import mysql.connector
from mysql.connector import Error
import asyncio

class DBConnector:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    async def connect(self):
        """Stellt eine Verbindung zur MySQL-Datenbank her (async)."""
        try:
            loop = asyncio.get_event_loop()
            connection = await loop.run_in_executor(None, lambda: mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            ))
            if connection.is_connected():
                print("Verbindung zur Datenbank erfolgreich")
                return connection
        except Error as e:
            print(f"Fehler bei der Verbindung zur Datenbank: {e}")
            return None
