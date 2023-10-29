# import
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.document_loaders import TextLoader


# load the document and split it into chunks



# split it into chunks

def chunking(documents, query):
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    # create the open-source embedding function
    embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    # load it into Chroma
    db = Chroma.from_documents(docs, embedding_function)

    # query it
    # query = "Who wrote the gettysburg address"
    docs = db.similarity_search(query)

    # print results
    print(docs[0].page_content)
    return docs[0].page_content



import os 

from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.document_loaders import TextLoader
from langchain.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma



os.environ['openAIkey']
llm = OpenAI()


# print(llm("tell me a joke"))

from langchain.chains.question_answering import load_qa_chain


def callAPI(documents, query):

    chain = load_qa_chain(llm=OpenAI(), chain_type="map_reduce")

    testing = chain.run(input_documents=documents, question=query)
    return testing