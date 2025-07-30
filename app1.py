import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
df = pd.read_csv("clean_feeback.csv")
with st.sidebar:
    selected = option_menu(
        menu_title="Feedback Dashboard",
        options=["Overview", "Charts", "Insights"],
        icons=["bar-chart", "graph-up", "emoji-smile"],
        menu_icon="cast",default_index=0,
              styles={
            "container": {"padding": "5!important"},
            "icon": {"color": "white", "font-size": "20px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#ac407a"},
            "nav-link-selected": {"background-color": "#ec407a", "color": "white"},
        }
        
    )
if selected == "Overview":
    st.title("🎓 Student Feedback Analysis")
    st.markdown("""
        Welcome to the **Feedback Dashboard**!  
        This interactive tool helps analyze student responses and visualize which factors were most effective in College Events.  
        Navigate using the sidebar to explore charts and key insights.
    """)

    st.markdown("📁 **Dataset Preview**")
    st.dataframe(df.head())

#Charts
elif selected == "Charts":
    st.title("📊 Feedback Charts")

    # Graph 1
    st.subheader("📘 Well versed with the subject")
    fig1, ax1 = plt.subplots()
    df['Well versed with the subject'].value_counts().sort_values().plot(kind='bar', color='#3498DB', ax=ax1)
    ax1.set_xlabel("Rating")
    ax1.set_ylabel("No. of Students")
    st.pyplot(fig1)

    # Graph 2
    st.subheader("Provides support for students going above and beyond rating distribution")
    fig2, ax2 = plt.subplots()
    df['Provides support for students going above and beyond'].value_counts().sort_values().plot(kind='bar', color='#2ECC71', ax=ax2)
    ax2.set_xlabel("Rating")
    ax2.set_ylabel("No. of Students")
    st.pyplot(fig2)

    # Graph 3
    st.subheader('Top 3 Events with Highest Satisfaction:')
    fig3, ax3 = plt.subplots()
    df.drop(columns=['Student ID','Feedback','Sentiment']).mean().sort_values().tail(3).plot(
    kind='barh',
    color='#FFDB58',
    ax=ax3
    )
    ax3.set_xlabel("Average Ratings")
    st.pyplot(fig3)
#Graph 4
    st.subheader('Top 3 Events with Lowest Satisfaction:')
    fig4, ax4 = plt.subplots()
    df.drop(columns=['Student ID','Feedback','Sentiment']).mean().sort_values(ascending=False).tail(3).plot(
    kind='barh',
    color='#8E44AD',
    ax=ax4
    )
    ax4.set_xlabel("Average Ratings")
    st.pyplot(fig4)


# Insights
elif selected == "Insights":
    st.title("📌 Key Insights")

    # Mean Ratings per Column
    st.subheader("📈 Mean Ratings")
    mean_ratings = df.drop(columns=['Student ID']).mean(numeric_only=True).sort_values(ascending=False)
    st.dataframe(mean_ratings)

    # Top 3
    st.subheader("🟢 Top 3 Feedback Points")
    st.write(mean_ratings.head(3))

    # Bottom 3
    st.subheader("🔴 Bottom 3 Feedback Points")
    st.write(mean_ratings.tail(3))

    # Final Decision Example
    st.markdown("### 🎯 Conclusion")
    st.markdown("""
    - ✅ **Best performing aspect**: `Degree of difficulty of assignments`
    - ⚠️ **Needs improvement**: `Well versed with the subject`
    - 📝 Recommendation: Conduct teacher training on engaging delivery & Subject clarity.
    """)
