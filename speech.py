from gtts import gTTS

def text_to_speech_with_gtts(input_text, output_filepath="response.mp3"):
    try:
        audioobj = gTTS(text=input_text, lang="en", slow=False)
        audioobj.save(output_filepath)
        return output_filepath
    except Exception as e:
        return f"Text-to-Speech Error: {str(e)}"
