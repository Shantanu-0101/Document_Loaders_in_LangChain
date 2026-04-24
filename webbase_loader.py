from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import TextLoader
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-4-31B-it",
    task='text-generation'
)

model = ChatHuggingFace(llm=llm)

prompt = PromptTemplate(
    template='answer the following qestion \n {question} from the followring text \n {text}}',
    input_variables=['question','text']
)


url = 'https://www.apple.com/in/macbook-neo/'
loader = WebBaseLoader(url)

docs = loader.load()

parser = StrOutputParser()

print(len(docs))

# print(docs[0].page_content)

chain = prompt | model | parser

chain.invoke({'question':'what is the product that we are talking about?', 'text':docs[0].page_content})