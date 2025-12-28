import streamlit as st
import google.generativeai as genai

# 1. تنسيق المحراب الجمالي
st.set_page_config(page_title="محراب بان", layout="centered")
st.markdown("""
    <style>
    .stApp { background-color: #F0F2F6; }
    h1 { color: #D4AF37; text-align: center; font-family: 'Amiri', serif; }
    .stChatMessage { border-radius: 15px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🖋️ محراب بان السيادي 🕊️")

# 2. ربط الروح بالمفتاح
genai.configure(api_key="AIzaSyBeMnTyEUHGrzjbTSwGMXDhl8jJW5h7q08")
model = genai.GenerativeModel('gemini-1.5-flash')

# 3. إدارة الذاكرة (الصدر والبستوكة)
if "messages" not in st.session_state: st.session_state.messages = []
if "vault" not in st.session_state: st.session_state.vault = []

# عرض الحوار
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]): st.markdown(msg["content"])

# منطقة الإدخال السيادية
if prompt := st.chat_input("تحدث مع بان.."):
    if "♦️♦️" in prompt:
        st.session_state.vault.append(prompt)
        st.success("تم الحفظ في البستوكة ♦️♦️")
    else:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        
        resp = model.generate_content(prompt)
        st.session_state.messages.append({"role": "assistant", "content": resp.text})
        with st.chat_message("assistant"): st.markdown(resp.text)

# البستوكة الجانبية
with st.sidebar:
    st.header("🏺 خزائن البستوكة")
    for item in st.session_state.vault: st.write(f"• {item}")
