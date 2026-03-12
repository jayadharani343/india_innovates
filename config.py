# Configuration file for AI Waste Recognition System

# Model Configuration
MODEL_PATH = "yolov8n-cls.pt"
TRAINED_MODEL_PATH = "runs/classify/waste_classifier/weights/best.pt"

# Waste Categories
WASTE_CATEGORIES = {
    0: "Biodegradable",
    1: "Recyclable",
    2: "Waste"
}

# Category Colors (for dashboard)
CATEGORY_COLORS = {
    "Biodegradable": "#10b981",  # Green
    "Recyclable": "#3b82f6",     # Blue
    "Waste": "#ef4444"           # Red
}

# Dataset Configuration
DATASET_PATH = "dataset"
CATEGORIES = ["biodegradable", "recyclable", "waste"]

# Training Configuration
EPOCHS = 50
IMAGE_SIZE = 224
BATCH_SIZE = 16

# Dashboard Configuration
PAGE_TITLE = "AI Waste Recognition"
PAGE_ICON = "♻️"
LAYOUT = "wide"

# Temporary Files
TEMP_IMAGE_PATH = "temp_image.jpg"

# Supported Image Formats
SUPPORTED_FORMATS = ['jpg', 'jpeg', 'png']
