# country_counts.py
import mysql.connector
from config import DB_CONFIG

def counts_by_country(iso_country: str):
    conn = mysql.connector.connect(**DB_CONFIG)
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT type, COUNT(*) AS n
                FROM airport
                WHERE iso_country = %s
                GROUP BY type
                ORDER BY n DESC
            """, (iso_country.strip().upper(),))
            return cur.fetchall()
    finally:
        conn.close()

def main():
    code = input("کد کشور (مثلاً FI): ").strip()
    rows = counts_by_country(code)
    if not rows:
        print("داده‌ای برای این کد کشور پیدا نشد.")
        return
    print(f"تعداد فرودگاه‌های {code.upper()} به تفکیک نوع:")
    for typ, n in rows:
        print(f"- {typ}: {n} تا")

if __name__ == "__main__":
    main()
