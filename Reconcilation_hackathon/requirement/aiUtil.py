import openai
from openai import OpenAI

client = OpenAI(
  api_key="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"
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