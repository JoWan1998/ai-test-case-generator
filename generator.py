from groq import Groq
from prompts import build_user_prompt, get_system_prompt
import os
from dotenv import load_dotenv

load_dotenv()

def generate_test_cases(feature_description: str,
                        language: str = "Español",
                        model: str = "llama-3.3-70b-versatile") -> str:
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": get_system_prompt(language)},
            {"role": "user",   "content": build_user_prompt(feature_description)},
        ],
        reasoning_format="hidden",
        temperature=0.3,
        max_tokens=2000,
    )
    
    return response.choices[0].message.content