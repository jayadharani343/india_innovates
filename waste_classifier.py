from ultralytics import YOLO
from PIL import Image
import os
import config

class WasteClassifier:
    def __init__(self, model_path=None):
        """Initialize waste classifier"""
        try:
            # Try trained model first, fallback to base model
            if model_path is None:
                if os.path.exists(config.TRAINED_MODEL_PATH):
                    model_path = config.TRAINED_MODEL_PATH
                    self.use_detection = False
                else:
                    # Use detection model for better results
                    model_path = "yolov8n.pt"  # Detection model
                    self.use_detection = True
            else:
                self.use_detection = False
            
            self.model = YOLO(model_path)
            self.categories = config.WASTE_CATEGORIES
            
            # Mapping from COCO classes to waste categories
            self.waste_mapping = {
                # Biodegradable items
                'banana': 'Biodegradable',
                'apple': 'Biodegradable',
                'orange': 'Biodegradable',
                'broccoli': 'Biodegradable',
                'carrot': 'Biodegradable',
                'hot dog': 'Biodegradable',
                'pizza': 'Biodegradable',
                'donut': 'Biodegradable',
                'cake': 'Biodegradable',
                'sandwich': 'Biodegradable',
                
                # Recyclable items
                'bottle': 'Recyclable',
                'wine glass': 'Recyclable',
                'cup': 'Recyclable',
                'fork': 'Recyclable',
                'knife': 'Recyclable',
                'spoon': 'Recyclable',
                'bowl': 'Recyclable',
                'laptop': 'Recyclable',
                'mouse': 'Recyclable',
                'keyboard': 'Recyclable',
                'cell phone': 'Recyclable',
                'book': 'Recyclable',
                'clock': 'Recyclable',
                'vase': 'Recyclable',
                'scissors': 'Recyclable',
                'teddy bear': 'Recyclable',
                'toothbrush': 'Recyclable',
                
                # General waste
                'chair': 'Waste',
                'couch': 'Waste',
                'bed': 'Waste',
                'toilet': 'Waste',
                'sink': 'Waste',
            }
            
        except Exception as e:
            raise Exception(f"Failed to load model: {e}")
    
    def classify(self, image_path):
        """Classify waste image"""
        if not os.path.exists(image_path):
            return "Unknown", None, 0.0
        
        try:
            results = self.model(image_path, verbose=False)
            
            if self.use_detection:
                # Using detection model - map detected objects to waste categories
                if len(results[0].boxes) == 0:
                    return "Unknown", None, 0.0
                
                # Get the most confident detection
                boxes = results[0].boxes
                confidences = boxes.conf.cpu().numpy()
                classes = boxes.cls.cpu().numpy()
                
                max_conf_idx = confidences.argmax()
                detected_class = int(classes[max_conf_idx])
                confidence = float(confidences[max_conf_idx])
                
                # Get class name
                class_name = results[0].names[detected_class]
                
                # Map to waste category
                category = self.waste_mapping.get(class_name, 'Waste')
                
                return category, detected_class, confidence
            else:
                # Using trained classification model
                probs = results[0].probs
                if probs is None:
                    return "Unknown", None, 0.0
                
                top_class = int(probs.top1)
                confidence = float(probs.top1conf.item())
                
                category = self.categories.get(top_class, "Unknown")
                
                return category, top_class, confidence
                
        except Exception as e:
            print(f"Classification error: {e}")
            return "Unknown", None, 0.0
    
    def classify_batch(self, image_paths):
        """Classify multiple images"""
        results = []
        for img_path in image_paths:
            category, class_id, conf = self.classify(img_path)
            results.append({
                "image": img_path,
                "category": category,
                "confidence": conf
            })
        return results

if __name__ == "__main__":
    classifier = WasteClassifier()
    
    # Test with sample image
    test_image = "test_image.jpg"
    if os.path.exists(test_image):
        category, _, confidence = classifier.classify(test_image)
        print(f"Category: {category}")
        print(f"Confidence: {confidence:.2%}")
