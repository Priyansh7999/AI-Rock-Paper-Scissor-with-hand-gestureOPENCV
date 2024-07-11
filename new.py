import openai
import os
from openai import OpenAI

# Load your API key from an environment variable or secret management service"

OPENAI_API_KEY = ("OPEN AI KEY")

# Set the environment variable
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Initialize the OpenAI client (it will automatically use the OPENAI_API_KEY environment variable)
client = OpenAI()
def chatbot():
    # Create a list to store all the messages for context
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
    ]

    # Keep repeating the following
    while True:
        # Prompt user for input
        message = input("User: ")

        # Exit program if user inputs "quit"
        if message.lower() == "quit":
            break

        # Add user message to the messages list
        messages.append({"role": "user", "content": message})

        # Get response from OpenAI API
        response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=message,
        max_tokens=256,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,  
    )

        # Print the response and add it to the messages list
        chat_message = response['choices'][0]['message']['content']
        print(f"Bot: {chat_message}")
        messages.append({"role": "assistant", "content": chat_message})

if __name__ == "__main__":
    print("Start chatting with the bot (type 'quit' to stop)!")
    chatbot()
