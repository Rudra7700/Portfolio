import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("GROQ_API_KEY")
models = ["groq/compound", "groq/compound-mini"]

if not API_KEY:
    print("GROQ_API_KEY not found in environment.")
else:
    client = Groq(api_key=API_KEY)
    for model in models:
        print(f"Testing model: {model}")
        try:
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": "Hi"}],
                model=model,
            )
            print(f"Success with {model}!")
            print(chat_completion.choices[0].message.content)
            break
        except Exception as e:
            print(f"Failed with {model}: {e}")
