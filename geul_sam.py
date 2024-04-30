import gradio as gr

def generate_welcome_message(name, color):
    return f"Welcome to Gradio, {name}! Your favorite color is {color}."

with gr.Blocks() as demo:
    gr.Markdown("# Hello World!\nStart typing below to see the output.")
    
    
    name_input = gr.Textbox(label="Enter your name", placeholder="Your name")
    color_input = gr.Textbox(label="Enter your favorite color", placeholder="Your favorite color")
    
    submit_button = gr.Button("Submit")
    
    output = gr.Textbox(label="Welcome Message")
    
    submit_button.click(
        fn=generate_welcome_message, 
        inputs=[name_input, color_input],
        outputs=output
    )

if __name__ == "__main__":
    demo.launch()
