import os
import threading
from sqlalchemy.orm import sessionmaker
from sqlmodel import create_engine

class DatabaseConnectionPool:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(DatabaseConnectionPool, cls).__new__(cls)
                    cls._instance._initialize_pool()
        return cls._instance

    def _initialize_pool(self):
        print("Initializing DB pool")
        self.engine = create_engine(os.getenv('DATABASE_URL', ''))
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def get_session(self):
        return self.SessionLocal()

def get_db():
    db_pool = DatabaseConnectionPool()
    db = db_pool.get_session()
    try:
        yield db
    finally:
        db.close()
