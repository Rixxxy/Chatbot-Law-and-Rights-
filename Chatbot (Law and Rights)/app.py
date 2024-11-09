import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai  as genai

# Load environment variables from the .env file
load_dotenv()

# Configure the Google Generative AI model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

# Set up the page configuration
st.set_page_config(page_title="Nyay_Mitra", layout="wide")


st.markdown("""
    <style>
        .sidebar .sidebar-content {
            background-image: linear-gradient(#2e7bcf, #2e7bcf);
            color: white;
        }
        .sidebar .sidebar-content .element-container {
            padding: 0.5rem;
        }
        .sidebar .sidebar-content .element-container:hover {
            background-color: rgba(255, 255, 255, 0.2);
        }
        .stButton>button {
            background-color: #2e7bcf;
            color: white;
        }
        .stButton>button:hover {
            background-color: #2e7bcf;
            color: white;
            opacity: 0.8;
        }
        .block-container {
            padding-top: 2rem;
        }
        .faq-item {
            margin-bottom: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# Navigation bar
st.sidebar.title("Navigation")
st.sidebar.markdown("---")
page = st.sidebar.radio("Go to", ["Home", "About", "How to Use", "FAQ", "Chat", "Chat History", "Contact"])



# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Function to get responses from the Gemini  model, considering chat history
def get_gemini_response(question):
    context = "\n".join([f"Q: {chat['question']} A: {chat['response']}" for chat in st.session_state.chat_history])
    
    # Handle introductory queries
    introduction_queries = [
        "introduce yourself",
        "who are you",
        "what is your name",
        "tell me about yourself",
        "what can you do",
        "what is Nyay Mitra",
        "what are you"
    ]
    if any(q in question.lower() for q in introduction_queries):
        return (
            "Hello! I am Nyay Mitra, your dedicated legal assistant. I am here to help you understand "
            "the intricacies of the Indian Constitution and laws. Whether you are a student, legal professional, "
            "or a curious citizen, I aim to provide you with accurate, concise, and comprehensive information. "
            "Feel free to ask me anything related to the Indian legal framework, and I will do my best to assist you. "
            "Together, let's make legal knowledge accessible and understandable for all!"
        )

    # For regular queries, include chat history and question
    prompt = (
        f"This is a query related to the Indian Constitution or Indian law. Please provide an accurate and concise answer. "
        f"If the query goes beyond the scope, limit your response and mention Nyay Mitra is not trained for such data in a polite and friendly way.\n\n"
        f"Previous queries and responses:\n{context}\n\n"
        f"Question: {question}\n"
    
    )
    response = model.generate_content(prompt)
    return response.text

# Define the Home page
def home_page():
    st.title("Nyay Mitra")
    st.markdown("""
    ### Welcome to Nyay Mitra
    Nyay Mitra is your go-to resource for understanding the Indian Constitution and laws.
    
    #### About Nyay Mitra
    Nyay Mitra aims to demystify the complexities of the Indian legal system by providing 
    clear, concise, and comprehensive information. Whether you are a student, a legal professional, 
    or just a curious citizen, Nyay Mitra is here to help you navigate the legal landscape of India 
    with ease and confidence.

    #### Features
    - **In-depth Articles:** Access a vast collection of articles covering various aspects of the Indian Constitution, legal principles, and landmark cases.
    - **Legal Glossary:** Look up definitions of legal terms and phrases to enhance your understanding of legal language.
    - **Interactive Q&A:** Engage with our chatbot to get answers to your legal queries in real-time.
    - **Latest Updates:** Stay informed about recent changes in laws, important judgments, and legal news.

    #### Our Mission
    Our mission is to promote legal literacy and awareness among the general public. 
    By providing accurate and up-to-date information, we strive to empower individuals 
    to understand their rights and responsibilities under the law.

    #### Get Started
    Explore the various sections of Nyay Mitra to find the information you need. 
    Use the navigation bar to access different features, and don't hesitate to ask our chatbot 
    if you have any specific questions. 

    Thank you for visiting Nyay Mitra. Together, let's make legal knowledge accessible to all!
    """)

# Define the Chat page
def chat_page():
    st.header("Ask Nyay Mitra")
    with st.form(key="question_form", clear_on_submit=True):
        input_text = st.text_input("Enter your question about the Indian Constitution or law:", key="input")
        submit_button = st.form_submit_button(label="Ask the question")

        if submit_button and input_text:
            response = get_gemini_response(input_text)
            st.session_state.chat_history.append({"question": input_text, "response": response})
            st.subheader("Response")
            st.write(response)

# Define the Contact page
def contact_page():
    st.title("Contact Us")
    st.markdown("""
    If you have any questions, suggestions, or need support, please reach out to us:

    - **Email:** contact@nyaymitra.com
    - **Address:** SDMIT,Ujire, Dakshina Kannada,Karnataka India

    #### Follow Us
    Stay connected with us on social media for the latest updates and legal insights:
    
    - **Twitter:** [@NyayMitra](https://twitter.com/NyayMitra)
    - **Facebook:** [NyayMitra](https://facebook.com/NyayMitra)
    - **LinkedIn:** [NyayMitra](https://linkedin.com/company/nyaymitra)

    We value your feedback and are always here to help you with any questions or concerns you may have.
    """)

# Define the About page
def about_page():
    st.title("About Nyay Mitra")
    st.markdown("""
    Nyay Mitra is an initiative to make legal information more accessible to the general public. 
    Our goal is to empower people with the knowledge they need to navigate the legal system effectively.
    
    #### Our Vision
    To create a society where legal knowledge is freely accessible and understood by all, 
    promoting justice and equality.

    #### Our Team
    Nyay Mitra is powered by a dedicated team of students who 
    are passionate about making legal information accessible to everyone.

    #### Our Technology
    This application leverages advanced AI technology, specifically Google Gemini Pro, to ensure 
    reliable and efficient service. By utilizing cutting-edge AI, Nyay Mitra can provide precise 
    and accurate responses to your legal queries in real-time.

    #### Our Commitment
    We are committed to continuously improving Nyay Mitra by updating our content and incorporating 
    user feedback to better serve your needs.
    """)

# Define the FAQ page
def faq_page():
    st.title("Frequently Asked Questions (FAQ)")

    faqs = [
        ("What is Nyay Mitra?", "Nyay Mitra is a chatbot designed to provide information and answer queries related to the Indian Constitution and laws."),
        ("How does Nyay Mitra work?", "Nyay Mitra uses advanced AI technology to understand your questions and provide accurate responses based on the Indian legal framework."),
        ("Who can use Nyay Mitra?", "Anyone with questions about the Indian Constitution and laws can use Nyay Mitra, including students, legal professionals, and the general public."),
        ("Is Nyay Mitra free to use?", "Yes, Nyay Mitra is a free resource to help make legal information more accessible."),
        ("How accurate are the responses provided by Nyay Mitra?", "Nyay Mitra aims to provide accurate and up-to-date information, but it's always a good idea to consult a legal professional for specific legal advice.")
    ]

    for question, answer in faqs:
        st.markdown(f"**Q: {question}**")
        st.markdown(f"**A: {answer}**")
        st.markdown("---")

# Define the How to Use page
def how_to_use_page():
    st.title("How to Use Nyay Mitra")
    st.markdown("""
    ### Getting Started with Nyay Mitra

    #### Navigation
    Use the navigation bar at the top to access different sections of the application:
    - **Home:** Learn about Nyay Mitra and its features.
    - **Chat:** Engage with our interactive chatbot to get answers to your legal questions.
    - **Contact:** Find out how to get in touch with us.
    - **About:** Learn more about the mission and team behind Nyay Mitra.
    - **FAQ:** Find answers to common questions about Nyay Mitra.

    #### Using the Chatbot
    1. **Enter Your Question:** Type your question related to the Indian Constitution or laws into the chatbox.
    2. **Receive an Answer:** The chatbot will provide a response based on its extensive legal knowledge.
    3. **Follow Up:** If you need further clarification, you can ask follow-up questions.



    #### Staying Updated
    - Follow us on social media to stay informed about the latest legal updates and news.
    - Check the Latest Updates section for recent changes in laws and important judgments.

    #### Feedback and Support
    - If you encounter any issues or have suggestions for improvement, please contact us through the Contact page.
    - Your feedback is invaluable in helping us improve Nyay Mitra and serve you better.

    Thank you for using Nyay Mitra. We hope this application helps you navigate the legal system with confidence and ease.
    """)

# Define the Chat History page
def chat_history():
    st.header("Chat History")

    if st.session_state.chat_history:
        for chat in st.session_state.chat_history:
            st.markdown(f"**Q:** {chat['question']}")
            st.markdown(f"**A:** {chat['response']}")
            st.markdown("---")
    else:
        st.write("No chat history available yet.")

# Page routing
if page == "Home":
    home_page()
elif page == "Chat":
    chat_page()
elif page == "Contact":
    contact_page()
elif page == "About":
    about_page()
elif page == "FAQ":
    faq_page()
elif page == "How to Use":
    how_to_use_page()
elif page == "Chat History":
    chat_history()