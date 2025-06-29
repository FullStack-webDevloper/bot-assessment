# %%
from swarmauri.llms.concrete.GroqModel import GroqModel as LLM
from swarmauri.conversations.concrete.Conversation import Conversation
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
if API_KEY:
    llm = GroqModel(api_key=API_KEY)
    print("LLM initialized successfully.")
else:
    print("Error: GROQ_API_KEY not found in environment variables. Please set it before running the script.")   
    

# %%
from swarmauri.vector_stores.concrete.TfidfVectorStore import TfidfVectorStore
from swarmauri.documents.concrete.Document import Document

vector_store = TfidfVectorStore()

documents= [
    Document(content="This is a sample document."),
    Document(content="This is another sample document."),
    Document(content="This is a third sample document.")
]
vector_store.add_documents(documents)
print("Documents added to vector store successfully.")

all_docs=vector_store.get_all_documents()
print("All documents in vector store:")
for doc in all_docs:
    print(doc.content)  
    

# %%


# %%
from swarmauri.conversations.concrete.MaxSystemContextConversation import MaxSystemContextConversation
from swarmauri.messages.concrete.SystemMessage import SystemMessage
from swarmauri.messages.concrete.HumanMessage import HumanMessage

system_context=SystemMessage(content="You are a helpful assistant.")
conversation = MaxSystemContextConversation(system_context=system_context)  
user_message = HumanMessage(content="What is the capital of France?")
conversation.add_message(user_message)  

print("current conversation History")
for message in conversation.history:
    print(message.content)


def get_allowed_models(llm):
    failing_llms=[
        "gemma2-9b-it",
        "llama-2-13b-chat",
        "llama-2-70b-chat",
        "llama-3-8b-instruct",
        "llama-3-70b-instruct",
    ]
    return [model for model in llm.allowed_models if model not in failing_llms]

    llm=LLM(apiu_key=API_KEY)
    print(f"Resource:{llm.resource}")
    print(f"Type:{llm.type}")
    print(f"Default Name:{llm.name}")
          
    

# %%
def get_allowed_models(llm):
    failing_llms=[
        "gemma-7b-it",
        "llama-2-13b-chat",
        "llama-2-70b-chat",
        "llama-3-8b-instruct",
        "llama-3-70b-instruct",
    ]
    return [model for model in llm.allowed_models if model not in failing_llms]

    llm=LLM(api_key=API_KEY)
    print(f"Resource:{llm.resource}")
    print(f"Type:{llm.type}")
    print(f"Default Name:{llm.name}")
    
allowed_models= get_allowed_models(llm)
print("Allowed models:", allowed_models)
          

# %%
system_context = "You are a helpful assistant."
conversation = MaxSystemContextConversation(system_context=system_context)
human_message = HumanMessage(content="What is the capital of France?")
conversation.add_message(human_message)

# %%
from swarmauri.llms.concrete.GroqModel import GroqModel as LLM
from swarmauri.conversations.concrete.Conversation import Conversation
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
if API_KEY:
    llm = GroqModel(api_key=API_KEY)
    print("LLM initialized successfully.")
else:
    print("Error: GROQ_API_KEY not found in environment variables. Please set it before running the script.") 
# Use the first allowed model that is not decommissioned
for model in allowed_models:
    if model != "llama-3.1-8b-instant":
        llm.name = model
        break

conversation = Conversation()
input_data = "What is the capital of France?"
human_message = HumanMessage(content=input_data)
conversation.add_message(human_message)
llm.predict(conversation=conversation)
prediction = conversation.get_last().content
print(f"Prediction:{llm.name}: {prediction}")

# %%
from swarmauri.agents.concrete.RagAgent import RagAgent
rag_system_context = "You are a helpful assistant with access to a vector store."
rag_conversation = MaxSystemContextConversation(system_context=rag_system_context)

rag_agent = RagAgent(llm=llm, vector_store=vector_store, conversation=rag_conversation, system_context=rag_system_context)


# %%
queries=[
    "what cloud service do they use?",
    "what database do they use?",
]
for query in queries:
    response= rag_agent.exec(query)
    print(f"Query: {query}\nRAG Response: {response}\n")


