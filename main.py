import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- PAGE SETUP ---
st.set_page_config(page_title="Student Performance Dashboard", layout="wide")

st.title("🎓 Student Performance Visualization Dashboard")
st.markdown("This dashboard visualizes relationships between academic performance, study behavior, and lifestyle factors.")

# --- LOAD DATA ---
@st.cache_data
def load_data():
    df = pd.read_csv("/content/ResearchInformation3_cleaned.csv")
    return df

df = load_data()

# --- SIDEBAR FILTERS ---
st.sidebar.header("🔍 Filter Data")
departments = st.sidebar.multiselect("Select Department", df["Department"].unique(), default=df["Department"].unique())
genders = st.sidebar.multiselect("Select Gender", df["Gender"].unique(), default=df["Gender"].unique())

filtered_df = df[(df["Department"].isin(departments)) & (df["Gender"].isin(genders))]

# --- METRICS ---
st.subheader("📊 Key Statistics")
col1, col2, col3 = st.columns(3)
col1.metric("Average CGPA", f"{filtered_df['Overall'].mean():.2f}")
col2.metric("Average HSC Score", f"{filtered_df['HSC'].mean():.1f}")
col3.metric("Average Attendance (%)", f"{filtered_df['Attendance_cat'].value_counts().idxmax()}")

st.divider()

# --- VISUAL 1: Academic Performance ---
st.subheader("1️⃣ Academic Performance by Department and Gender")
fig, ax = plt.subplots(figsize=(8,4))
sns.barplot(x="Department", y="Overall", hue="Gender", data=filtered_df, ci=None, ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

# --- VISUAL 2: Study Behavior ---
st.subheader("2️⃣ Study Behavior Patterns")
fig, ax = plt.subplots(figsize=(8,4))
sns.boxplot(x="Preparation_cat", y="Overall", data=filtered_df, ax=ax)
plt.title("Preparation Time vs Overall CGPA")
st.pyplot(fig)

# --- VISUAL 3: Lifestyle Factors ---
st.subheader("3️⃣ Lifestyle Impact")
fig, ax = plt.subplots(figsize=(8,4))
sns.barplot(x="Gaming_cat", y="Overall", data=filtered_df, ci=None, ax=ax)
plt.title("Gaming Duration vs Academic Performance")
st.pyplot(fig)

# --- FOOTER ---
st.markdown("---")
st.markdown("📚 *Data Source:* Student Performance Metrics Dataset (Mendeley Data, DOI: 10.17632/5b82ytz489.1)")

