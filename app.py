from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import load_prompt
from dotenv import load_dotenv
import streamlit as st


# Load environment variables
load_dotenv()


# Page configuration
st.set_page_config(
    page_title="Research Assistant",
    page_icon="🔬",
    layout="centered"
)


# Initialize Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)


# Load prompt template
prompt_template = load_prompt("prompt_template.json")


# App title
st.title("🔬 Research Assistant")
st.write(
    "Generate customized explanations of AI research topics "
    "using Google Gemini and LangChain."
)


# Research paper selection
paper_title = st.selectbox(
    "📄 Select a research topic",
    [
        "Attention Is All You Need",
        "BERT",
        "GPT-3",
        "RAG",
        "Generative AI"
    ]
)


# Explanation style
style_input = st.selectbox(
    "🎨 Select explanation style",
    [
        "Beginner-friendly",
        "Technical",
        "Code-oriented",
        "Concise",
        "Detailed",
        "Mathematical"
    ]
)


# Explanation length
length_input = st.selectbox(
    "📏 Select explanation length",
    ["Short", "Medium", "Long"]
)


# Generate explanation
if st.button("✨ Generate Explanation", use_container_width=True):

    with st.spinner("Generating explanation..."):

        chain = prompt_template | model

        result = chain.invoke({
            "paper_title": paper_title,
            "style_input": style_input,
            "length_input": length_input
        })

    st.subheader("📚 Explanation")
    st.markdown(result.content[0]["text"])
