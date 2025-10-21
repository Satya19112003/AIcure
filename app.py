import gradio as gr
from doctor.diagnosis import process_inputs

iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Textbox(label="Describe Your Symptoms", placeholder="e.g., I have a rash on my arm"),
        gr.Image(type="filepath", label="Upload Image (Optional)")
    ],
    outputs=[
        gr.Textbox(label="Doctor's Response"),
        gr.Audio(label="Doctor's Audio Response")
    ],
    title="🩺 AIcura - Your AI Health Assistant"
)

if __name__ == "__main__":
    iface.launch(debug=True)
