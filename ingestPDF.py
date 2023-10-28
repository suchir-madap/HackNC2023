from fileReader import convertPDF


def readUploadedPdf(uploaded_file):
    if uploaded_file is not None:
        with open("data/store.pdf", "wb") as f:
            print(type(f))
            f.write(uploaded_file.read())

        convertPDF("data/store.pdf")




from langchain.document_loaders import PyPDFLoader



def convertPDF(uploadFile):
    loader = PyPDFLoader(uploadFile)

    pages = loader.load()
    print(pages)