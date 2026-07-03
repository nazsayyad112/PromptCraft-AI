import os
import google.generativeai as genai
from dotenv import load_dotenv
from prompt_templates import PROMPT_TEMPLATE

# Load API key from .env
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")


def optimize_prompt(user_prompt, category, tone, length):

    prompt = PROMPT_TEMPLATE.format(
        user_prompt=user_prompt,
        category=category,
        tone=tone,
        length=length
    )

    response = model.generate_content(prompt)

    return response.text