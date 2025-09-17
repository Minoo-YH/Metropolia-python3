import mysql.connector
from mysql.connector import Error
import settings
from contextlib import contextmanager

CFG = dict(
    host=settings.HOST,
    port=settings.PORT,
    user=settings.USER,
    password=settings.PASS,
    charset="utf8mb4",
    collation="utf8mb4_unicode_ci",
)

def get_connection(database=settings.DB, autocommit=True):
    return mysql.connector.connect(database=database, autocommit=autocommit, **CFG)

@contextmanager
def db_cursor(*, database=settings.DB, autocommit=True, dictionary=False):
    """با این کانتکست‌منیجر، مدیریت اتصال/کرسر، کمیت/رول‌بک خودکار می‌شه."""
    conn = get_connection(database=database, autocommit=autocommit)
    cur = conn.cursor(dictionary=dictionary)
    try:
        yield cur, conn
        if not autocommit:
            conn.commit()
    except Exception:
        if not autocommit:
            conn.rollback()
        raise
    finally:
        cur.close()
        conn.close()

def bootstrap():
    # دیتابیس و جدول نمونه
    with db_cursor(database=None) as (cur, conn):
        cur.execute("CREATE DATABASE IF NOT EXISTS ihmiset CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
    with db_cursor() as (cur, conn):
        cur.execute("""
        CREATE TABLE IF NOT EXISTS Työntekijä (
            Numero   INT PRIMARY KEY AUTO_INCREMENT,
            Sukunimi VARCHAR(100) NOT NULL,
            Etunimi  VARCHAR(100) NOT NULL,
            Palkka   DECIMAL(10,2) NOT NULL,
            OsastoId INT NULL,
            UNIQUE KEY uq_full_name (Sukunimi, Etunimi),
            INDEX idx_sukunimi (Sukunimi),
            INDEX idx_osasto (OsastoId)
        ) ENGINE=InnoDB;
        """)
