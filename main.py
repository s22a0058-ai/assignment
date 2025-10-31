import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Placeholder DataFrame (Replace this section with your actual data loading)
try:
    df # Check if df already exists
except NameError:
    data = {
        'Department': ['CS', 'EE', 'ME', 'CS', 'EE', 'ME', 'CS', 'EE', 'ME', 'CS'],
        'Overall': [3.5, 3.2, 2.8, 3.8, 3.0, 2.5, 3.6, 3.4, 2.9, 3.7],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
        'Computer': ['Good', 'Excellent', 'Average', 'Excellent', 'Good', 'Average', 'Excellent', 'Good', 'Average', 'Excellent'],
        'Preparation_cat': ['High', 'Low', 'Medium', 'High', 'Low', 'Medium', 'High', 'Low', 'Medium', 'High'],
        'Attendance_cat': ['High', 'Medium', 'Low', 'High', 'Medium', 'Low', 'High', 'Medium', 'Low', 'High'],
        'Gaming_cat': ['Low', 'High', 'Medium', 'Low', 'High', 'Medium', 'Low', 'High', 'Medium', 'Low'],
        'Income_cat': ['High', 'Low', 'Medium', 'High', 'Low', 'Medium', 'High', 'Low', 'Medium', 'High'],
        'Job': ['No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes'],
    }
    df = pd.DataFrame(data)

# Set Streamlit page title and configuration
st.set_page_config(layout="wide")

# ==========================================================
# 🎯 SIDEBAR OBJECTIVE 🎯
# ==========================================================
st.sidebar.header('Dashboard Objective')
st.sidebar.markdown(
    """
    This dashboard provides a comprehensive **Exploratory Data Analysis (EDA)** of student academic performance data, measured by **Overall CGPA**. 
    
    The objective is to visualize and understand the relationships between academic outcomes and various **demographic, behavioral, and socio-economic factors** such as department, study habits (preparation, attendance), computer proficiency, lifestyle (gaming), and job status.
    
    Use the sections below to explore these insights.
    """
)
st.sidebar.info("Data source: Simulated Academic Performance Data") # Optional: Add a little note

# ==========================================================
# MAIN PAGE CONTENT
# ==========================================================
st.title('📊 Academic Performance Visualization Dashboard')

# ---
# Section 1: Core Performance Metrics
# ---
st.header('Core Performance Metrics')

# 1. Average Overall Score by Department
st.subheader('1. Average Overall Score by Department')
fig1, ax1 = plt.subplots(figsize=(10, 5))
sns.barplot(x='Department', y='Overall', data=df, estimator='mean', errorbar=None, palette='pastel', ax=ax1)
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45)
ax1.set_title('Average Overall Score by Department')
st.pyplot(fig1)

# 2. CGPA by Gender
st.subheader('2. Distribution of Overall Scores by Gender')
fig2, ax2 = plt.subplots(figsize=(8, 5))
sns.boxplot(x='Gender', y='Overall', data=df, palette='pastel', ax=ax2)
ax2.set_title('Distribution of Overall Scores by Gender')
st.pyplot(fig2)

# 3. Distribution of Overall Scores
st.subheader('3. Distribution of Overall Performance (Overall CGPA)')
fig3, ax3 = plt.subplots(figsize=(8, 5))
sns.histplot(df['Overall'], bins=10, kde=True, color=sns.color_palette('pastel')[0], ax=ax3)
ax3.set_title('Distribution of Overall Performance (Overall CGPA)')
st.pyplot(fig3)

---
# Section 2: Study Habits and Skills
---
st.header('Study Habits and Skills')

# 1. Average CGPA by Computer Proficiency
st.subheader('1. Average CGPA by Computer Proficiency')
fig4, ax4 = plt.subplots(figsize=(8, 5))
sns.barplot(x='Computer', y='Overall', data=df, estimator='mean', errorbar=None, palette='Blues_d', ax=ax4)
ax4.set_title('Average CGPA by Computer Proficiency')
st.pyplot(fig4)

# 2. Preparation Time vs. Average Overall Score
st.subheader('2. Average Overall Score by Preparation Time')
fig5, ax5 = plt.subplots(figsize=(8, 5))
sns.barplot(x='Preparation_cat', y='Overall', data=df, estimator='mean', errorbar=None, palette='pastel', ax=ax5)
ax5.set_title('Average Overall Score by Preparation Time')
st.pyplot(fig5)

# 3. Attendance vs. Overall Score
st.subheader('3. Overall Performance by Attendance Level')
fig6, ax6 = plt.subplots(figsize=(8, 5))
sns.boxplot(x='Attendance_cat', y='Overall', data=df, palette='pastel', ax=ax6)
ax6.set_title('Overall Performance by Attendance Level')
st.pyplot(fig6)

---
# Section 3: Lifestyle and Socio-Economic Factors
---
st.header('Lifestyle and Socio-Economic Factors')

# 1. Gaming Duration vs. Overall Score
st.subheader('1. Average Overall Score by Gaming Duration')
fig7, ax7 = plt.subplots(figsize=(8, 5))
sns.barplot(x='Gaming_cat', y='Overall', data=df, estimator='mean', errorbar=None, palette='pastel', ax=ax7)
ax7.set_title('Average Overall Score by Gaming Duration')
st.pyplot(fig7)

# 2. Income vs. Overall Score
st.subheader('2. Overall Performance by Family Income Level')
fig8, ax8 = plt.subplots(figsize=(8, 5))
sns.boxplot(x='Income_cat', y='Overall', data=df, palette='pastel', ax=ax8)
ax8.set_title('Overall Performance by Family Income Level')
st.pyplot(fig8)

# 3. Job Status vs. Overall Score
st.subheader('3. Comparison of Academic Performance by Job Status')
fig9, ax9 = plt.subplots(figsize=(8, 5))
sns.barplot(x='Job', y='Overall', data=df, estimator='mean', errorbar=None, palette='pastel', ax=ax9)
ax9.set_title('Comparison of Academic Performance by Job Status')
st.pyplot(fig9)

# End of Streamlit app
