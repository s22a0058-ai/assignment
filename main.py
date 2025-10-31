import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

# --- PAGE SETUP ---
st.set_page_config(page_title="Student Performance Dashboard", layout="wide")

# --- LOAD DATA ---
@st.cache_data
def load_data():
    # Reading the generated sample data file
    df = pd.read_csv("student_data.csv")
    return df

try:
    df = load_data()
except FileNotFoundError:
    st.error("Error: The data file 'student_data.csv' was not found. Please ensure it is uploaded.")
    st.stop()


# Ensure categorical columns are properly ordered for better visualization
category_orders = {
    "Preparation_cat": ["Low", "Moderate", "High"],
    "Attendance_cat": ["Low", "Medium", "High"],
    "Income_cat": ["Low", "Medium", "High"],
    "Gaming_cat": ["Low", "Moderate", "High"]
}
for col, order in category_orders.items():
    if col in df.columns:
        df[col] = pd.Categorical(df[col], categories=order, ordered=True)

# --- SIDEBAR ---
st.sidebar.title("🎯 Dashboard Navigation")
st.sidebar.markdown("Use this panel to select an analysis objective.")

objective = st.sidebar.radio(
    "Choose Objective:",
    [
        "Objective 1: Academic Performance Overview",
        "Objective 2: Study & Learning Behavior",
        "Objective 3: Lifestyle & Non-Academic Factors"
    ]
)

st.sidebar.divider()
st.sidebar.markdown("📘 *Data Source:* Student Performance Metrics Dataset")

# --- PAGE HEADER ---
st.title("🎓 Student Performance Dashboard")
st.markdown("An interactive visualization dashboard analyzing academic, behavioral, and lifestyle factors affecting student performance.")

st.divider()

# --- OBJECTIVE 1 ---
if "Objective 1" in objective:
    st.header("📊 Objective 1: Academic Performance Overview")
    st.write("To analyze how students’ overall academic performance (CGPA) varies across departments and gender. **Charts are interactive: hover to see data, click and drag to zoom.**")

    # Filter by Department & Gender
    with st.sidebar.expander("🔍 Filters for Objective 1"):
        departments = st.multiselect("Select Department", df["Department"].unique(), default=df["Department"].unique())
        genders = st.multiselect("Select Gender", df["Gender"].unique(), default=df["Gender"].unique())
    
    filtered_df = df[(df["Department"].isin(departments)) & (df["Gender"].isin(genders))]

    col1, col2 = st.columns(2)

    # Visualization 1: Department vs Overall (Interactive Bar Chart)
    with col1:
        st.subheader("Average Overall CGPA by Department")
        
        chart1 = alt.Chart(filtered_df).mark_bar().encode(
            x=alt.X("Department:N", axis=alt.Axis(labelAngle=-45)),
            y=alt.Y("mean(Overall):Q", title="Average Overall CGPA"),
            color="Department:N",
            tooltip=["Department", alt.Tooltip("mean(Overall)", format=".2f", title="Avg CGPA")],
            order=alt.Order("mean(Overall):Q", sort="descending")
        ).properties(
            title="Avg CGPA by Department"
        ).interactive() # Enable zooming and panning
        
        st.altair_chart(chart1, use_container_width=True)

    # Visualization 2: Gender vs Overall (Interactive Box Plot)
    with col2:
        st.subheader("Distribution of Overall CGPA by Gender")
        
        chart2 = alt.Chart(filtered_df).mark_boxplot(extent="min-max").encode(
            x="Gender:N",
            y=alt.Y("Overall:Q", title="Overall CGPA"),
            color="Gender:N",
            tooltip=["Gender", "Overall"]
        ).properties(
            title="CGPA Distribution by Gender"
        ).interactive()
        
        st.altair_chart(chart2, use_container_width=True)

    # Visualization 3: CGPA Distribution (Interactive Histogram)
    st.subheader("Distribution of Overall Performance")
    
    chart3 = alt.Chart(filtered_df).mark_bar().encode(
        x=alt.X("Overall:Q", bin=alt.Bin(maxbins=20), title="Overall CGPA"),
        y=alt.Y("count():Q", title="Number of Students"),
        tooltip=[alt.Tooltip("Overall:Q", bin=True), "count():Q"]
    ).properties(
        title="Overall CGPA Frequency"
    ).interactive()
    
    st.altair_chart(chart3, use_container_width=True)

