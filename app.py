import streamlit as st
import PyPDF2
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama

# Title of the app
st.title("📄 Iterative Document Summarizer")
st.write("Upload a PDF and get an AI-generated summary that improves with each iteration!")

# Initialize the AI model
@st.cache_resource
def load_model():
    try:
        model = Ollama(model="llama3.1")
        return model
    except:
        return None

# Function to read PDF text
def get_pdf_text(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Function to create summary with iterations
def create_summary(model, text, iterations=3):
    # Step 1: Create initial summary
    prompt = """
    Please create a clear and concise summary of this document:
    
    {document}
    
    Summary:
    """
    template = ChatPromptTemplate.from_template(prompt)
    summary = model.invoke(template.format(document=text))
    initial_summary = summary
    
    # Step 2: Refine the summary multiple times
    for i in range(iterations):
        refine_prompt = """
        Please improve and refine this summary to make it better:
        
        Original document: {document}
        
        Current summary: {current_summary}
        
        Improved summary:
        """
        refine_template = ChatPromptTemplate.from_template(refine_prompt)
        summary = model.invoke(refine_template.format(document=text, current_summary=summary))
    
    return initial_summary, summary

# Load the model
model = load_model()

if model is None:
    st.error("⚠️ Please make sure Ollama is running with llama3.1 model")
    st.code("ollama serve")
    st.code("ollama pull llama3.1")

# File upload
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file and model:
    # Extract text from PDF
    with st.spinner("Reading PDF..."):
        document_text = get_pdf_text(uploaded_file)
    
    st.info(f"Document loaded: {len(document_text.split())} words")
    
    # Add slider for iterations
    iterations = st.slider("Number of refinement iterations", min_value=1, max_value=5, value=3)
    st.info(f"The summary will be refined {iterations} times for better quality")
    
    # Generate summary when button is clicked
    if st.button("Generate Summary"):
        with st.spinner(f"Creating summary with {iterations} refinements..."):
            initial_summary, final_summary = create_summary(model, document_text, iterations)
            
        # Show both summaries
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("� Initial Summary")
            st.write(initial_summary)
            
        with col2:
            st.subheader(f"✨ Refined Summary ({iterations} iterations)")
            st.write(final_summary)
        
        # Option to download final summary
        st.download_button(
            label="Download Final Summary",
            data=final_summary,
            file_name="refined_summary.txt",
            mime="text/plain"
        )
