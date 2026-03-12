from ultralytics import YOLO
from PIL import Image
import cv2

# Load model
model = YOLO("yolov8n.pt")

# Run detection
results = model("images/plastic.jpg")

# Get annotated image
annotated = results[0].plot()

# Save result
cv2.imwrite("detection_result.jpg", annotated)

# Display info
if len(results[0].boxes) > 0:
    boxes = results[0].boxes
    for i, box in enumerate(boxes):
        cls = int(box.cls[0])
        conf = float(box.conf[0])
        name = results[0].names[cls]
        print(f"Detected: {name} (Confidence: {conf:.2%})")
else:
    print("No objects detected")

print("\nResult saved to detection_result.jpg")
