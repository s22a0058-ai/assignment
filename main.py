import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE SETUP ---
st.set_page_config(page_title="Student Performance Dashboard", layout="wide")

# --- SUMMARY BOX SECTION ---
st.subheader("📦 Summary Statistics")

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("👥 Total Students", f"{df.shape[0]}")
col2.metric("📈 Average CGPA", f"{df['Overall'].mean():.2f}")
col3.metric("🏆 Highest CGPA", f"{df['Overall'].max():.2f}")
col4.metric("📉 Lowest CGPA", f"{df['Overall'].min():.2f}")
col5.metric("🏫 Most Common Department", df['Department'].mode()[0])

st.markdown("---")

# --- RAW DATA PREVIEW SECTION ---
st.subheader("🗂️ Raw Data Preview")

with st.expander("Click to view dataset"):
    st.dataframe(df.head(20))  # show first 20 rows
    st.caption("Showing first 20 rows. You can scroll horizontally to view all columns.")

# --- LOAD DATA ---
@st.cache_data
def load_data():
    df = pd.read_csv("ResearchInformation3_cleaned.csv")
    return df

df = load_data()

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("🎯 Dashboard Navigation")
objective = st.sidebar.radio(
    "Choose Objective:",
    [
        "Objective 1: Academic Performance Overview",
        "Objective 2: Study & Learning Behavior",
        "Objective 3: Lifestyle & Socio-Economic Factors"
    ]
)

st.sidebar.divider()
st.sidebar.markdown("📘 *Data Source:* Student Performance Metrics Dataset (Mendeley Data, DOI: 10.17632/5b82ytz489.1)")

# --- PAGE HEADER ---
st.title("🎓 Student Performance Dashboard")
st.markdown("An interactive visualization dashboard analyzing academic, behavioral, and lifestyle factors affecting student performance.")
st.divider()

# =====================================================================
# OBJECTIVE 1: Academic Performance
# =====================================================================
if "Objective 1" in objective:
    st.header("📊 Objective 1: Academic Performance Overview")
    st.write("To analyze how students’ overall academic performance varies across departments and gender.")

    # --- SIDEBAR FILTERS ---
    with st.sidebar.expander("🔍 Filters for Objective 1"):
        selected_dept = st.multiselect("Select Department", df["Department"].unique(), default=df["Department"].unique())
        selected_gender = st.multiselect("Select Gender", df["Gender"].unique(), default=df["Gender"].unique())

    filtered_df = df[(df["Department"].isin(selected_dept)) & (df["Gender"].isin(selected_gender))]

    col1, col2 = st.columns(2)

    # Chart 1: Average CGPA by Department
    with col1:
        fig1 = px.bar(filtered_df, x="Department", y="Overall", color="Department",
                      title="Average CGPA by Department",
                      color_discrete_sequence=px.colors.qualitative.Set2)
        st.plotly_chart(fig1, use_container_width=True)

    # Chart 2: CGPA Distribution by Gender
    with col2:
        fig2 = px.box(filtered_df, x="Gender", y="Overall", color="Gender",
                      title="Distribution of CGPA by Gender",
                      color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig2, use_container_width=True)

    # Chart 3: Distribution of Overall CGPA
    fig3 = px.histogram(filtered_df, x="Overall", nbins=10, color="Gender",
                        title="Distribution of Overall Performance",
                        color_discrete_sequence=px.colors.qualitative.Vivid,
                        marginal="box")
    st.plotly_chart(fig3, use_container_width=True)

# =====================================================================
# OBJECTIVE 2: Study & Learning Behavior
# =====================================================================
elif "Objective 2" in objective:
    st.header("💻 Objective 2: Study & Learning Behavior")
    st.write("To explore how study-related factors such as computer use, preparation time, and attendance influence academic performance.")

    # --- SIDEBAR FILTERS ---
    with st.sidebar.expander("🔍 Filters for Objective 2"):
        selected_semester = st.multiselect("Select Semester", df["Semester"].unique(), default=df["Semester"].unique())

    filtered_df = df[df["Semester"].isin(selected_semester)]

    col1, col2 = st.columns(2)

    # Chart 1: Computer Proficiency vs CGPA
    with col1:
        fig4 = px.bar(filtered_df, x="Computer", y="Overall", color="Computer",
                      title="Average CGPA by Computer Proficiency",
                      color_discrete_sequence=px.colors.qualitative.Bold)
        st.plotly_chart(fig4, use_container_width=True)

    # Chart 2: Preparation Time vs CGPA
    with col2:
        fig5 = px.bar(filtered_df, x="Preparation_cat", y="Overall", color="Preparation_cat",
                      title="Average Overall Score by Preparation Time",
                      color_discrete_sequence=px.colors.qualitative.Safe)
        st.plotly_chart(fig5, use_container_width=True)

    # Chart 3: Attendance vs CGPA
    fig6 = px.box(filtered_df, x="Attendance_cat", y="Overall", color="Attendance_cat",
                  title="Overall Performance by Attendance Level",
                  color_discrete_sequence=px.colors.diverging.Tealrose)
    st.plotly_chart(fig6, use_container_width=True)

# =====================================================================
# OBJECTIVE 3: Lifestyle & Socio-Economic Factors
# =====================================================================
elif "Objective 3" in objective:
    st.header("🕹️ Objective 3: Lifestyle & Socio-Economic Factors")
    st.write("To examine how lifestyle and socioeconomic factors (gaming, income, part-time jobs, extracurriculars) influence students’ academic outcomes.")

    # --- SIDEBAR FILTERS ---
    with st.sidebar.expander("🔍 Filters for Objective 3"):
        selected_income = st.multiselect("Select Income Level", df["Income_cat"].dropna().unique(), default=df["Income_cat"].dropna().unique())

    filtered_df = df[df["Income_cat"].isin(selected_income)]

    col1, col2 = st.columns(2)

    # Chart 1: Gaming vs CGPA
    with col1:
        fig7 = px.bar(filtered_df, x="Gaming_cat", y="Overall", color="Gaming_cat",
                      title="Average Overall Score by Gaming Duration",
                      color_discrete_sequence=px.colors.qualitative.Vivid)
        st.plotly_chart(fig7, use_container_width=True)

    # Chart 2: Income vs CGPA
    with col2:
        fig8 = px.box(filtered_df, x="Income_cat", y="Overall", color="Income_cat",
                      title="Overall Performance by Family Income Level",
                      color_discrete_sequence=px.colors.qualitative.Prism)
        st.plotly_chart(fig8, use_container_width=True)

    # Chart 3: Job vs CGPA
    fig9 = px.bar(filtered_df, x="Job", y="Overall", color="Job",
                  title="Comparison of Academic Performance by Job Status",
                  color_discrete_sequence=px.colors.qualitative.Pastel1)
    st.plotly_chart(fig9, use_container_width=True)

# --- FOOTER ---
st.divider()
st.markdown("👩‍💻 Developed using Python, Pandas, Plotly, and Streamlit.")
