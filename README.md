# --video-chat-assistant
EduVision – Visual Understanding Chat Assistant AI-powered assistant that analyzes short videos to detect events, summarize content, generate heatmaps, and support multi-turn conversations through a chat interface.  
🚀 Built with DETR, OpenCV, LangChain, and Gradio.

Team name - HACKHIVE

📁 Submitted to: https://github.com/MantraHackathon

# PROJECT OVERVIEW
This project presents a Visual Understanding Chat Assistant that accepts a short video input (up to 2 minutes) and performs intelligent scene analysis to deliver the following:
1. Object Detection using the DETR (DEtection TRansformer) model to identify entities such as people, motorcycles, and other visual elements within frames.
2. Event Logging that records detected objects with corresponding timestamps for clear traceability.
3. Violation/Event Heatmap to highlight segments of the video with frequent or notable detections.
4. Automated PDF Report generation summarizing the detected events along with the heatmap visualization.
5. Interactive Chat Assistant powered by LangChain, enabling users to ask context-based questions about the video and receive relevant responses.
6. Keyword Search Capability for quickly locating specific objects or events within the analyzed summary.
   
All results are delivered through an intuitive and user-friendly Gradio interface, making interaction seamless and effective.

# ARCHITECTURE DIAGRAM

<img width="800" height="800" alt="image" src="https://github.com/user-attachments/assets/bbbef85d-99fd-4e80-99bc-1cb0becc9003" />


# TECH STACK

| Component                 | Technology Used                 | Justification                                                                                                                                          |
| ------------------------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Object Detection**      | `facebook/detr-resnet-50`       | DETR is a transformer-based model used to detect visual elements in frames. It supports a wide range of objects and performs well on the COCO dataset. |
| **Video Processing**      | `OpenCV`                        | Used to extract frames efficiently from the uploaded video for further analysis.                                                                       |
| **Summarization & Chat**  | `LangChain` + `Ollama (LLaMA3)` | Enables multi-turn conversational memory and response generation based on the detected video events.                                                   |
| **Frontend Interface**    | `Gradio`                        | Provides a user-friendly interface to upload videos, view outputs, and interact with the assistant.                                                    |
| **PDF Report Generator**  | `ReportLab`                     | Generates downloadable summaries of the video analysis in PDF format.                                                                                  |
| **Heatmap Visualization** | `Matplotlib`                    | Creates a visual heatmap showing which frames had more frequent detections.                                                                            |
| **Search Functionality**  | Custom Python logic             | Allows users to search for specific keywords within the generated summary.                                                                             |


# SETUP AND INSTALLATION INSTRUCTIONS

Prerequisites:-

* Python 3.10 or above
* Internet connection to download model weights
* A short .mp4 video file (less than 2 minutes)

Step-by-Step Installation:-

1. Clone the Repository
   
git clone https://github.com/yourusername/eduvision-video-chat-assistant.git
cd eduvision-video-chat-assistant

2. Create and Activate Virtual Environment

* On Windows:

python -m venv venv
venv\Scripts\activate

* On Mac/Linux:

python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
   
pip install -r requirements.txt

required packages:-
* gradio
* opencv-python
* transformers
* torch
* torchvision
* matplotlib
* reportlab
* langchain
* moviepy
* tiktoken

4. Run the App
   
 python gradio_app.py

5. Launch Interface

# USAGE INSTRUCTIONS 

1. Upload a Video (.mp4, max 2 mins)

   * Example: Classroom or outdoor scene with people or vehicles.

2. Automatic Analysis

   * Detects objects like person, car, motorcycle, etc.

   * Generates event logs with timestamps.

3. View Output

   * See text summary of detections.

   * View heatmap highlighting active frames.

   * Download PDF report.

4. Chat with Assistant

Ask:

“What happened in the middle of the video?”

“Was any motorcycle detected?”

Get context-aware answers from the assistant.

Search Summary

Enter keywords (e.g., car) to find related events quickly.











