import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(page_title="Smart-Ops Pro Dashboard", layout="wide")

# Fixed CSS for styling (Error fixed here)
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("🛠️ Smart-Ops Menu")
page = st.sidebar.selectbox("Jump to Section:", ["Dashboard Overview", "AI Prompt Lab", "Task Analytics", "Live Performance Chart"])

# --- SECTION 1: OVERVIEW ---
if page == "Dashboard Overview":
    st.title("🚀 Operational Performance Hub")
    st.write(f"Welcome back, **Kaustubh**! Here is your business activity for today.")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Pending Tasks", "14", "2 New")
    col2.metric("Efficiency", "92%", "+5%")
    col3.metric("AI Requests", "128", "Active")
    col4.metric("Savings (Time)", "40 hrs", "This Month")

    st.image("https://img.freepik.com/free-vector/modern-dashboard-interface-with-infographics_23-2148381501.jpg", caption="Operational Flowchart", use_container_width=True)

# --- SECTION 2: AI PROMPT LAB ---
elif page == "AI Prompt Lab":
    st.title("🤖 AI Response Library")
    st.info("Directly copy these prompts to use in ChatGPT for business tasks.")
    
    job_role = st.selectbox("Select Business Role", ["Operations Manager", "HR Specialist", "Customer Support"])
    
    if job_role == "Operations Manager":
        st.warning("Prompt: 'Analyze this weekly logistics data and find top 3 bottlenecks.'")
    elif job_role == "HR Specialist":
        st.success("Prompt: 'Draft an interview evaluation form for a B.Tech graduate trainee.'")
    elif job_role == "Customer Support":
        st.help("Prompt: 'Reply to a customer complaining about a delayed delivery with a 10% discount offer.'")

# --- SECTION 3: TASK ANALYTICS ---
elif page == "Task Analytics":
    st.title("📊 Team Productivity Data")
    
    data = {
        'Department': ['Sales', 'HR', 'Tech', 'Logistics'],
        'Tasks Completed': [45, 32, 58, 20],
        'Overdue': [2, 0, 5, 8],
        'Efficiency %': [95, 100, 85, 60]
    }
    df = pd.DataFrame(data)
    st.table(df)
    
    st.subheader("Departmental Task Comparison")
    st.bar_chart(df.set_index('Department')['Tasks Completed'])

# --- SECTION 4: LIVE PERFORMANCE CHART ---
elif page == "Live Performance Chart":
    st.title("📈 Live Efficiency Tracking")
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['Team A', 'Team B', 'Team C']
    )
    st.line_chart(chart_data)