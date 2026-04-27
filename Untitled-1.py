import requests
from bs4 import BeautifulSoup
from newspaper import Article
from utils import ArticleData

def extract_with_newspaper(url: str):
    article = Article(url)
    article.download()
    article.parse()

    return ArticleData(
        url=url,
        title=article.title or "Untitled Article",
        text=article.text or "",
        authors=article.authors or [],
        publish_date=str(article.publish_date) if article.publish_date else None
    )

def extract_with_bs4(url: str):
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string.strip() if soup.title else "Untitled Article"

    paragraphs = soup.find_all("p")
    text = "\n".join(p.get_text(strip=True) for p in paragraphs)

    return ArticleData(
        url=url,
        title=title,
        text=text,
        authors=[],
        publish_date=None
    )

def extract_article(url: str) -> ArticleData:
    try:
        article = extract_with_newspaper(url)
        if article.text.strip():
            return article
    except Exception:
        pass

    return extract_with_bs4(url)