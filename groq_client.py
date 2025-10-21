from groq import Groq
from config import GROQ_API_KEY

def analyze_with_groq(query, encoded_image=None, model="llama-3.2-11b-vision-preview"):
    try:
        client = Groq(api_key=GROQ_API_KEY)
        messages = [{"role": "user", "content": [{"type": "text", "text": query}]}]

        if encoded_image:
            messages[0]["content"].append({
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}
            })

        chat_completion = client.chat.completions.create(messages=messages, model=model)
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Analysis Error: {str(e)}"
