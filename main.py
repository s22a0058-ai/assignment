import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE SETUP ---
st.set_page_config(page_title="Student Performance Dashboard", layout="wide")

# --- LOAD DATA ---
@st.cache_data
def load_data():
    df = pd.read_csv("ResearchInformation3_cleaned.csv")
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

    with st.sidebar.expander("🔍 Filters for Objective 1"):
        departments = st.multiselect("Select Department", df["Department"].unique(), default=df["Department"].unique())
        genders = st.multiselect("Select Gender", df["Gender"].unique(), default=df["Gender"].unique())

    filtered_df = df[(df["Department"].isin(departments)) & (df["Gender"].isin(genders))]

    col1, col2 = st.columns(2)

    # Chart 1: Average Overall CGPA by Department
    with col1:
        fig1 = px.bar(filtered_df, x="Department", y="Overall", color="Department",
                      title="Average CGPA by Department", 
                      color_discrete_sequence=px.colors.qualitative.Set2)
        st.plotly_chart(fig1, use_container_width=True)

    # Chart 2: Distribution by Gender
    with col2:
        fig2 = px.box(filtered_df, x="Gender", y="Overall", color="Gender",
                      title="CGPA Distribution by Gender",
                      color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig2, use_container_width=True)

    # Chart 3: Overall Distribution
    fig3 = px.histogram(filtered_df, x="Overall", nbins=10, color="Gender", 
                        title="Distribution of Overall Performance",
                        marginal="box", color_discrete_sequence=px.colors.qualitative.Vivid)
    st.plotly_chart(fig3, use_container_width=True)

# --- OBJECTIVE 2 ---
elif "Objective 2" in objective:
    st.header("💻 Objective 2: Study & Learning Behavior")
    st.write("To explore how study-related factors such as computer use, preparation time, and attendance influence academic performance.")

    with st.sidebar.expander("🔍 Filters for Objective 2"):
        semesters = st.multiselect("Select Semester", df["Semester"].unique(), default=df["Semester"].unique())
    filtered_df = df[df["Semester"].isin(semesters)]

    col1, col2 = st.columns(2)

    # Chart 1: Computer Skill vs Overall
    with col1:
        fig1 = px.box(filtered_df, x="Computer", y="Overall", color="Computer",
                      title="Computer Proficiency vs CGPA",
                      color_discrete_sequence=px.colors.sequential.Plasma)
        st.plotly_chart(fig1, use_container_width=True)

    # Chart 2: Preparation vs CGPA
    with col2:
        fig2 = px.bar(filtered_df, x="Preparation_cat", y="Overall", color="Preparation_cat",
                      title="Preparation Time vs Average CGPA", 
                      color_discrete_sequence=px.colors.qualitative.Safe)
        st.plotly_chart(fig2, use_container_width=True)

    # Chart 3: Attendance vs CGPA
    fig3 = px.box(filtered_df, x="Attendance_cat", y="Overall", color="Attendance_cat",
                  title="Attendance vs Overall CGPA",
                  color_discrete_sequence=px.colors.diverging.Tealrose)
    st.plotly_chart(fig3, use_container_width=True)

# --- OBJECTIVE 3 ---
elif "Objective 3" in objective:
    st.header("🕹️ Objective 3: Lifestyle & Non-Academic Factors")
    st.write("To examine how lifestyle and socioeconomic factors (gaming, income, part-time jobs, extracurriculars) influence academic outcomes.")

    with st.sidebar.expander("🔍 Filters for Objective 3"):
        incomes = st.multiselect("Select Income Level", df["Income_cat"].dropna().unique(), default=df["Income_cat"].dropna().unique())
    filtered_df = df[df["Income_cat"].isin(incomes)]

    col1, col2 = st.columns(2)

    # Chart 1: Gaming vs CGPA
    with col1:
        fig1 = px.bar(filtered_df, x="Gaming_cat", y="Overall", color="Gaming_cat",
                      title="Gaming Duration vs CGPA",
                      color_discrete_sequence=px.colors.qualitative.Vivid)
        st.plotly_chart(fig1, use_container_width=True)

    # Chart 2: Income vs CGPA
    with col2:
        fig2 = px.box(filtered_df, x="Income_cat", y="Overall", color="Income_cat",
                      title="Income vs CGPA",
                      color_discrete_sequence=px.colors.qualitative.Bold)
        st.plotly_chart(fig2, use_container_width=True)

    # Chart 3: Job Status vs CGPA
    fig3 = px.bar(filtered_df, x="Job", y="Overall", color="Job",
                  title="Part-time Job vs CGPA",
                  color_discrete_sequence=px.colors.qualitative.Prism)
    st.plotly_chart(fig3, use_container_width=True)

# --- FOOTER ---
st.divider()
st.markdown("👩‍💻 Developed using Python, Pandas, Plotly, and Streamlit.")
