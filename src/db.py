"""Conexión a la base de datos usando variables de entorno (sin credenciales en el código)."""
import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()


def get_engine():
    url = (
        f"postgresql+psycopg2://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}"
        f"@{os.environ['DB_HOST']}:{os.environ.get('DB_PORT', '5432')}/{os.environ['DB_NAME']}"
    )
    return create_engine(url)


def run_query_file(path: str) -> pd.DataFrame:
    """Ejecuta un archivo .sql y devuelve un DataFrame."""
    with open(path, encoding="utf-8") as f:
        query = f.read()
    return pd.read_sql(query, get_engine())
