def clean_article_text(text: str) -> str:
    lines = [line.strip() for line in text.splitlines()]
    lines = [line for line in lines if len(line) > 30]
    return "\n".join(lines)


from dataclasses import dataclass


@dataclass
class ArticleData:
    url: str
    title: str
    text: str
    authors: list
    publish_date: str
@dataclass
class PodcastContent:
    summary: str
    script: str
    audio_path: str 



                

