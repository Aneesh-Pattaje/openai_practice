import openai
from openai import OpenAI

client = OpenAI(
  api_key=""
)

def generate_output(input):
    messages= [
        {
            "role" : "System",
            "content" : """As a Product Description Generator, Generate multi paragraph rich text product description with emojis from the information provided to you' \n"""

        }
    ]
    messages.append({"role": "user", "content" : f"{input}"})
    completion = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        store = True,
        messages = messages
    )
    reply = completion.choices[0].message
    return reply
