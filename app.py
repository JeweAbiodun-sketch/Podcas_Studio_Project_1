from newspaper import Article
from utils import ArticleData

def extract_article(url: str) -> ArticleData:
    article = Article(url)
    article.download()
    article.parse()
    
    extracted_data = ArticleData(
        url=url,
        title=article.title,
        text=article.text,
        authors=article.authors,
        publish_date=str(article.publish_date) if article.publish_date else None
    )
    
    return extracted_data
    
# Test it
if __name__ == "__main__":
    # Swapped to a known working URL
    test_url = "https://en.wikipedia.org/wiki/Generative_artificial_intelligence"
    data = extract_article(test_url)
    
    print("Success! Here is the title:")
    print(data.title)

    # Build Gradio Interface
    # Now make a web app so the user can paste a newspaper URL and get results.
    import gradio as gr
from pipeline import create_podcast_from_url

def run_podcast_pipeline(url):
    try:
        article, podcast = create_podcast_from_url(url)

        metadata = f"""
Title: {article.title}

Authors: {', '.join(article.authors) if article.authors else 'Unknown'}

Published: {article.publish_date or 'Unknown'}

Source URL: {article.url}
"""

        return metadata, article.text[:3000], podcast.summary, podcast.script, podcast.audio_path

    except Exception as e:
        return f"Error: {str(e)}", "", "", "", None

with gr.Blocks() as demo:
    gr.Markdown("# AI Podcast Studio from Newspaper URL")
    gr.Markdown("Paste a newspaper article URL to generate a summary, podcast script, and audio.")

    with gr.Row():
        url_input = gr.Textbox(label="Newspaper URL", placeholder="https://...")

    run_btn = gr.Button("Generate Podcast")

    metadata_output = gr.Textbox(label="Article Metadata")
    article_output = gr.Textbox(label="Extracted Article Text")
    summary_output = gr.Textbox(label="Summary")
    script_output = gr.Textbox(label="Podcast Script")
    audio_output = gr.Audio(label="Podcast Audio", type="filepath")

    run_btn.click(
        fn=run_podcast_pipeline,
        inputs=[url_input],
        outputs=[metadata_output, article_output, summary_output, script_output, audio_output]
    )

demo.launch()