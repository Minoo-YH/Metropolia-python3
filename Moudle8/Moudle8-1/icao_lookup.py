# icao_lookup.py
import mysql.connector
from config import DB_CONFIG

def airport_by_icao(icao: str):
    conn = mysql.connector.connect(**DB_CONFIG)
    try:
        with conn.cursor(dictionary=True) as cur:
            cur.execute("""
                SELECT name, municipality
                FROM airport
                WHERE ident = %s
            """, (icao.strip().upper(),))
            return cur.fetchone()
    finally:
        conn.close()

def main():
    icao = input("کد ICAO را وارد کن (مثلاً EFHK): ").strip()
    row = airport_by_icao(icao)
    if row:
        print(f"{icao.upper()}: {row['name']} — {row['municipality']}")
    else:
        print("برای این کد چیزی پیدا نشد.")

if __name__ == "__main__":
    main()
