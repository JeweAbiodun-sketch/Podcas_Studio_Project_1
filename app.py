import gradio as gr
from newspaper import Article
from utils import ArticleData
from pipeline import create_podcast_from_url

# --- 1. Article Extraction ---
def extract_article(url: str) -> ArticleData:
    try:
        article = Article(url)
        article.download()
        article.parse()
        
        return ArticleData(
            url=url,
            title=article.title,
            text=article.text,
            authors=article.authors,
            publish_date=str(article.publish_date) if article.publish_date else None
        )
    except Exception as e:
        # Raise a standard exception that the pipeline can catch
        raise ValueError(f"Failed to extract article from {url}. Error: {str(e)}")

# --- 2. Pipeline wrapper with Progress Bar ---
# Notice we added `progress=gr.Progress()` here
def run_podcast_pipeline(url, progress=gr.Progress()):
    if not url.strip():
        raise gr.Error("Please enter a valid URL.")
        
    try:
        # Tell the user what the app is doing
        progress(0.1, desc="Downloading & parsing article...")
        
        # NOTE: If your `create_podcast_from_url` takes a long time, 
        # it will run here. 
        progress(0.4, desc="Reading article and generating podcast script...")
        article, podcast = create_podcast_from_url(url)

        progress(0.9, desc="Finalizing metadata and UI...")
        
        metadata = f"""Title: {article.title}
Authors: {', '.join(article.authors) if getattr(article, 'authors', None) else 'Unknown'}
Published: {getattr(article, 'publish_date', 'Unknown') or 'Unknown'}
Source URL: {article.url}"""

        return metadata, article.text[:3000], podcast.summary, podcast.script, podcast.audio_path

    except Exception as e:
        # gr.Error creates a nice red popup in the UI instead of breaking the text boxes
        raise gr.Error(f"Error generating podcast: {str(e)}")


# --- 3. Gradio Interface ---
# Adding a theme makes it look more modern out-of-the-box
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🎙️ AI Podcast Studio")
    gr.Markdown("Paste a news article URL to generate a summary, a conversational podcast script, and an audio file.")

    with gr.Row():
        url_input = gr.Textbox(
            label="Newspaper URL", 
            placeholder="https://en.wikipedia.org/wiki/Generative_artificial_intelligence",
            scale=4 # Takes up 80% of the row
        )
        run_btn = gr.Button("Generate Podcast", variant="primary", scale=1) # Takes up 20%

    # Add clickable examples so users can test immediately
    gr.Examples(
        examples=[
            ["https://en.wikipedia.org/wiki/Generative_artificial_intelligence"],
            ["https://en.wikipedia.org/wiki/SpaceX_Starship"]
        ],
        inputs=url_input
    )

    # Reorganizing the layout into two columns for a cleaner dashboard look
    with gr.Row():
        # Left Column: Inputs & Raw Data
        with gr.Column(scale=1):
            metadata_output = gr.Textbox(label="Article Metadata", lines=4)
            article_output = gr.Textbox(label="Extracted Article Text (Preview)", lines=15)
            
        # Right Column: The AI Output
        with gr.Column(scale=1):
            audio_output = gr.Audio(label="Podcast Audio", type="filepath")
            summary_output = gr.Textbox(label="Summary", lines=3)
            script_output = gr.Textbox(label="Podcast Script", lines=10)

    # Wire up the button
    run_btn.click(
        fn=run_podcast_pipeline,
        inputs=[url_input],
        outputs=[metadata_output, article_output, summary_output, script_output, audio_output]
    )

if __name__ == "__main__":
    demo.launch()