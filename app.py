import streamlit as st

# Page Config
st.set_page_config(page_title="Village Grievance Router", page_icon="🏘️", layout="centered")

# Colourful CSS
st.markdown("""
<style>
.main { background-color: #f0f8ff; }
.stTextArea textarea { border: 2px solid #4CAF50; border-radius: 10px; }
.stButton>button { 
    background: linear-gradient(to right, #FF512F, #DD2476); 
    color: white; 
    font-weight: bold;
    border-radius: 20px;
    padding: 10px 25px;
    border: none;
}
h1 { color: #FF512F; text-align: center; }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1>🏘️ Village Grievance Router</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color: #555;'>A smart system to route your village complaints instantly!</p>", unsafe_allow_html=True)

st.markdown("---")

# Input
col1, col2 = st.columns([1,4])
with col1:
    st.markdown("### 📝")
with col2:
    complaint = st.text_area("Enter your complaint here:", placeholder="Ex: water tap not working, street light problem...")

# Button
if st.button("🚀 Submit Complaint"):

    if complaint == "":
        st.warning("⚠️ Please enter a complaint first!")
    else:
        c = complaint.lower()
        if "water" in c or "tap" in c or "pipe" in c:
            dept = "💧 Water Department"
            color = "#2196F3"
            icon = "💧"
        elif "light" in c or "electricity" in c or "power" in c or "current" in c:
            dept = "💡 Electricity Department"
            color = "#FFC107"
            icon = "💡"
        elif "road" in c or "drainage" in c or "street" in c:
            dept = "🚧 Public Works Department"
            color = "#FF5722"
            icon = "🚧"
        elif "school" in c or "teacher" in c:
            dept = "📚 Education Department"
            color = "#9C27B0"
            icon = "📚"
        elif "hospital" in c or "health" in c or "doctor" in c:
            dept = "🏥 Health Department"
            color = "#E91E63"
            icon = "🏥"
        else:
            dept = "🏛️ Village Administration Office"
            color = "#4CAF50"
            icon = "🏛️"
        
        st.markdown(f"""
        <div style="background-color:{color}; padding:20px; border-radius:15px; text-align:center; color:white;">
            <h2>{icon} Routed to: {dept}</h2>
            <p>Your complaint has been successfully forwarded!</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.balloons()
        st.snow()

st.markdown("---")
st.markdown("<p style='text-align:center; color: grey;'>Built with ❤️ by Harshini | Village Project 2026</p>", unsafe_allow_html=True)
