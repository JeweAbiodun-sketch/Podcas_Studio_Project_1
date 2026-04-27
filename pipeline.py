from scraper import extract_article
from llm_utils import summarize_article, generate_podcast_script
from tts_utils import text_to_speech
from utils import PodcastContent

def create_podcast_from_url(url: str) -> tuple:
    article = extract_article(url)

    if not article.text.strip():
        raise ValueError("Could not extract article text from the provided URL.")

    summary = summarize_article(article.title, article.text)
    script = generate_podcast_script(article.title, article.text)
    audio_path = text_to_speech(script)

    podcast = PodcastContent(
        summary=summary,
        script=script,
        audio_path=audio_path
    )

    return article, podcast