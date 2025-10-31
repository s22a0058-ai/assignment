import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE SETUP ---
st.set_page_config(page_title="Academic Performance Dashboard", layout="wide")

# --- LOAD DATA ---
# Replace with your actual CSV
@st.cache_data
def load_data():
    # Example placeholder (replace with your actual data file)
    df = pd.read_csv("ResearchInformation3_cleaned.csv")
    return df

df = load_data()

# --- PAGE HEADER ---
st.title("🎓 Academic Performance Visualization Dashboard")
st.markdown("An interactive dashboard exploring academic, behavioral, and lifestyle factors affecting student performance.")
st.divider()

# ==============================
# SECTION 1: CORE PERFORMANCE
# ==============================
st.header("📊 Core Performance Metrics")
col1, col2 = st.columns(2)

# 1. Average Overall Score by Department
with col1:
    fig1 = px.bar(df, x="Department", y="Overall", color="Department",
                  title="Average Overall Score by Department",
                  color_discrete_sequence=px.colors.qualitative.Set2)
    fig1.update_layout(height=400)
    st.plotly_chart(fig1, use_container_width=True)

# 2. CGPA by Gender
with col2:
    fig2 = px.box(df, x="Gender", y="Overall", color="Gender",
                  title="Distribution of Overall Scores by Gender",
                  color_discrete_sequence=px.colors.qualitative.Pastel)
    fig2.update_layout(height=400)
    st.plotly_chart(fig2, use_container_width=True)

# 3. Distribution of Overall Scores
fig3 = px.histogram(df, x="Overall", nbins=10, color="Gender",
                    title="Distribution of Overall Performance (Overall CGPA)",
                    color_discrete_sequence=px.colors.qualitative.Vivid,
                    marginal="box")
fig3.update_layout(height=400)
st.plotly_chart(fig3, use_container_width=True)

# ==============================
# SECTION 2: STUDY HABITS
# ==============================
st.header("💻 Study Habits and Skills")
col3, col4 = st.columns(2)

# 1. Average CGPA by Computer Proficiency
with col3:
    fig4 = px.bar(df, x="Computer", y="Overall", color="Computer",
                  title="Average CGPA by Computer Proficiency",
                  color_discrete_sequence=px.colors.qualitative.Bold)
    fig4.update_layout(height=400)
    st.plotly_chart(fig4, use_container_width=True)

# 2. Preparation Time vs. Average Overall Score
with col4:
    fig5 = px.bar(df, x="Preparation_cat", y="Overall", color="Preparation_cat",
                  title="Average Overall Score by Preparation Time",
                  color_discrete_sequence=px.colors.qualitative.Safe)
    fig5.update_layout(height=400)
    st.plotly_chart(fig5, use_container_width=True)

# 3. Attendance vs. Overall Score
fig6 = px.box(df, x="Attendance_cat", y="Overall", color="Attendance_cat",
              title="Overall Performance by Attendance Level",
              color_discrete_sequence=px.colors.diverging.Tealrose)
fig6.update_layout(height=400)
st.plotly_chart(fig6, use_container_width=True)

# ==============================
# SECTION 3: LIFESTYLE & SOCIO-ECONOMIC FACTORS
# ==============================
st.header("🕹️ Lifestyle and Socio-Economic Factors")
col5, col6 = st.columns(2)

# 1. Gaming Duration vs. Overall Score
with col5:
    fig7 = px.bar(df, x="Gaming_cat", y="Overall", color="Gaming_cat",
                  title="Average Overall Score by Gaming Duration",
                  color_discrete_sequence=px.colors.qualitative.Vivid)
    fig7.update_layout(height=400)
    st.plotly_chart(fig7, use_container_width=True)

# 2. Income vs. Overall Score
with col6:
    fig8 = px.box(df, x="Income_cat", y="Overall", color="Income_cat",
                  title="Overall Performance by Family Income Level",
                  color_discrete_sequence=px.colors.qualitative.Prism)
    fig8.update_layout(height=400)
    st.plotly_chart(fig8, use_container_width=True)

# 3. Job Status vs. Overall Score
fig9 = px.bar(df, x="Job", y="Overall", color="Job",
              title="Comparison of Academic Performance by Job Status",
              color_discrete_sequence=px.colors.qualitative.Pastel1)
fig9.update_layout(height=400)
st.plotly_chart(fig9, use_container_width=True)

# --- FOOTER ---
st.divider()
st.markdown("👩‍💻 Developed using Python, Pandas, Plotly, and Streamlit.")
