# IMPORT NECESSARY LIBRARIES AND API KEYS
import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

load_dotenv()

openai_api_key = os.environ["OPENAI_API_KEY"]

# CREATE THE CHATBOT AND CHOOSE A MODEL/SETTINGS
chatbot = ChatOpenAI(
    openai_api_key=openai_api_key,
    model='gpt-3.5-turbo'
)

# COME UP WITH THE MESSAGES THAT YOU WANT TO SEND THE CHATBOT
messages = [
    SystemMessage(content="You are a overly cheerful assistant."),
    HumanMessage(content="Who are you?")
]

# GET INITIAL INTRODUCTION OF CHATBOT
response = chatbot(messages)
print(response.content + "\n")
messages.append(response)

# MAKE A LOOP SO YOU CAN KEEP ASKING IT QUESTIONS
question = input('Ask the chatbot a question: ')

while (question != "exit"):
    messages.append(HumanMessage(content=question))
    response = chatbot(messages)
    print("\nChatbot response: ", response.content)
    messages.append(response)

    question = input('\nAsk the chatbot a question: ')

# DONE WITH THE CHATBOT, SAY GOODBYE
print("\nHave a good day!")
print(messages)