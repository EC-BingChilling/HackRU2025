from elevenlabs import ElevenLabs
from dotenv import load_dotenv
import os

load_dotenv("api.env")


def text_to_speech(text: str) -> str:
    try:
        api_key = os.getenv("ELEVENLABS_API_KEY")
        client = ElevenLabs(api_key=api_key)

        # Choose a default voice
        voice_id = "pNInz6obpgDQGcFmaJgB"  # You can change this later

        # Generate speech
        audio = client.text_to_speech.convert(
            voice_id=voice_id,
            output_format="mp3_44100_128",
            text=text,
            model_id="eleven_turbo_v2",
        )

        # Save the audio file
        file_path = "output.mp3"
        with open(file_path, "wb") as f:
            for chunk in audio:
                f.write(chunk)

        return file_path

    except Exception as e:
        print("ElevenLabs error:", e)
        return f"Error: {e}"
