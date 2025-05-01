import streamlit as st
import os 
import shutil

# Define the folder where PDFs will be stored 
UPLOAD_DIR = "data"

#check the upload directory exists
os.makedirs(UPLOAD_DIR, exist_ok=True)

def clear_upload_pdf():
    for filename in os.listdir( UPLOAD_DIR):
        file_path = os.path.join(UPLOAD_DIR,filename)
        if os.path.isfile(file_path):
            os.remove(file_path)


def save_uploaded_pdfs(uploaded_files):
    for file in uploaded_files:
        with open(os.path.join(UPLOAD_DIR,file.name),'wb') as f:
            f.write(file.getbuffer())


def main():
    st.set_page_config(page_title="Chat With Multiple PDFs", page_icon=":books:")
    
    st.header("Chat with multiple PDFs :books:")
    st.text_input("Ask a question about your documents:")

    with st.sidebar:
        st.subheader("Your Documents")
        uploaded_files = st.file_uploader("upload your PDFs", type=["pdf"], accept_multiple_files=True)

        if st.button("process") and uploaded_files:
            clear_upload_pdf() # clearn previous pdf
            save_uploaded_pdfs(uploaded_files)
            #st.success(f"{len(uploaded_files)} file(s) uploaded and saved.")

        # st.file_uploader("Upload your PDF here and Click on 'Process'")
        # st.button("Process")

if __name__ == "__main__":
    main()
