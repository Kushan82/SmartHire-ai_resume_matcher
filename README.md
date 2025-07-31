# **SmartHire AI Resume Matcher**
Intelligent resume matching and ranking system powered by advanced NLP and semantic analysis

## **🚀 Overview**
SmartHire AI is a sophisticated resume matching platform that leverages cutting-edge Natural Language Processing techniques to intelligently rank candidates against job descriptions. The system combines traditional TF-IDF vectorization with modern transformer-based semantic embeddings to provide accurate, context-aware candidate matching with integrated LLM feedback.

## **✨ Key Features**
* **🧠 Dual Matching Engine**: TF-IDF and transformer-based semantic similarity for comprehensive analysis
* **📄 Multi-Format Support**: PDF, DOCX, and TXT file processing with robust text extraction
* **🎯 Intelligent Ranking**: Automatic candidate ranking based on job description alignment
* **💬 LLM Integration**: Contextual feedback and insights using Mistral AI via Ollama
* **🔍 Semantic Querying**: Natural language queries to find specific candidate skills and experiences
* **⚡ Real-Time Processing**: Streamlit-powered interactive web interface with instant results
* **📊 Visual Analytics**: Color-coded similarity matrices and interactive result exploration
* **🎨 Modern UI**: Clean, intuitive interface with expandable resume previews

## **🏗️ Architecture**

```
SmartHire-AI/
├── src/
│   ├── data_loader.py          # Multi-format file processing
│   ├── preprocessing.py        # Text cleaning and NLP preprocessing
│   ├── feature_engineering.py  # TF-IDF vectorization engine
│   ├── semantic_matcher.py     # Transformer-based similarity
│   └── llm_utils.py            # Mistral AI integration
├── app/
│   └── streamlit_app.py        # Interactive web interface
├── data/
│   ├── resumes/               # Resume storage
│   └── job_descriptions/      # Job description storage
├── notebooks/
│   └── 01_eda_and_model.ipynb # Analysis and experimentation
└── config/
    └── config.yaml            # Configuration management
```

## **🔧 Technology Stack**

**Core NLP & ML**
- **Sentence Transformers**: Advanced semantic embeddings with `all-MiniLM-L6-v2`
- **scikit-learn**: TF-IDF vectorization and cosine similarity
- **spaCy**: Text preprocessing and linguistic analysis
- **NLTK**: Tokenization and stopword removal

**Document Processing**
- **PyMuPDF**: High-performance PDF text extraction
- **python-docx**: DOCX document processing
- **BeautifulSoup4**: HTML content cleaning

**LLM Integration**
- **Ollama**: Local LLM deployment and management
- **Mistral AI**: Advanced reasoning and feedback generation

**Frontend & Deployment**
- **Streamlit**: Interactive web application framework
- **pandas/NumPy**: Data manipulation and numerical computing

## **🚀 Quick Start**

### **Prerequisites**
* Python 3.10+
* Ollama with Mistral model
* spaCy English model

### **1. Clone Repository**
```bash
git clone https://github.com/yourusername/SmartHire-ai_resume_matcher.git
cd SmartHire-ai_resume_matcher
```

### **2. Environment Setup**
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Download spaCy model
python -m spacy download en_core_web_sm
```

### **3. Ollama Setup**
```bash
# Install and start Ollama
curl -fsSL https://ollama.ai/install.sh | sh
ollama serve

# Pull Mistral model
ollama pull mistral
```

### **4. Data Preparation**
```bash
# Create data directories
mkdir -p data/resumes data/job_descriptions

# Add your resume files (PDF, DOCX, TXT) to data/resumes/
# Add job descriptions (TXT) to data/job_descriptions/
```

### **5. Run Application**
```bash
# Start Streamlit app
streamlit run app/streamlit_app.py
```

### **6. Access Application**
* **Web Interface**: http://localhost:8501
* **Upload resumes and job descriptions to start matching!**

## **📊 Matching Algorithms**

### **TF-IDF Vectorization**
- **Purpose**: Keyword-based similarity using term frequency analysis
- **Strengths**: Fast, interpretable, handles domain-specific terminology
- **Use Case**: Initial filtering and traditional HR keyword matching

### **Semantic Embeddings**
- **Model**: `all-MiniLM-L6-v2` (384-dimensional embeddings)
- **Purpose**: Context-aware semantic understanding
- **Strengths**: Captures meaning beyond exact keywords, handles synonyms
- **Use Case**: Deep semantic analysis and nuanced skill matching

### **Hybrid Scoring**
The system provides both scoring methods, allowing users to compare traditional keyword matching with modern semantic analysis for comprehensive candidate evaluation.

## **💬 LLM Integration**

### **Mistral AI Features**
- **Resume Analysis**: Detailed strengths and improvement areas
- **Contextual Q&A**: Natural language queries about candidate experience
- **Match Explanation**: Why candidates rank high or low for specific roles
- **Personalized Feedback**: Tailored recommendations for resume improvement

### **Sample Queries**
- "Who has AWS cloud experience?"
- "Which candidates have project management skills?"
- "Find resumes with Python and machine learning background"

## **🎯 Use Cases**

**For Recruiters**
- Quickly identify top candidates from large resume pools
- Understand why candidates match specific requirements
- Generate detailed candidate assessments with AI insights

**For HR Teams**
- Standardize resume screening processes
- Reduce unconscious bias through objective scoring
- Create detailed feedback for candidate communications

**For Candidates**
- Receive AI-powered feedback on resume effectiveness
- Understand how to better align with job requirements
- Get specific improvement recommendations

## **📈 Performance Metrics**

**Matching Accuracy**
- Semantic similarity scores: 0.0 - 1.0 range
- Color-coded visualization for quick assessment
- Ranked results with confidence indicators

**Processing Speed**
- Multi-resume batch processing
- Real-time similarity computation
- Optimized text extraction pipelines
