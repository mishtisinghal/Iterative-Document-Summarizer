# 📄 Iterative Document Summarizer

A simple Python web application that extracts text from PDF files and generates AI-powered summaries using iterative refinement with LLaMA 3.1 via Ollama.

## Features
- **PDF Upload & Processing** - Extract text from PDF documents
- **AI-Powered Summarization** - Uses LLaMA 3.1 model for intelligent summarization
- **Iterative Refinement** - Improves summary quality through multiple refinement passes (1-5 iterations)
- **Side-by-Side Comparison** - View initial summary vs refined summary
- **Download Option** - Save final summary as text file
- **Clean Web Interface** - Built with Streamlit for easy use
- **Error Handling** - User-friendly messages and setup instructions

### Prerequisites
- Python 3.7+
- Ollama installed and running
- LLaMA 3.1 model downloaded

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/mishtisinghal/Iterative-Document-Summarizer.git
   cd Iterative-Document-Summarizer
   ```

2. **Install dependencies**
   ```bash
   pip install streamlit PyPDF2 langchain langchain_community
   ```

3. **Install and setup Ollama**
   ```bash
   # Install Ollama from https://ollama.ai
   ollama serve
   ollama pull llama3.1
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser** and go to `http://localhost:8501`

##  How to Use

1. **Upload PDF** - Click "Choose a PDF file" and select your document
2. **Set Iterations** - Use the slider to choose refinement passes (1-5)
3. **Generate Summary** - Click "Generate Summary" and wait for processing
4. **View Results** - Compare initial vs refined summary side-by-side
5. **Download** - Save the final summary using the download button

## Technical Details

### Core Components
- **Streamlit** - Web interface framework
- **PyPDF2** - PDF text extraction
- **LangChain** - AI model integration
- **Ollama** - Local LLM serving
- **LLaMA 3.1** - Large language model for summarization

### Architecture
```
PDF Upload → Text Extraction → Initial Summary → Iterative Refinement → Final Output
```

##  Performance

- **Small PDFs** (< 10 pages): ~30 seconds
- **Medium PDFs** (10-50 pages): ~2-5 minutes  
- **Large PDFs** (50+ pages): ~5-15 minutes

*Processing time depends on document size and number of refinement iterations*

## Contributing

This is a beginner-friendly project! Feel free to:
- Report bugs
- Suggest improvements
- Submit pull requests
