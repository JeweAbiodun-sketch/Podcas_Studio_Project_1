import os
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()

def text_to_speech(text: str, output_path: str = "output.mp3"):
    print("Generating audio via OpenAI...")
    
    # Use OpenAI's tts-1 model to generate the speech
    response = client.audio.speech.create(
        model="tts-1", 
        voice="alloy", # You can change this to: echo, fable, onyx, nova, or shimmer
        input=text
    )
    
    # Save the audio to the output path
    response.stream_to_file(output_path)
    print(f"Audio saved successfully to {output_path}")
    
    return output_path