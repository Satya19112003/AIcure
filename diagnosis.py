from .image_utils import encode_image
from .groq_client import analyze_with_groq
from .speech import text_to_speech_with_gtts

system_prompt = """You have to act as a professional doctor, I know you are not, but this is for learning purposes.
With what I see, I think you have .... If you make a differential, suggest some remedies for them.
Do not add any numbers or special characters in your response. Your response should be in one long paragraph.
Always answer as if you are talking to a real person. Do not respond as an AI model in markdown;
your answer should mimic that of an actual doctor, not an AI bot. Keep your answer concise (max 2 sentences).
No preamble, start your answer right away please."""

def process_inputs(text_input, image_filepath=None):
    if not text_input or text_input.strip() == "":
        return "Please describe your symptoms to proceed.", None

    query = system_prompt + " " + text_input

    if image_filepath:
        encoded_image = encode_image(image_filepath)
        if "Image Encoding Error" in encoded_image:
            return encoded_image, None
        doctor_response = analyze_with_groq(query, encoded_image)
    else:
        doctor_response = analyze_with_groq(query)

    if "Analysis Error" in doctor_response:
        return doctor_response, None

    audio_output_path = text_to_speech_with_gtts(doctor_response)
    if "Text-to-Speech Error" in audio_output_path:
        return doctor_response, None

    return doctor_response, audio_output_path
