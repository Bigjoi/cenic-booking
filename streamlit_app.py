pip install streamlit pandas sqlalchemy

import sqlite3

# สร้างฐานข้อมูลและตาราง
conn = sqlite3.connect('booking.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    room TEXT NOT NULL,
    start_time TEXT NOT NULL,
    end_time TEXT NOT NULL,
    status TEXT NOT NULL
)
''')

conn.commit()
conn.close()

import streamlit as st
import pandas as pd
import sqlite3
from datetime import datetime

# เชื่อมต่อกับฐานข้อมูล
def connect_db():
    conn = sqlite3.connect('booking.db')
    return conn

# ฟังก์ชันสำหรับแสดงสถานะการจอง
def show_bookings():
    conn = connect_db()
    df = pd.read_sql_query("SELECT * FROM bookings", conn)
    conn.close()
    return df

# ฟังก์ชันสำหรับบันทึกการจอง
def book_room(name, room, start_time, end_time):
    conn = connect_db()
    c = conn.cursor()
    c.execute('''
    INSERT INTO bookings (name, room, start_time, end_time, status)
    VALUES (?, ?, ?, ?, 'booked')
    ''', (name, room, start_time, end_time))
    conn.commit()
    conn.close()

# ส่วนการแสดงผลใน Streamlit
st.title("ระบบจองห้อง")

# ฟอร์มสำหรับการจองห้อง
st.header("จองห้อง")
with st.form(key='booking_form'):
    name = st.text_input("ชื่อผู้จอง")
    room = st.text_input("ห้อง")
    start_time = st.datetime_input("เวลาเริ่ม")
    end_time = st.datetime_input("เวลาสิ้นสุด")
    submit_button = st.form_submit_button(label='จอง')

    if submit_button:
        book_room(name, room, start_time.isoformat(), end_time.isoformat())
        st.success("จองห้องเรียบร้อยแล้ว!")

# แสดงสถานะการจอง
st.header("สถานะการจองห้อง")
bookings = show_bookings()
if not bookings.empty:
    st.table(bookings)
else:
    st.write("ไม่มีการจองห้องในขณะนี้")

streamlit run app.py
