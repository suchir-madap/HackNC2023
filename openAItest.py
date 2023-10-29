import os 

from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.document_loaders import TextLoader
from langchain.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma



llm = OpenAI()
# print(llm("tell me a joke"))

from langchain.chains.question_answering import load_qa_chain

# load document
loader = PyPDFLoader("data/gettysburg_address.pdf")
documents = loader.load()

### For multiple documents 
# loaders = [....]
# documents = []
# for loader in loaders:
#     documents.extend(loader.load())

chain = load_qa_chain(llm=OpenAI(), chain_type="map_reduce")
query = "what is the purpose of the speech?"
testing = chain.run(input_documents=documents, question=query)

print(testing)

# # load document
# loader = PyPDFLoader("data/gettysburg_address.pdf")
# documents = loader.load()

# # split the documents into chunks
# text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
# texts = text_splitter.split_documents(documents)


# # select which embeddings we want to use
# embeddings = OpenAIEmbeddings()
# # create the vectorestore to use as the index
# db = Chroma.from_documents(texts, embeddings)
# # expose this index in a retriever interface
# retriever = db.as_retriever(search_type="similarity", search_kwargs={"k":2})
# # create a chain to answer questions 
# qa = RetrievalQA.from_chain_type(
#     llm=OpenAI(), chain_type="stuff", retriever=retriever, return_source_documents=True)
# query = "what is the total number of AI publications?"
# result = qa({"query": query})

