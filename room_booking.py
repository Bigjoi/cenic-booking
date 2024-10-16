import streamlit as st
import pandas as pd
from datetime import datetime

# สร้าง DataFrame เพื่อเก็บข้อมูลการจองห้อง
if 'booking_data' not in st.session_state:
    st.session_state.booking_data = pd.DataFrame(columns=["ชื่อผู้จอง", "ชื่อห้อง", "วันที่", "เวลา"])

# ฟังก์ชันสำหรับแสดงสถานะห้อง
def show_booking_status():
    if st.session_state.booking_data.empty:
        st.write("ไม่มีการจองห้องในขณะนี้")
    else:
        st.write("สถานะการจองห้อง:")
        st.dataframe(st.session_state.booking_data)

# UI สำหรับการจองห้อง
st.title("โปรแกรมการจองห้อง")

# ฟอร์มกรอกข้อมูล
with st.form("booking_form"):
    name = st.text_input("ชื่อผู้จอง")
    room = st.selectbox("เลือกชื่อห้อง", ["ห้อง A", "ห้อง B", "ห้อง C"])
    date = st.date_input("วันที่", datetime.now())
    time = st.time_input("เวลา", datetime.now().time())
    
    submit_button = st.form_submit_button("จองห้อง")

# เมื่อกดปุ่ม "จองห้อง"
if submit_button:
    if name and room and date and time:
        new_booking = {
            "ชื่อผู้จอง": name,
            "ชื่อห้อง": room,
            "วันที่": date,
            "เวลา": time
        }
        st.session_state.booking_data = st.session_state.booking_data.append(new_booking, ignore_index=True)
        st.success("จองห้องเรียบร้อยแล้ว")
    else:
        st.error("กรุณากรอกข้อมูลให้ครบถ้วน")

# แสดงสถานะการจองห้อง
show_booking_status()
