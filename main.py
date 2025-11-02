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

# --- PAGE HEADER ---
st.title("🎓 Student Performance Dashboard")
st.markdown("An interactive visualization dashboard analyzing academic, behavioral, and lifestyle factors affecting student performance.")
st.divider()

# --- SUMMARY BOX SECTION ---
st.subheader("📦 Summary Statistics")

# Calculate gender counts safely for full dataset
if "Gender" in df.columns:
    male_count = df[df["Gender"].str.lower() == "male"].shape[0]
    female_count = df[df["Gender"].str.lower() == "female"].shape[0]
else:
    male_count = female_count = 0

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

col1.metric("👥 Total Students", f"{df.shape[0]}")
col2.metric("🚹 Total Male", f"{male_count}")
col3.metric("🚺 Total Female", f"{female_count}")
col4.metric("📈 Average CGPA", f"{df['Overall'].mean():.2f}")
col5.metric("🏆 Highest CGPA", f"{df['Overall'].max():.2f}")
col6.metric("📉 Lowest CGPA", f"{df['Overall'].min():.2f}")
col7.metric("🏫 Most Common Department", df['Department'].mode()[0])

st.write("""An overview of the student dataset is given by the summary statistics above. 
 Students from several departments are represented overall, and the distribution of male and female participants is almost equal. 
 According to the average CGPA, the majority of students score in the moderate to high academic category, showing generally high levels of success. 
 The performance disparity between students, which may be impacted by behavioral, academic, or socioeconomic variables, is highlighted by the greatest and lowest CGPA numbers. 
 The most popular department indicates where most students are concentrated, which may be a reflection of enrollment patterns or institutional focus. 
 Before delving into more in-depth visual analyses in later parts, these statistics provide a basic overview of the dataset's structure and overall academic achievement.""")
 


st.markdown("---")

# --- RAW DATA PREVIEW SECTION ---
st.subheader("🗂️ Raw Data Preview")

with st.expander("Click to view dataset"):
    st.dataframe(df.head(20))  # show first 20 rows
    st.caption("Showing first 20 rows. You can scroll horizontally to view all columns.")

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
        st.caption("🔍 Observation: Students from the Computer Science department achieved the highest average CGPA, suggesting program-level and institutional influences on performance.")

    # Chart 2: CGPA Distribution by Gender
    with col2:
        fig2 = px.box(filtered_df, x="Gender", y="Overall", color="Gender",
                      title="Distribution of CGPA by Gender",
                      color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig2, use_container_width=True)
        st.caption("📊 Observation: Female students show slightly higher median CGPAs, though overall gender performance is balanced — reflecting equitable academic achievement.")

    # Chart 3: Distribution of Overall CGPA
    fig3 = px.histogram(filtered_df, x="Overall", nbins=10, color="Gender",
                        title="Distribution of Overall Performance",
                        color_discrete_sequence=px.colors.qualitative.Vivid,
                        marginal="box")
    st.plotly_chart(fig3, use_container_width=True)
    st.caption("📈 Observation: The CGPA distribution is right-skewed, with most students achieving moderate to high performance (3.0–3.7). Few students fall below average, indicating generally strong academic achievement.")


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
        st.caption("💡 Observation: Students with higher computer proficiency consistently score higher CGPAs. This supports the relationship between digital literacy and academic success in technology-supported learning environments.")


    # Chart 2: Preparation Time vs CGPA
    with col2:
        fig5 = px.bar(filtered_df, x="Preparation_cat", y="Overall", color="Preparation_cat",
                      title="Average Overall Score by Preparation Time",
                      color_discrete_sequence=px.colors.qualitative.Safe)
        st.plotly_chart(fig5, use_container_width=True)
        st.caption("📘 Observation: Students who spend more time preparing for assessments achieve higher average CGPAs, confirming that consistent study time improves academic performance.")


    # Chart 3: Attendance vs CGPA
    fig6 = px.box(filtered_df, x="Attendance_cat", y="Overall", color="Attendance_cat",
                  title="Overall Performance by Attendance Level",
                  color_discrete_sequence=px.colors.diverging.Tealrose)
    st.plotly_chart(fig6, use_container_width=True)
    st.caption("📅 Observation: Higher attendance correlates with higher CGPAs, reinforcing that consistent class participation enhances understanding and academic results.")


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
        st.caption("🎮 Observation: Students with low to moderate gaming time perform better academically. Excessive gaming may reduce study focus, slightly lowering performance.")


    # Chart 2: Income vs CGPA
    with col2:
        fig8 = px.box(filtered_df, x="Income_cat", y="Overall", color="Income_cat",
                      title="Overall Performance by Family Income Level",
                      color_discrete_sequence=px.colors.qualitative.Prism)
        st.plotly_chart(fig8, use_container_width=True)
        st.caption("💰 Observation: Students from medium-income families tend to achieve the highest CGPAs, suggesting a balanced access to resources and stable study environments.")


    # Chart 3: Job vs CGPA
    fig9 = px.bar(filtered_df, x="Job", y="Overall", color="Job",
                  title="Comparison of Academic Performance by Job Status",
                  color_discrete_sequence=px.colors.qualitative.Pastel1)
    st.plotly_chart(fig9, use_container_width=True)
    st.caption("👔 Observation: Students without part-time jobs achieve slightly higher CGPAs. Working students may face time constraints that limit study hours, affecting overall performance.")


# --- FOOTER ---
st.divider()
st.markdown("👩‍💻 Developed using Python, Pandas, Plotly, and Streamlit.")
