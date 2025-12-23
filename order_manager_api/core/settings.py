
from dataclasses import dataclass, field
import os

@dataclass
class Settings:
    DATABASE_URI: str = f"sqlite:///{os.getenv("SQLITE_FILE_NAME", "database.db")}"