# AI Chat with Documents 📚

## Project Overview
Developed by Anish Mahapatra, this project features an intuitive user interface for interacting with documents using AI-driven insights. It integrates OpenAI's powerful AI models to process and generate coherent responses from uploaded documents in various formats such as PDF, DOCX, PPTX, and XLSX.

## Objectives
- **User-Friendly Interface**: Provides a streamlined interface for uploading and interacting with multiple document sources.
- **AI API Integration**: Utilizes OpenAI to enable rich, context-aware interactions with document contents.
- **Multi-Format Document Handling**: Supports a variety of document formats, enhancing accessibility and user engagement.
- **Interactive Prompts**: Allows users to query uploaded documents dynamically, fostering a conversational model that aids in information extraction and understanding.
- **Scalable Architecture**: Designed to be flexible and scalable, accommodating future enhancements like additional AI integrations or document types.

## Key Features
- **Multi-Source Document Input**: Users can upload multiple documents simultaneously, supported by a backend that handles diverse document types.
- **Dynamic AI Interaction**: The application connects with OpenAI to interpret and respond to user queries based on the document contents.
- **Customizable User Interaction**: Through an intuitive UI, users can craft specific prompts to guide the AI in generating relevant responses.
- **Security and Privacy**: Implements essential security measures to ensure data integrity and confidentiality.
- **Accessibility and Ease of Use**: A focus on user experience with features like error handling and real-time feedback on document processing.

## Technical Specifications
- **Frontend**: Streamlit
- **API Integration**: OpenAI
- **Document Processing**: Custom functions leveraging Python libraries like PyPDF2, python-docx, python-pptx, and pandas for handling different file formats.
- **Data Handling**: Utilizes LangChain for AI interactions, including text splitting, vector storage, and conversational chains.
- **Deployment**: Designed for ease of deployment and scalability, accommodating various deployment environments.

## Installation and Setup
1. **Clone the repository**:
    ```bash
    git clone [repository-link]
    ```
2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3. **Set up environment variables**:
    - Configure `OPENAI_API_KEY` for API access.

## Usage
Run the application:
```bash
streamlit run app.py