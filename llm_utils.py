import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_article(title: str, article_text: str) -> str:
    prompt = f"""
You are a news editor.
Summarize the following article clearly and accurately in 5-7 bullet points.

Title: {title}

Article:
{article_text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You summarize news articles accurately."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content

def generate_podcast_script(title: str, article_text: str) -> str:
    prompt = f"""
Turn the following news article into a short podcast script.

Requirements:
- conversational but informative tone
- around 2 to 4 minutes long
- include an engaging intro
- explain key events clearly
- end with a short closing takeaway
- do not invent facts

Title: {title}

Article:
{article_text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You write factual podcast scripts from news content."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5
    )

    return response.choices[0].message.content