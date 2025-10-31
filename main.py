import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- PAGE SETUP ---
st.set_page_config(page_title="Student Performance Dashboard", layout="wide")

# --- LOAD DATA ---
@st.cache_data
def load_data():
    df = pd.read_csv("ResearchInformation3_cleaned(1).csv")
    return df

df = load_data()

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
st.sidebar.markdown("📘 *Data Source:* Student Performance Metrics Dataset (Mendeley Data, DOI: 10.17632/5b82ytz489.1)")

# --- PAGE HEADER ---
st.title("🎓 Student Performance Dashboard")
st.markdown("An interactive visualization dashboard analyzing academic, behavioral, and lifestyle factors affecting student performance.")

st.divider()

# --- OBJECTIVE 1 ---
if "Objective 1" in objective:
    st.header("📊 Objective 1: Academic Performance Overview")
    st.write("To analyze how students’ overall academic performance varies across departments and gender.")

    # Filter by Department & Gender
    with st.sidebar.expander("🔍 Filters for Objective 1"):
        departments = st.multiselect("Select Department", df["Department"].unique(), default=df["Department"].unique())
        genders = st.multiselect("Select Gender", df["Gender"].unique(), default=df["Gender"].unique())
    filtered_df = df[(df["Department"].isin(departments)) & (df["Gender"].isin(genders))]

    # Visualization 1: Department vs Overall
    st.subheader("Average Overall CGPA by Department")
    fig, ax = plt.subplots(figsize=(8,4))
    sns.barplot(x="Department", y="Overall", data=filtered_df, ci=None, ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Visualization 2: Gender vs Overall
    st.subheader("Distribution of Overall CGPA by Gender")
    fig, ax = plt.subplots(figsize=(6,4))
    sns.boxplot(x="Gender", y="Overall", data=filtered_df, ax=ax)
    st.pyplot(fig)

    # Visualization 3: CGPA Distribution
    st.subheader("Distribution of Overall Performance")
    fig, ax = plt.subplots(figsize=(6,4))
    sns.histplot(filtered_df["Overall"], bins=10, kde=True, ax=ax)
    st.pyplot(fig)

# --- OBJECTIVE 2 ---
elif "Objective 2" in objective:
    st.header("💻 Objective 2: Study & Learning Behavior")
    st.write("To explore how study-related factors such as computer use, preparation time, and attendance influence academic performance.")

    with st.sidebar.expander("🔍 Filters for Objective 2"):
        semesters = st.multiselect("Select Semester", df["Semester"].unique(), default=df["Semester"].unique())
    filtered_df = df[df["Semester"].isin(semesters)]

    # Visualization 1: Computer Skill vs Overall
    st.subheader("Computer Proficiency vs Overall Score")
    fig, ax = plt.subplots(figsize=(7,4))
    sns.boxplot(x="Computer", y="Overall", data=filtered_df, ax=ax)
    st.pyplot(fig)

    # Visualization 2: Preparation Time vs CGPA
    st.subheader("Preparation Time vs Average CGPA")
    fig, ax = plt.subplots(figsize=(7,4))
    sns.barplot(x="Preparation_cat", y="Overall", data=filtered_df, estimator="mean", ci=None, ax=ax)
    st.pyplot(fig)

    # Visualization 3: Attendance vs CGPA
    st.subheader("Attendance vs Overall CGPA")
    fig, ax = plt.subplots(figsize=(7,4))
    sns.boxplot(x="Attendance_cat", y="Overall", data=filtered_df, ax=ax)
    st.pyplot(fig)

# --- OBJECTIVE 3 ---
elif "Objective 3" in objective:
    st.header("🕹️ Objective 3: Lifestyle & Non-Academic Factors")
    st.write("To examine how lifestyle and socioeconomic factors (gaming, income, part-time jobs, extracurriculars) influence academic outcomes.")

    with st.sidebar.expander("🔍 Filters for Objective 3"):
        incomes = st.multiselect("Select Income Level", df["Income_cat"].dropna().unique(), default=df["Income_cat"].dropna().unique())
    filtered_df = df[df["Income_cat"].isin(incomes)]

    # Visualization 1: Gaming vs CGPA
    st.subheader("Gaming Duration vs Overall Performance")
    fig, ax = plt.subplots(figsize=(7,4))
    sns.barplot(x="Gaming_cat", y="Overall", data=filtered_df, estimator="mean", ci=None, ax=ax)
    st.pyplot(fig)

    # Visualization 2: Income vs CGPA
    st.subheader("Family Income vs Overall CGPA")
    fig, ax = plt.subplots(figsize=(7,4))
    sns.boxplot(x="Income_cat", y="Overall", data=filtered_df, ax=ax)
    st.pyplot(fig)

    # Visualization 3: Job Status vs CGPA
