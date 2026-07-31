import streamlit as st

#ส่วนที่ 1 หัวข้อหน้าเว็บ (Title สีแดง)
st.markdown("# :red[แอปพิเคชันคำนวนค่าดัชนีมวลกาย BMI]")
st.write("กรอกข้อมูลน้ำหนักและส่วนสูงของคุณ เพื่อเช็กสุขภาพเบื้องต้น")

#ส่วนที่ 2 สร้างช่องรับค่าน้ำหนัก และ ส่วนสูง
wight = st.number_input("กรอกน้ำหนักของคุณ (กิโลกรัม):")
heigh_cm = st.number_input("กรอกส่วนสูงของคุณ (เซนติเมตร):")

#ส่วนที่ 3 สร้างปุ่มกดคำนวน
if st.botton("คำนวนค่า BMI"):
    # แปลงส่วนสูงจาก cm เป็น เมตร แล้วคำนวน BMI
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2) 

    st.write("---")
    st.header(f"ค่า BMI ของคุณคือ: **{bmi}**")
