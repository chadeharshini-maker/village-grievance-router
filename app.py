import streamlit as st

st.set_page_config(page_title="Village Grievance Router", page_icon="🏘️")

st.title("🏘️ Village Grievance Router")
st.write("A simple system to automatically categorize and route village complaints.")

complaint = st.text_area("Enter your complaint:")

if st.button("Submit Complaint"):
    if complaint == "":
        st.warning("Please enter a complaint.")
    else:
        c = complaint.lower()
        if "water" in c or "tap" in c:
            dept = "Water Department"
        elif "light" in c or "electricity" in c or "power" in c:
            dept = "Electricity Department"
        elif "road" in c or "drainage" in c:
            dept = "Public Works Department"
        elif "school" in c:
            dept = "Education Department"
        elif "hospital" in c or "health" in c:
            dept = "Health Department"
        else:
            dept = "Village Administration Office"
        st.success(f"Routed to: {dept}")
        st.balloons()
