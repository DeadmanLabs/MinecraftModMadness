import os, time, json
from datetime import datetime

from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

batch_one = "1.7.10-1.12.2\\javadoc\\forge"
batch_two = "1.12.2-1.19.3\\javadoc"
batch_three = "1.19.4-1.20.4"

def buildRepository(basePath):
    loader = DirectoryLoader(basePath.replace("\\", "/") + "/", glob="**/*.html")
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=50)
    docs = splitter.split_documents(docs)
    #embeddings = OpenAIEmbeddings()
    embeddings = HuggingFaceEmbeddings()
    vectorstore = basePath.replace("\\", "/") + "/" + basePath.split("\\")[-1] + ".cvs"
    db = Chroma.from_documents(docs, embeddings, persist_directory=vectorstore)
    db.persist()
    return db

subdirectories = []
subdirectories += [os.path.join(batch_one, name) for name in os.listdir(batch_one) if os.path.isdir(os.path.join(batch_one, name))]
subdirectories += [os.path.join(batch_one, name) for name in os.listdir(batch_two) if os.path.isdir(os.path.join(batch_two, name))]
subdirectories += [os.path.join(batch_one, name) for name in os.listdir(batch_three) if os.path.isdir(os.path.join(batch_three, name))]
for forgeVersion in subdirectories:
    print("Processing " + forgeVersion.split('\\')[-1] +  " Version...")
    buildRepository(forgeVersion)
    print("Done!")
