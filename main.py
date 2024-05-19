import cv2
from ultralytics import YOLO
import pyttsx3

# Initialize TTS engine
tts_engine = pyttsx3.init()
tts_engine.setProperty('rate', 150)  # You can adjust the speech rate if needed

# Load the YOLOv8 model
model = YOLO('models/best2.pt')

# Load class names
class_names = model.names  # Assuming the model has a 'names' attribute containing class names

# Replace with your phone's IP address and port
url = "http://xxx.xxx.xxx.xxx:8080/video"

# Open video stream
cap = cv2.VideoCapture(url)

if not cap.isOpened():
    print("Error: Could not open video stream")
    exit()

# Get the width and height of the frames from the video stream
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('videos/output.avi', fourcc, 20.0, (frame_width, frame_height))

previous_objects = set()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame")
        break
    
    # Run YOLOv8 model on the frame
    results = model(frame)
    
    detected_objects = set()

    # Assuming results is a list, iterate through each result
    if isinstance(results, list):
        for result in results:
            # Plot the results
            annotated_frame = result.plot()
            # Collect detected object names
            for box in result.boxes:
                class_idx = int(box.cls)
                class_name = class_names[class_idx]
                detected_objects.add(class_name)
    else:
        annotated_frame = results.plot()
        # Collect detected object names
        for box in results.boxes:
            class_idx = int(box.cls)
            class_name = class_names[class_idx]
            detected_objects.add(class_name)
    
    # Announce detected objects using TTS if there are new detections
    new_objects = detected_objects - previous_objects
    if new_objects:
        announcement = "Detectant: " + ", ".join(new_objects)
        tts_engine.say(announcement)
        tts_engine.runAndWait()
        previous_objects = detected_objects

    # Write the frame into the file 'output.avi'
    out.write(annotated_frame)

    # Display the frame
    cv2.imshow('YOLOv8 Segmentation', annotated_frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and video write objects and close display windows
cap.release()
out.release()
cv2.destroyAllWindows()

