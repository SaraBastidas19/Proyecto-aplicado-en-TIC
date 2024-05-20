from sqlalchemy import create_engine, MetaData
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from sqlalchemy.pool import NullPool
import os

class Session:
    session = None

    def __init__(self):
        load_dotenv()  # Cargar variables de entorno desde el archivo .env
        url = URL.create(
            drivername='postgresql',
            username='postgres',
            password='indeapp',
            host='localhost',
            database='indeapp_db'
        )
        self.session = self._create_session(url)

    def _create_session(self, url):
        engine = create_engine(url, poolclass=NullPool)
        metadata = MetaData()
        metadata.reflect(bind=engine, schema='testRepository')
        session = sessionmaker(bind=engine)
        return session()

    def __del__(self):
        if self.session:
            self.session.close()