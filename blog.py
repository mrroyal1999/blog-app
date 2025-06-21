
import streamlit as st
from PIL import Image
#from streamlit_option_menu import option_menu

# --- Page Config ---
st.set_page_config(page_title="Naib Althaf | AI/ML Engineer", layout="wide")

# --- Load Resume PDF ---
with open("malthaf resume.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

# --- Sidebar Navigation ---
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "About Me", "Projects", "Skills", "Resume", "Contact"],
        icons=["house", "person", "briefcase", "tools", "file-earmark-person", "envelope"],
        menu_icon="cast",
        default_index=0,
    )

# --- Home ---
if selected == "Home":
    st.title("👋 Naib Mohammad Althaf")
    st.subheader("Machine Learning Engineer | Data Scientist")
    st.markdown(
        """
        Passionate about building scalable, ethical, and impactful AI systems for real-world problems.
        
        [GitHub](https://github.com/naib1999/my-projects) | [Email](mailto:naibalthaf@gmail.com) | 📞 9704077035
        """
    )
    st.image("https://images.unsplash.com/photo-1504384308090-c894fdcc538d", caption="AI & Innovation")
    st.markdown("---")

# --- About Me ---
elif selected == "About Me":
    st.header("🙋‍♂️ About Me")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
            I am a Data Scientist with over 3 years of experience designing and deploying machine learning solutions across various domains. 
            With a background in mechanical engineering and a Master’s in Data Science, I’ve transformed my passion for AI into real-world impact.

            Currently working at Tata Consultancy Services, I’ve built chatbots using RAG pipelines, improved workflows, and developed tools 
            that reduced hours of manual effort. My interest lies in natural language processing, explainable AI, and bridging ML systems 
            with real business needs.
        """)
    with col2:
        st.image("https://avatars.githubusercontent.com/u/674621?v=4", width=200)
    st.markdown("---")

# --- Projects ---
elif selected == "Projects":
    st.header("🚀 Featured Projects")
    project_cols = st.columns(2)

    with project_cols[0]:
        st.subheader("🔧 RAG-Based AI Chatbot for Designers")
        st.write("""
        - Developed and deployed an internal chatbot using Retrieval-Augmented Generation (RAG).
        - Reduced search time for designers and improved access to knowledge.
        - Scalable deployment using Azure Databricks.
        """)

    with project_cols[1]:
        st.subheader("📊 Sentiment Analysis for Renewable Energy Tweets")
        st.write("""
        - NLP model classifies tweets into positive, negative, and neutral.
        - Helped stakeholders analyze public opinion on renewable trends.
        - Used deep learning for improved performance.
        """)

    st.markdown("---")

# --- Skills ---
elif selected == "Skills":
    st.header("🛠️ Skills & Technologies")
    skill_groups = {
        "Languages & Tools": ["Python", "SQL", "Git", "Azure Databricks", "Hadoop"],
        "Machine Learning": ["scikit-learn", "Regression", "Model Evaluation"],
        "Deep Learning & NLP": ["TensorFlow", "PyTorch", "RNNs", "GPT APIs", "LangChain"],
        "Data Handling": ["Pandas", "NumPy", "EDA", "Matplotlib", "Seaborn"],
        "Cloud & MLOps": ["Azure", "MLflow", "Deployment"],
        "Core Concepts": ["RAG", "Explainable AI", "Agile"]
    }
    for category, skills in skill_groups.items():
        st.subheader(f"{category}")
        st.markdown(", ".join(f"`{skill}`" for skill in skills))
    st.markdown("---")

# --- Resume ---
elif selected == "Resume":
    st.header("📄 Resume")
    st.download_button(
        label="⬇️ Download My Resume",
        data=PDFbyte,
        file_name="Naib_Althaf_Resume.pdf",
        mime='application/octet-stream',
    )
    st.markdown("---")

# --- Contact ---
elif selected == "Contact":
    st.header("📬 Contact Me")
    st.write("Feel free to reach out via email or connect on GitHub!")
    st.write("**Email:** naibalthaf@gmail.com")
    st.write("**Phone:** 9704077035")
    st.write("**GitHub:** [github.com/naib1999/my-projects](https://github.com/naib1999/my-projects)")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        message = st.text_area("Message")
        send = st.form_submit_button("Send Message")
        if send:
            st.success("Thank you! Your message has been sent.")
    st.markdown("---")
