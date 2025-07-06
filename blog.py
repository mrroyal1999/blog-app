
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

# --- Page Config ---
st.set_page_config(page_title="Naib Althaf | AI/ML Engineer", layout="wide")

# --- Load Resume PDF ---
with open("malthaf resume.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

# --- Sidebar Navigation ---
with st.sidebar:
    selected =option_menu(menu_title="Main Menu",options=["Home", "About Me", "Projects", "Skills", "Resume", "Contact"],icons=["house", "person", "briefcase", "tools", "file-earmark-person", "envelope"],menu_icon="cast",default_index=0)

if selected == "Home":
    st.markdown(
        """
        <style>
        html, body, .stApp {
            height: 100%;
            background-color: #0a0a0a;
        }

        .split-container {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: flex-start;      /* keep content up */
        padding: 3rem 4rem 2rem 4rem; /* top right bottom left */
        min-height: calc(100vh - 4rem); /* account for top Streamlit padding */
        box-sizing: border-box;


      

        }

        .left-content {
            flex: 1.1;
            color: white;
            display: flex;
            flex-direction: column;
            justify-content: center;
            height: 100%;
            padding-right: 2rem;
        }

        .right-content {
            flex: 1;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100%;
        }

        .right-content img {
            max-width: 500px;
            width: 100%;
            height: auto;
            border-radius: 12px;
            box-shadow: 0 0 35px rgba(0, 255, 255, 0.4);
        }

        h1 {
            font-size: 3.5rem;
            font-weight: 800;
            margin-bottom: 0.5rem;
        }

        h3 {
            font-size: 1.7rem;
            font-weight: 500;
            margin-bottom: 1.2rem;
        }

        p {
            font-size: 1.2rem;
            line-height: 1.8;
            margin-bottom: 1rem;
        }

        .contact-links {
            margin-top: 1.2rem;
        }

        .contact-links a {
            color: #ffd700;
            text-decoration: none;
            font-weight: bold;
            margin-right: 1rem;
            font-size: 1.1rem;
        }

        .contact-links a:hover {
            text-decoration: underline;
        }

        @media screen and (max-width: 768px) {
            .split-container {
                flex-direction: column;
                text-align: center;
                height: auto;
                padding: 2rem;
            }

            .right-content {
                margin-top: 2rem;
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="split-container">
            <div class="left-content">
                <h1>👋 Naib Mohammad Althaf</h1>
                <h3>Machine Learning Engineer | Data Scientist</h3>
                <p>
                    Passionate about building scalable, ethical, and impactful AI systems for real-world problems.
                </p>
                <p style='font-style: italic;'>“The best way to predict the future is to invent it.” – Alan Kay</p>
                <div class="contact-links">
                    📁 <a href="https://github.com/naib1999/my-projects" target="_blank">GitHub</a>
                    📧 <a href="mailto:naibalthaf@gmail.com">Email</a>
                    📞 9704077035
                </div>
            </div>
            <div class="right-content">
                <img src="https://plus.unsplash.com/premium_photo-1682756540097-6a887bbcf9b0?q=80&w=1171&auto=format&fit=crop&ixlib=rb-4.1.0" alt="AI Brain">
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )







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
        st.image("IMG_0042s.jpg", width=200)
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
