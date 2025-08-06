

from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_events(events):
    if not events:
        return "No notable events were detected in the video."

    summary_lines = []
    previous_event = None

    for e in events[:20]:
        frame = e.get("frame", "unknown")
        event = e.get("event", "an event")
        if event != previous_event:
            summary_lines.append(f"At frame {frame}, the event '{event}' occurred.")
            previous_event = event
        else:
            summary_lines.append(f"Later at frame {frame}, the same event '{event}' happened again.")

    return "Video Summary:\n" + "\n".join(summary_lines)
