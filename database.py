import sqlite3

def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn

def create_table(conn):
    sql_create_table = """
    CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        room_name TEXT NOT NULL,
        booking_date TEXT NOT NULL,
        status TEXT NOT NULL
    );"""
    conn.execute(sql_create_table)

def add_booking(conn, room_name, booking_date, status):
    sql_insert_booking = """
    INSERT INTO bookings (room_name, booking_date, status)
    VALUES (?, ?, ?);"""
    conn.execute(sql_insert_booking, (room_name, booking_date, status))
    conn.commit()

if __name__ == '__main__':
    conn = create_connection('bookings.db')
    create_table(conn)
    conn.close()
