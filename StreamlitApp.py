import streamlit as st
from QAWithPDF.data_ingestion import load_data, save_uploaded_file
from QAWithPDF.embedding import download_gemini_embedding
from QAWithPDF.model_api import load_model

    
def main():
    st.set_page_config("QA with Documents")
    
    doc=st.file_uploader("upload your document")
    
    st.header("QA with Documents(Information Retrieval)")
    
    user_question= st.text_input("Ask your question")
    
    if st.button("submit & process"):
        with st.spinner("Processing..."):
            file_path = save_uploaded_file(doc)
            document=load_data(file_path)
            model=load_model()
            query_engine=download_gemini_embedding(model,document)
                
            response = query_engine.query(user_question)
                
            st.write(response.response)
                
                
if __name__=="__main__":
    main()          
                
    
    
    
    
    