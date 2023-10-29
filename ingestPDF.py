from fileReader import convertPDF


# takes in a pdf file from streamlit that is stored in memory and then uploads content to a file
def readUploadedPdf(uploaded_file):
    if uploaded_file is not None:
        with open("data/store.pdf", "wb") as f:
            print(type(f))
            f.write(uploaded_file.read())

    return convertPDF("data/store.pdf")




from langchain.document_loaders import PyPDFLoader


# takes in a pdf and loads it and returns it
def convertPDF(uploadFile):
    loader = PyPDFLoader(uploadFile)

    pages = loader.load()
    return pages
    