# --- OBJECTIVE 2 ---
elif "Objective 2" in objective:
    st.header("💻 Objective 2: Study & Learning Behavior")
    st.write("To explore how study-related factors such as computer use, preparation time, and attendance influence academic performance.")

    with st.sidebar.expander("🔍 Filters for Objective 2"):
        # Note: Semester is not in the dummy data, so I'll comment it out for the runnable example
        # semesters = st.multiselect("Select Semester", df["Semester"].unique(), default=df["Semester"].unique())
        # filtered_df = df[df["Semester"].isin(semesters)]
        filtered_df = df # Use all data

    col1, col2 = st.columns(2)
    
    # Visualization 1: Computer Skill vs Overall (Interactive Box Plot)
    with col1:
        st.subheader("Computer Proficiency vs Overall Score")
        
        chart4 = alt.Chart(filtered_df).mark_boxplot(extent="min-max").encode(
            x=alt.X("Computer:N", sort=["Poor", "Average", "Good", "Excellent"], title="Computer Skill"),
            y=alt.Y("Overall:Q", title="Overall CGPA"),
            color=alt.Color("Computer:N", sort=["Poor", "Average", "Good", "Excellent"]),
            tooltip=["Computer", "Overall"]
        ).properties(
            title="CGPA by Computer Skill"
        ).interactive()
        
        st.altair_chart(chart4, use_container_width=True)

    # Visualization 2: Preparation Time vs Average CGPA (Interactive Bar Chart)
    with col2:
        st.subheader("Preparation Time vs Average CGPA")
        
        chart5 = alt.Chart(filtered_df).mark_bar().encode(
            x=alt.X("Preparation_cat:N", title="Preparation Time", sort=category_orders["Preparation_cat"]),
            y=alt.Y("mean(Overall):Q", title="Average Overall CGPA"),
            color=alt.Color("Preparation_cat:N", sort=category_orders["Preparation_cat"]),
            tooltip=["Preparation_cat", alt.Tooltip("mean(Overall)", format=".2f", title="Avg CGPA")]
        ).properties(
            title="Avg CGPA by Preparation Time"
        ).interactive()
        
        st.altair_chart(chart5, use_container_width=True)

    # Visualization 3: Attendance vs CGPA (Interactive Box Plot)
    st.subheader("Attendance vs Overall CGPA")
    
    chart6 = alt.Chart(filtered_df).mark_boxplot(extent="min-max").encode(
        x=alt.X("Attendance_cat:N", title="Attendance", sort=category_orders["Attendance_cat"]),
        y=alt.Y("Overall:Q", title="Overall CGPA"),
        color=alt.Color("Attendance_cat:N", sort=category_orders["Attendance_cat"]),
        tooltip=["Attendance_cat", "Overall"]
    ).properties(
        title="CGPA Distribution by Attendance"
    ).interactive()
    
    st.altair_chart(chart6, use_container_width=True)


# --- OBJECTIVE 3 ---
elif "Objective 3" in objective:
    st.header("🕹️ Objective 3: Lifestyle & Non-Academic Factors")
    st.write("To examine how lifestyle and socioeconomic factors (gaming, income, part-time jobs, extracurriculars) influence academic outcomes.")

    with st.sidebar.expander("🔍 Filters for Objective 3"):
        incomes = st.multiselect("Select Income Level", df["Income_cat"].dropna().unique(), default=df["Income_cat"].dropna().unique())
    
    filtered_df = df[df["Income_cat"].isin(incomes)]

    col1, col2 = st.columns(2)

    # Visualization 1: Gaming vs CGPA (Interactive Bar Chart)
    with col1:
        st.subheader("Gaming Duration vs Overall Performance")
        
        chart7 = alt.Chart(filtered_df).mark_bar().encode(
            x=alt.X("Gaming_cat:N", title="Gaming Duration", sort=category_orders["Gaming_cat"]),
            y=alt.Y("mean(Overall):Q", title="Average Overall CGPA"),
            color=alt.Color("Gaming_cat:N", sort=category_orders["Gaming_cat"]),
            tooltip=["Gaming_cat", alt.Tooltip("mean(Overall)", format=".2f", title="Avg CGPA")]
        ).properties(
            title="Avg CGPA by Gaming Duration"
        ).interactive()
        
        st.altair_chart(chart7, use_container_width=True)

    # Visualization 2: Income vs CGPA (Interactive Box Plot)
    with col2:
        st.subheader("Family Income vs Overall CGPA")
        
        chart8 = alt.Chart(filtered_df).mark_boxplot(extent="min-max").encode(
            x=alt.X("Income_cat:N", title="Income Level", sort=category_orders["Income_cat"]),
            y=alt.Y("Overall:Q", title="Overall CGPA"),
            color=alt.Color("Income_cat:N", sort=category_orders["Income_cat"]),
            tooltip=["Income_cat", "Overall"]
        ).properties(
            title="CGPA Distribution by Income"
        ).interactive()
        
        st.altair_chart(chart8, use_container_width=True)
