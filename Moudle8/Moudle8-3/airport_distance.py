# airport_distance.py
import mysql.connector
from geopy.distance import geodesic
from config import DB_CONFIG

def coords_for_icao(icao: str):
    conn = mysql.connector.connect(**DB_CONFIG)
    try:
        with conn.cursor(dictionary=True) as cur:
            cur.execute("""
                SELECT latitude_deg AS lat, longitude_deg AS lon, name
                FROM airport
                WHERE ident = %s
            """, (icao.strip().upper(),))
            row = cur.fetchone()
            if row and row["lat"] is not None and row["lon"] is not None:
                return row  # {'lat':..., 'lon':..., 'name':...}
            return None
    finally:
        conn.close()

def main():
        a = input("ICAO اول (مثل EFHK): ").strip()
        b = input("ICAO دوم (مثل EGLL): ").strip()

        A = coords_for_icao(a)
        B = coords_for_icao(b)

        if not A:
            print(f"{a.upper()}: مختصات پیدا نشد.")
            return
        if not B:
            print(f"{b.upper()}: مختصات پیدا نشد.")
            return

        km = geodesic((A['lat'], A['lon']), (B['lat'], B['lon'])).kilometers
        print(f"فاصلهٔ {a.upper()} ({A['name']}) تا {b.upper()} ({B['name']}): {km:.1f} km")

if __name__ == "__main__":
    main()
