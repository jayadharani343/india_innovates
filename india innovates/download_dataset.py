import os
import requests
from pathlib import Path
import config

def download_waste_dataset():
    """Download waste classification dataset from Kaggle/GitHub"""
    
    base_path = Path(config.DATASET_PATH)
    categories = config.CATEGORIES
    
    for category in categories:
        (base_path / category).mkdir(parents=True, exist_ok=True)
    
    # Better quality waste images from various sources
    dataset_urls = {
        "biodegradable": [
            "https://raw.githubusercontent.com/garythung/trashnet/master/data/dataset-resized/cardboard/cardboard1.jpg",
            "https://raw.githubusercontent.com/garythung/trashnet/master/data/dataset-resized/cardboard/cardboard2.jpg",
            "https://raw.githubusercontent.com/garythung/trashnet/master/data/dataset-resized/cardboard/cardboard3.jpg",
            "https://raw.githubusercontent.com/garythung/trashnet/master/data/dataset-resized/cardboard/cardboard4.jpg",
            "https://raw.githubusercontent.com/garythung/trashnet/master/data/dataset-resized/cardboard/cardboard5.jpg",
            "https://raw.githubusercontent.com/garythung/trashnet/master/data/dataset-resized/cardboard/cardboard6.jpg",
            "https://raw.githubusercontent.com/garythung/trashnet/master/data/dataset-resized/cardboard/cardboard7.jpg",
            "https://raw.githubusercontent.com/garythung/trashnet/master/data/dataset-resized/cardboard/cardboard8.jpg",
            "https://raw.githubusercontent.com/garythung/trashnet/master/data/dataset-resized/cardboard/cardboard9.jpg",
            "https://raw.githubusercontent.com/garythung/trashnet/master/data/dataset-resized/cardboard/cardboard10.jpg",
        ],
        "recyclable": [
            "https://raw.githubusercontent.com/garythung/trashnet/master/data/dataset-resized/glass/glass1.jpg",
            "https://raw.githubusercontent.com/garythung/trashnet/master/data/dataset-resized/glass/glass2.jpg",
            "https://raw.githubusercontent.com/garythung/trashnet/master/data/dataset-resized/glass/glass3.jpg",
            "https://raw.githubusercontent.com/garythung/trashnet/master/data/dataset-resized/glass/glass4.jpg",
            "https://raw.githubusercontent.com/garythung/trashnet/master/data/dataset-resized/glass/glass5.jpg",
            "https://raw.githubusercontent.com/garythung/trashnet/master/data/dataset-resized/metal/metal1.jpg",
            "https://raw.githubusercontent.com/garythung/trashnet/master/data/dataset-resized/metal/metal2.jpg",
            "https://raw.githubusercontent.com/garythung/trashnet/master/data/dataset-resized/metal/metal3.jpg",
            "https://raw.githubusercontent.com/garythung/trashnet/master/data/dataset-resized/plastic/plastic1.jpg",
            "https://raw.githubusercontent.com/garythung/trashnet/master/data/dataset-resized/plastic/plastic2.jpg",
        ],
        "waste": [
            "https://raw.githubusercontent.com/garythung/trashnet/master/data/dataset-resized/trash/trash1.jpg",
            "https://raw.githubusercontent.com/garythung/trashnet/master/data/dataset-resized/trash/trash2.jpg",
            "https://raw.githubusercontent.com/garythung/trashnet/master/data/dataset-resized/trash/trash3.jpg",
            "https://raw.githubusercontent.com/garythung/trashnet/master/data/dataset-resized/trash/trash4.jpg",
            "https://raw.githubusercontent.com/garythung/trashnet/master/data/dataset-resized/trash/trash5.jpg",
            "https://raw.githubusercontent.com/garythung/trashnet/master/data/dataset-resized/trash/trash6.jpg",
            "https://raw.githubusercontent.com/garythung/trashnet/master/data/dataset-resized/trash/trash7.jpg",
            "https://raw.githubusercontent.com/garythung/trashnet/master/data/dataset-resized/trash/trash8.jpg",
            "https://raw.githubusercontent.com/garythung/trashnet/master/data/dataset-resized/trash/trash9.jpg",
            "https://raw.githubusercontent.com/garythung/trashnet/master/data/dataset-resized/trash/trash10.jpg",
        ]
    }
    
    print("Downloading waste classification dataset from TrashNet...")
    print("Source: https://github.com/garythung/trashnet")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    total_downloaded = 0
    for category, urls in dataset_urls.items():
        print(f"\nDownloading {category} images...")
        for idx, url in enumerate(urls):
            try:
                response = requests.get(url, timeout=15, headers=headers)
                if response.status_code == 200:
                    filepath = base_path / category / f"{category}_{idx+1}.jpg"
                    with open(filepath, 'wb') as f:
                        f.write(response.content)
                    print(f"  ✓ Downloaded {filepath.name}")
                    total_downloaded += 1
                else:
                    print(f"  ✗ Failed to download image {idx+1}: HTTP {response.status_code}")
            except Exception as e:
                print(f"  ✗ Failed to download image {idx+1}: {str(e)}")
    
    print(f"\n✓ Dataset download complete! Downloaded {total_downloaded} images.")
    print(f"Dataset location: {base_path.absolute()}")
    print("\nYou can now train the model using: python train_model.py")

if __name__ == "__main__":
    download_waste_dataset()
