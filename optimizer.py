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

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:

        error_message = str(e)

        if "429" in error_message or "quota" in error_message.lower():
            return "⚠️ Gemini API quota exceeded. Please wait about a minute and try again."

        elif "API_KEY" in error_message or "api key" in error_message.lower():
            return "⚠️ Invalid Gemini API key. Please check your .env file."

        else:
            return f"⚠️ Something went wrong:\n\n{error_message}"