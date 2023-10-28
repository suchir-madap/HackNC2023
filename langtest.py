# import
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.document_loaders import TextLoader


# load the document and split it into chunks

relativePath = "data/gettysburg_address.pdf"
loader = TextLoader(relativePath)
documents = loader.load() 



# def file_reader(file):
#     if(file.multiple_chunks() == False):
#         text = file.read()
#     else:
#         while(file.multiple_chunks()):
#             text += file.chunks()




# split it into chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

# create the open-source embedding function
embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# load it into Chroma
db = Chroma.from_documents(docs, embedding_function)

# query it
query = "What did the president say about Ketanji Brown Jackson"
docs = db.similarity_search(query)

# print results
print(docs[0].page_content)