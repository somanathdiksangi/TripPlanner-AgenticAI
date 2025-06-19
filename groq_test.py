from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq()
completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=False,
    response_format={"type": "json_object"},
    stop=None,
)

print(completion.choices[0].message)
