import mysql.connector
from mysql.connector import Error
import settings

# اتصال ساده (هر بار یک connection نو)
def get_connection(database=settings.DB, autocommit=True):
    return mysql.connector.connect(
        host=settings.HOST,
        port=settings.PORT,
        database=database,
        user=settings.USER,
        password=settings.PASS,
        autocommit=autocommit,
        charset="utf8mb4",
        collation="utf8mb4_unicode_ci"
    )

# ایجاد دیتابیس و جدول نمونه (فقط بار اول لازم است)
def bootstrap():
    # 1) اگر دیتابیس نبود، بساز
    root_conn = mysql.connector.connect(
        host=settings.HOST, port=settings.PORT,
        user=settings.USER, password=settings.PASS, autocommit=True
    )
    cur = root_conn.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS ihmiset CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
    cur.close()
    root_conn.close()

    # 2) جداول داخل دیتابیس
    conn = get_connection(database="ihmiset", autocommit=True)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Työntekijä (
            Numero     INT PRIMARY KEY AUTO_INCREMENT,
            Sukunimi   VARCHAR(100) NOT NULL,
            Etunimi    VARCHAR(100) NOT NULL,
            Palkka     DECIMAL(10,2) NOT NULL,
            UNIQUE KEY uq_full_name (Sukunimi, Etunimi),
            INDEX idx_sukunimi (Sukunimi)
        ) ENGINE=InnoDB;
    """)
    conn.close()

if __name__ == "__main__":
    try:
        bootstrap()
        print("Bootstrap OK")
    except Error as e:
        print("DB error:", e)
