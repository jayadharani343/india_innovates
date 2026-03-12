from ultralytics import YOLO
import os
import config

def train_waste_classifier():
    """Train YOLOv8 model for waste classification"""
    
    # Verify dataset structure
    if not os.path.exists(config.DATASET_PATH):
        print(f"Error: Dataset not found at {config.DATASET_PATH}")
        return None
    
    # Check if categories exist
    for category in config.CATEGORIES:
        cat_path = os.path.join(config.DATASET_PATH, category)
        if not os.path.exists(cat_path):
            print(f"Error: Category folder '{category}' not found")
            return None
        
        # Count images
        images = [f for f in os.listdir(cat_path) if f.endswith(('.jpg', '.jpeg', '.png'))]
        print(f"Found {len(images)} images in '{category}' category")
    
    print("\nStarting model training...")
    
    # Load pretrained YOLOv8 model
    model = YOLO(config.MODEL_PATH)
    
    # Train the model
    results = model.train(
        data=config.DATASET_PATH,
        epochs=config.EPOCHS,
        imgsz=config.IMAGE_SIZE,
        batch=config.BATCH_SIZE,
        name="waste_classifier",
        patience=10,
        save=True,
        plots=True
    )
    
    print("\n✓ Training complete!")
    print("Model saved to: runs/classify/waste_classifier/weights/best.pt")
    
    return model

if __name__ == "__main__":
    if not os.path.exists(config.DATASET_PATH):
        print("Error: Dataset not found. Run download_dataset.py first.")
    else:
        train_waste_classifier()
