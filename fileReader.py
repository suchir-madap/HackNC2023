# import
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.document_loaders import TextLoader


# load the document and split it into chunks

relativePath = "data/test.txt"


from langchain.document_loaders import PyPDFLoader



def convertPDF(uploadFile):
    loader = PyPDFLoader(uploadFile)

    pages = loader.load()
    print(pages)


import fitz  # PyMuPDF

def convert_pdf_to_txt(pdf_path):
    # txt_output_path = "data/try.txt"
    # # Open the PDF file
    # pdf_document = fitz.open(pdf_path)

    # text = ""
    # for page_num in range(pdf_document.page_count):
    #     # Get text from each page
    #     page = pdf_document.load_page(page_num)
    #     text += page.get_text("text")

    # # Write the text to a .txt file
    # with open(txt_output_path, 'w', encoding='utf-8') as txt_file:
    #     txt_file.write(text)
    
    loader = TextLoader(pdf_path)
    documents = loader.load() 

    print(documents)





# pass in the path of the file pdf



# pip install PyMuPDF
# pip3 install langchain