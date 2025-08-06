import cv2

def process_video(video_path, sample_rate=1, max_frames=30):
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frames = []
    count = 0
    while cap.isOpened() and len(frames) < max_frames:
        ret, frame = cap.read()
        if not ret:
            break
        if count % (fps * sample_rate) == 0:
            frames.append(frame)
        count += 1
    cap.release()
    return frames
