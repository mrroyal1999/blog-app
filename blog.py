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
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "About Me", "Projects", "Skills", "Resume", "Contact"],
        icons=["house", "person", "briefcase", "tools", "file-earmark-person", "envelope"],
        menu_icon="cast",
        default_index=0,
    )

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
            align-items: flex-start;
            padding: 3rem 4rem 2rem 4rem;
            min-height: calc(100vh - 4rem);
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

elif selected == "About Me":
    st.markdown(
        """
        <style>
        html, body, .stApp {
            height: 100%;
        }
        .about-wrapper {
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: flex-start;
            padding: 2rem 4rem;
            background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
            box-sizing: border-box;
        }
        .about-container {
            max-width: 1000px;
            width: 100%;
            background-color: rgba(0, 0, 0, 0.4);
            border-radius: 20px;
            padding: 3rem 3rem 2rem 3rem;
            box-shadow: 0 0 30px rgba(0, 255, 255, 0.2);
            color: #f0f0f0;
        }
        .about-container h2 {
            color: #00e6e6;
            font-size: 2.2rem;
            margin-bottom: 1.5rem;
        }
        .about-container p {
            font-size: 1.2rem;
            line-height: 1.8;
            margin-bottom: 1rem;
        }
        @media screen and (max-width: 768px) {
            .about-wrapper {
                padding: 2rem 1rem;
            }
            .about-container {
                padding: 2rem;
            }
            .about-container h2 {
                font-size: 1.8rem;
            }
            .about-container p {
                font-size: 1.1rem;
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="about-wrapper">
            <div class="about-container">
                <h2>🙋‍♂️ About Me</h2>
                <p>
                    I am a Data Scientist with over 3 years of experience designing and deploying machine learning solutions across various domains.
                    With a background in mechanical engineering and a Master’s in Data Science, I’ve transformed my passion for AI into real-world impact.
                </p>
                <p>
                    Currently working at <strong>Tata Consultancy Services</strong>, I’ve built chatbots using <strong>RAG pipelines</strong>, improved workflows, and developed tools 
                    that reduced hours of manual effort. My interest lies in <strong>Natural Language Processing</strong>, <strong>Explainable AI</strong>, and bridging ML systems 
                    with real business needs.
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

elif selected == "Projects":
    st.header("🚀 Featured Projects")
    st.markdown("""
    <style>
    .project-section {
        display: flex;
        overflow-x: auto;
        flex-wrap: nowrap;
        gap: 1rem;
        padding: 1rem 0;
        scroll-behavior: smooth;
    }
    .project-card {
        min-width: 300px;
        max-width: 350px;
        background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
        color: white;
        margin-right: 1.5rem;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 0 15px rgba(0,255,255,0.3);
        transition: transform 0.3s ease;
    }
    .project-card:hover {
        transform: scale(1.05);
        box-shadow: 0 0 25px rgba(0,255,255,0.5);
    }
    .project-title {
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .project-desc {
        font-size: 1rem;
        line-height: 1.6;
    }
    ::-webkit-scrollbar {
        height: 8px;
    }
    ::-webkit-scrollbar-thumb {
        background: #00e6e6;
        border-radius: 10px;
    }
    </style>
    <div class="project-section">
        <div class="project-card">
            <img src="https://your-image-url.jpg" style="width:100%; border-radius:10px; margin-bottom:1rem;">
            <div class="project-title">🔧 RAG-Based AI Chatbot for Designers</div>
            <div class="project-desc">
                - Built internal RAG chatbot to assist UI/UX designers.<br>
                - Integrated with Azure Databricks for scalability.<br>
                - Improved knowledge retrieval efficiency.<br>
                <a href="https://github.com/your-link" target="_blank" style="color:#00e6e6;font-weight:bold;">🔗 View Project</a>
            </div>
        </div>
        <div class="project-card">
            <div class="project-title">📊 Sentiment Analysis of Renewable Tweets</div>
            <div class="project-desc">
                - Trained NLP model for classifying renewable energy tweets.<br>
                - Helped stakeholders understand public sentiment.<br>
                - Leveraged deep learning for robust predictions.
            </div>
        </div>
        <div class="project-card">
            <div class="project-title">🤖 Chatbot Feedback Summarizer</div>
            <div class="project-desc">
                - Created tool to summarize customer chatbot feedback using LLMs.<br>
                - Enabled product teams to extract key complaints easily.<br>
                - Integrated with internal dashboards.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

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

elif selected == "Resume":
    st.header("📄 Resume")
    st.download_button(
        label="⬇️ Download My Resume",
        data=PDFbyte,
        file_name="Naib_Althaf_Resume.pdf",
        mime='application/pdf',
    )
    st.markdown("---")

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
