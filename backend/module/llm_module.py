import os
from decorators import logger, timeit_log

from dotenv import load_dotenv
from openai import OpenAI
from langchain_community.chat_models import ChatOpenAI
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise EnvironmentError("OPENAI_API_KEY not found in .env , please set in .env")

@timeit_log
def get_openai_sdk():
    return OpenAI()

@timeit_log
def get_chat_model(model_name="gpt-4.1-2025-04-14", temperature=1):
    return ChatOpenAI(model=model_name, 
                      temperature=temperature, 
                      api_key=openai_api_key,
                      verbose=True), model_name

@timeit_log
def get_embedding_model(model_name="text-embedding-ada-002"):
    return OpenAIEmbeddings(
        model=model_name,
        api_key=openai_api_key
    )
@timeit_log
def build_qa_chain(llm, retriever):
    return RetrievalQA.from_chain_type(
        llm=llm, 
        retriever=retriever,
        chain_type="stuff")

"""gpt-5-2025-08-07"""