from groq import Groq
from prompts import SYSTEM_PROMPT, build_user_prompt
import os
from dotenv import load_dotenv

load_dotenv()

def generate_test_cases(feature_description: str, 
                         format_type: str = "Estándar",
                         model: str = "llama3-8b-8192") -> str:
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": build_user_prompt(
                feature_description, format_type
            )}
        ],
        temperature=0.3,  # Bajo = más consistente
        max_tokens=2000,
    )
    
    return response.choices[0].message.content