import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import os

def generate_heatmap(events, save_path="static/heatmaps/violation_heatmap.png"):
    
    frame_nums = [e['frame'] for e in events if 'frame' in e]

    
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

   
    plt.figure(figsize=(10, 4))
    plt.hist(frame_nums, bins=20, color='red', edgecolor='black')
    plt.title("Violation/Event Heatmap")
    plt.xlabel("Frame Buckets")
    plt.ylabel("Event Count")
    plt.tight_layout()

    
    plt.savefig(save_path)
    plt.close()

  
    return Image.open(save_path).convert("RGB")
