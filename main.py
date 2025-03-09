import streamlit as st
from zoneinfo import ZoneInfo
from datetime import datetime
import timezone  # Make sure this is properly defined

# Streamlit Page Config
st.set_page_config(page_title="World Time Zone", page_icon="🌍", layout="centered")

# Custom CSS for Styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    body {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    .title {
        font-size: 2.5rem;
        font-weight: 700;
        text-align: center;
        background: linear-gradient(45deg, #4F46E5, #EC4899);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2rem;
        animation: fadeIn 1s ease-in;
    }
    
    .time-card {
        background: rgba(255, 255, 255, 0.95);
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
        transition: all 0.3s ease;
        transform: translateY(0);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.3);
    }
    
    .time-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15);
    }
    
    .dropdown-label {
        font-size: 1.1rem;
        font-weight: 500;
        color: #4a5568;
        margin-bottom: 0.5rem;
    }
    
    .footer {
        text-align: center;
        font-size: 0.9rem;
        margin-top: 3rem;
        color: #718096;
        animation: pulse 2s infinite;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    .stMultiSelect [data-baseweb="select"] {
        border-radius: 10px;
        padding: 0.5rem;
        border: 2px solid #e2e8f0;
        transition: all 0.3s ease;
    }
    
    .stMultiSelect [data-baseweb="select"]:hover {
        border-color: #4F46E5;
        box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1);
    }
    
    .time-display {
        font-size: 1.8rem;
        font-weight: 600;
        color: #2d3748;
        margin: 0.5rem 0;
    }
    
    .zone-name {
        font-size: 1.1rem;
        color: #4a5568;
        margin-bottom: 0.5rem;
    }
    
    </style>
    """, unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🌐 Global Time Tracker</div>', unsafe_allow_html=True)

# Dropdown for Time Zone Selection
st.markdown('<div class="dropdown-label">Select Time Zones</div>', unsafe_allow_html=True)
selected_zones = st.multiselect(
    "",
    timezone.selected_time_zones,
    default=["Asia/Karachi", "America/New_York"],
    label_visibility="collapsed"
)

# Display Time for Selected Zones
if selected_zones:
    cols = st.columns(2)
    for idx, zone in enumerate(selected_zones):
        with cols[idx % 2]:
            current_time = datetime.now(ZoneInfo(zone)).strftime("%I:%M %p")
            current_date = datetime.now(ZoneInfo(zone)).strftime("%A, %d %B %Y")
            st.markdown(f"""
                <div class="time-card">
                    <div class="zone-name">📍 {zone}</div>
                    <div class="time-display">{current_time}</div>
                    <div style="color: #718096; font-size: 0.9rem;">{current_date}</div>
                </div>
            """, unsafe_allow_html=True)
else:
    st.markdown("""
        <div style="text-align: center; color: #718096; margin: 2rem 0;">
            Select time zones to begin...
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        🚀 Developed with <span style="animation: pulse 2s infinite;">❤️</span> by Muhammad Shahroz<br>
        <span style="font-size: 0.8rem; color: #a0aec0;">Real-time global time tracking</span>
    </div>
""", unsafe_allow_html=True)