import cv2
from transformers import AutoModelForObjectDetection, AutoImageProcessor
from PIL import Image
import torch

processor = AutoImageProcessor.from_pretrained("facebook/detr-resnet-50")
model = AutoModelForObjectDetection.from_pretrained("facebook/detr-resnet-50")
id2label = model.config.id2label

def recognize_events(frames):
    events = []
    for i, frame in enumerate(frames):
        inputs = processor(images=frame, return_tensors="pt")
        outputs = model(**inputs)
        height, width = frame.shape[:2]
        target_sizes = torch.tensor([[height, width]])
        results = processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.9)[0]

        for score, label_id, box in zip(results["scores"], results["labels"], results["boxes"]):
            label = id2label.get(label_id.item(), f"Unknown_{label_id.item()}")
            event = {
                "frame": i,
                "event": label,
                "confidence": round(score.item(), 2),
                "bbox": [round(x.item(), 2) for x in box]
            }
            events.append(event)

    return events
