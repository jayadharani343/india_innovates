# AI-Driven Circular Waste Intelligence System

## Project Summary

The AI-Driven Circular Waste Intelligence System is a software-focused smart waste management prototype designed to improve urban waste segregation and collection efficiency. The system uses computer vision (YOLO-based object detection) to automatically identify waste types such as biodegradable, recyclable, and hazardous materials.

Smart bin data is simulated through IoT integration and processed via a cloud-based backend. The platform provides real-time analytics through a dashboard, enabling optimized waste collection routes and better decision-making for municipal authorities. Additionally, a citizen reward concept encourages proper waste segregation practices.

This prototype demonstrates how AI, data analytics, and intelligent routing can support scalable circular economy solutions for smarter and more sustainable cities.

## Features

- 🤖 **AI-Powered Waste Classification** - Uses YOLOv8 object detection to identify and classify waste items
- 🌱 **Three Category Classification** - Biodegradable, Recyclable, and General Waste
- 📊 **Real-time Analytics Dashboard** - Visual insights into waste collection and segregation patterns
- 📈 **Trend Analysis** - Weekly, monthly, and hourly waste classification trends
- 🎯 **High Accuracy Detection** - Leverages pre-trained YOLO models for reliable object recognition
- 💡 **Smart Recommendations** - Provides disposal guidance based on waste type
- 🖼️ **Visual Detection Results** - Shows bounding boxes and confidence scores

## Technology Stack

- **Frontend**: Streamlit
- **AI/ML**: YOLOv8 (Ultralytics)
- **Data Visualization**: Plotly
- **Image Processing**: OpenCV, PIL
- **Backend**: Python 3.14

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. **Clone the repository**
```bash
git clone <repository-url>
cd "india innovates/india innovates"
```

2. **Install required packages**
```bash
pip install streamlit pandas plotly pillow ultralytics opencv-python
```

3. **Fix protobuf compatibility (if using Python 3.14)**
```bash
pip install "protobuf<7,>=3.20"
```

4. **Verify YOLO model exists**
- Ensure `yolov8n.pt` is in the project directory
- The model will be downloaded automatically on first run if not present

## Running the Application

### Start the Streamlit App

```bash
python -m streamlit run app.py
```

The application will automatically open in your default browser at `http://localhost:8501`

### Alternative Method

```bash
streamlit run app.py
```

## Usage Guide

### 1. Dashboard Page (📊)
- View overall waste classification statistics
- Monitor real-time metrics and trends
- Analyze waste distribution patterns
- Track weekly classification trends
- Review hourly collection rates

### 2. Classify Waste Page (🔍)
- Upload an image of waste item (JPG, JPEG, PNG)
- Click "Classify Waste" button
- View detection results with bounding boxes
- See waste category and confidence score
- Get disposal recommendations

### 3. Analytics Page (📈)
- Detailed monthly statistics
- Recent classification history
- Environmental impact metrics
- Recycling rate tracking

## Project Structure

```
india innovates/
├── app.py                    # Main Streamlit application
├── waste_classifier.py       # YOLO-based waste classification logic
├── config.py                 # Configuration settings
├── test_detection.py         # Testing script for YOLO detection
├── yolov8n.pt               # YOLOv8 detection model
├── yolov8n-cls.pt           # YOLOv8 classification model (optional)
├── images/                   # Sample images for testing
│   ├── plastic.jpg
│   └── banana-peel.avif
├── requirements.txt          # Python dependencies
└── README.md                # Project documentation
```

## Waste Classification Categories

### 🌱 Biodegradable
- Food items (fruits, vegetables, cooked food)
- Organic materials
- Natural waste that decomposes

**Disposal**: Compost or green bins

### ♻️ Recyclable
- Plastic bottles and containers
- Glass items
- Metal objects
- Paper and cardboard
- Electronic items

**Disposal**: Recycling bins (clean and dry)

### 🗑️ General Waste
- Non-recyclable materials
- Mixed waste
- Contaminated items

**Disposal**: General waste bins

## How It Works

1. **Image Upload**: User uploads an image of waste item
2. **YOLO Detection**: YOLOv8 model detects objects in the image
3. **Classification**: Detected objects are mapped to waste categories
4. **Visualization**: Results displayed with bounding boxes and labels
5. **Recommendations**: System provides disposal guidance

## Model Information

- **Base Model**: YOLOv8n (Nano) - Optimized for speed and accuracy
- **Detection Classes**: 80 COCO dataset classes
- **Custom Mapping**: Objects mapped to 3 waste categories
- **Confidence Threshold**: Displays highest confidence detection

## Configuration

Edit `config.py` to customize:

- Model paths
- Waste categories
- Category colors
- Image formats
- Training parameters

## Testing

Test the detection system independently:

```bash
python test_detection.py
```

This will process `images/plastic.jpg` and save the result to `detection_result.jpg`

## Troubleshooting

### Model Not Loading
- Ensure `yolov8n.pt` exists in the project directory
- Check internet connection (model downloads automatically)
- Verify ultralytics package is installed

### Protobuf Errors (Python 3.14)
```bash
pip install "protobuf<7,>=3.20"
```

### Streamlit Not Found
```bash
pip install streamlit
# or
python -m pip install streamlit
```

### No Objects Detected
- Ensure image is clear and well-lit
- Try different angles or closer shots
- Verify the object is in YOLO's training classes

## Future Enhancements

- 🔄 Real-time video stream classification
- 📱 Mobile application integration
- 🗺️ Route optimization for waste collection
- 🏆 Citizen reward system implementation
- 📡 IoT sensor integration for smart bins
- 🌐 Multi-language support
- 📊 Advanced analytics and reporting
- 🔐 User authentication and profiles

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is developed as part of the India Innovates initiative.

## Contact

For questions or support, please open an issue in the repository.

---

**Made with ♻️ for a Greener Future | Powered by YOLOv8 & Streamlit**
