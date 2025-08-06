import gradio as gr
import warnings
warnings.filterwarnings("ignore")  
from dotenv import load_dotenv
load_dotenv()
from video_processor import process_video
from event_recognition import recognize_events
from summarizer import summarize_events
from chatbot import handle_chat, init_chat_memory
from heatmap_generator import generate_heatmap
from report_generator import generate_pdf_report
from search_module import search_summary
from frame_extractor import extract_frames  
from PIL import Image
import numpy as np
summary_cache = ""


def handle_video(video):
    global summary_cache  
    frames = extract_frames(video)
    if not frames:
        return "No frames extracted from the video.", None, None
    events = recognize_events(frames)
    if not events:
        dummy_image = Image.fromarray(np.zeros((480, 640, 3), dtype=np.uint8)) 
        return (
            "No meaningful events found.",
            dummy_image,
            None
        )

    
    video_summary = summarize_events(events)
    summary_cache = video_summary 
    

    
    heatmap_image = generate_heatmap(events)
    summary_file_path = generate_pdf_report(video_summary, events)

    return video_summary, heatmap_image, summary_file_path



def handle_question(message):
    return handle_chat(message, summary_cache)

def handle_search(query):
    return search_summary(summary_cache, query)

with gr.Blocks() as demo:
    gr.Markdown("# 🎥 Agentic Video Chat Assistant")

    video_input = gr.Video(label="Upload Video")
    summary_output = gr.Textbox(label="Video Summary")
    heatmap_output = gr.Image(label="Violation Heatmap")
    report_output = gr.File(label="Download PDF Report")

    chat_input = gr.Textbox(label="Ask the Assistant")
    chat_response = gr.Textbox(label="Assistant's Response")

    search_input = gr.Textbox(label="Search in Summary")
    search_output = gr.Textbox(label="Search Result")

    
    video_input.change(fn=handle_video, inputs=video_input, outputs=[summary_output, heatmap_output, report_output])
    chat_input.change(fn=handle_question, inputs=chat_input, outputs=chat_response)
    search_input.change(fn=handle_search, inputs=search_input, outputs=search_output)

print("\n\n🚀 Starting Agentic Video Chat Assistant...")
demo.launch(share=True)
