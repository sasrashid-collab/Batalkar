# Active Device Discovery System v1.3 (A.D.D.S)
# Optimization & Functional Sync Module

import streamlit as st
import time

# LEX-Ω: جێگیرکردنی ناوی "دۆزەرەوەی ئامێری کارا" (V1.3)
st.set_page_config(
    page_title="Active Device Discovery Hub",
    page_icon="📟",
    layout="centered"
)

# بیرگەی ئامێرە دۆزراوەکان
if 'scanned_devices' not in st.session_state:
    st.session_state.scanned_devices = set()

def scan_nearby_devices():
    """پشکنینی ئامێرە چالاکەکان لە دەوروبەر (Active Device Scan)"""
    devices = [
        {"id": "D-POINT-99", "class": "Dynamic"},
        {"id": "D-POINT-04", "class": "Dynamic"},
        {"id": "STATION-X", "class": "Static"}
    ]
    # تەنها ئەو ئامێرانە پیشان دەدات کە هێشتا کاریگەرییان لەسەر دانەنراوە
    return [d for d in devices if d['id'] not in st.session_state.scanned_devices]

def sync_active_device(device_id):
    """جێگیرکردنی پەیوەندی و گەڕانەوەی ئامێر بۆ خاڵی بنەڕەتی"""
    with st.status(f"Analyzing Device {device_id}...", expanded=True):
        time.sleep(1.2)
        # لۆژیکی بێکاریگەرکردنی ئامێر (الردع المرتد)
        st.session_state.scanned_devices.add(device_id)
        return True

# ڕووکاری دۆزەرەوە v1.3
st.title("سیستەمی دۆزەرەوەی ئامێری کارا v1.3")
st.write("ئەم پلاتفۆرمە بۆ دۆزینەوە و شیکردنەوەی ئامێرە چالاکەکان لە دەوروبەر بەکاردێت.")

# لیستی دۆزەرەوە (تەنیشت)
with st.sidebar:
    st.header("دۆزەرەوە (Scanner)")
    active_units = scan_nearby_devices()
    st.write(f"ئامێرە دۆزراوەکان: {len(active_units)}")
    
    for d in active_units:
        # سوور بۆ ئامێرە جوڵاوەکان، سپی بۆ جێگیرەکان
        color = "red" if d['class'] == "Dynamic" else "white"
        st.markdown(f":{color}[REF: {d['id']}]")
    
    if st.button("Reset Scanner"):
        st.session_state.scanned_devices.clear()
        st.rerun()

st.divider()

# جێبەجێکردنی پڕۆسەی جێگیرکردن
device_ref = st.text_input("Enter Device Reference (e.g. D-POINT-99):")

if st.button("Initialize Sync Cycle"):
    if device_ref and any(d['id'] == device_ref for d in active_units):
        if sync_active_device(device_ref):
            st.success(f"Device {device_ref} synchronized and secured.")
            time.sleep(0.5)
            st.rerun() 
    else:
        st.error("Invalid Reference or Device already analyzed.")
