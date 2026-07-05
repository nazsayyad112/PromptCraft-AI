import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
from prompt_templates import PROMPT_TEMPLATE

load_dotenv()

api_key = st.secrets.get("GEMINI_API_KEY", os.getenv("GEMINI_API_KEY"))

genai.configure(api_key=api_key)

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
            return f"⚠️ Invalid Gemini API key.\n\n{error_message}"

        else:
            return f"⚠️ Something went wrong:\n\n{error_message}"