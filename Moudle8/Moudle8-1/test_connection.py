import mysql.connector

DB_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "12345",   # اگر رمزت چیز دیگری است، همین‌جا عوض کن
    "database": "flightgame",
    "charset": "utf8mb4",
    "use_unicode": True
}

def main():
    conn = mysql.connector.connect(**DB_CONFIG)
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT DATABASE();")
            db = cur.fetchone()[0]
            print("Connected to DB:", db)
            cur.execute("SELECT COUNT(*) FROM airport;")
            cnt = cur.fetchone()[0]
            print("airport rows:", cnt)
    finally:
        conn.close()

if __name__ == "__main__":
    main()
