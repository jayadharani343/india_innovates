# AI Waste Recognition System

An intelligent waste classification system using YOLOv8 to identify and categorize waste into three types:
- 🌱 Biodegradable (cardboard, paper, organic waste)
- ♻️ Recyclable (glass, metal, plastic)
- 🗑️ Waste (general trash)

## Features

- ✅ Real-time waste classification using YOLOv8
- ✅ Interactive dashboard with metrics and analytics
- ✅ Beautiful gradient theme
- ✅ Upload and classify images
- ✅ Detailed analytics and trends
- ✅ Environmental impact tracking
- ✅ Uses TrashNet dataset for training

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Download Training Data (Optional)
```bash
python download_dataset.py
```
This downloads the TrashNet dataset from GitHub.

### 3. Train Model (Optional)
```bash
python train_model.py
```
Trains a custom model on the downloaded dataset.

### 4. Run Dashboard
```bash
streamlit run app.py
```

## How It Works

### Without Training (Default)
- Uses YOLOv8 object detection model
- Detects objects in images (bottles, food, etc.)
- Maps detected objects to waste categories
- Works immediately without training

### With Training (Optional)
- Downloads TrashNet dataset (30 images)
- Trains custom YOLOv8 classification model
- Better accuracy for waste-specific images
- Takes 10-30 minutes to train

## Model

Uses YOLOv8 from Ultralytics:
- **Detection Mode**: Maps COCO objects to waste categories
- **Classification Mode**: Custom trained on waste images

## Dashboard Pages

1. **Dashboard** - Overview metrics and visualizations
2. **Classify Waste** - Upload images for classification
3. **Analytics** - Detailed statistics and insights

## Dataset

TrashNet Dataset: https://github.com/garythung/trashnet
- Real waste images
- Multiple categories (glass, metal, plastic, cardboard, trash)
- Pre-resized for training
