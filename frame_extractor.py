import cv2

def extract_frames(video_path, sample_rate=1):

    frames = []

    #to open the vedeo file
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Cannot open video file: {video_path}")
        return frames

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    if fps <= 0:
        fps = 25  

    frame_interval = int(fps * sample_rate)
    count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if count % frame_interval == 0:
            frames.append(frame)
        count += 1

    cap.release()
    return frames
