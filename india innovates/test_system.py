"""
Test script to verify all components of the waste recognition system
"""
import os
import sys

def test_imports():
    """Test if all required packages are installed"""
    print("Testing imports...")
    packages = [
        ('streamlit', 'Streamlit'),
        ('ultralytics', 'Ultralytics'),
        ('plotly', 'Plotly'),
        ('PIL', 'PIL'),
        ('pandas', 'Pandas'),
        ('requests', 'Requests'),
        ('cv2', 'OpenCV')
    ]
    
    all_installed = True
    for package, name in packages:
        try:
            __import__(package)
            print(f"✓ {name} installed")
        except ImportError:
            print(f"✗ {name} not installed")
            all_installed = False
    
    return all_installed

def test_files():
    """Test if all required files exist"""
    print("\nTesting files...")
    required_files = [
        "app.py",
        "waste_classifier.py",
        "download_dataset.py",
        "train_model.py",
        "requirements.txt",
        "README.md",
        "config.py"
    ]
    
    all_exist = True
    for file in required_files:
        if os.path.exists(file):
            print(f"✓ {file} exists")
        else:
            print(f"✗ {file} missing")
            all_exist = False
    
    return all_exist

def test_classifier():
    """Test if classifier can be imported"""
    print("\nTesting classifier...")
    try:
        import config
        print("✓ Config module imported")
    except Exception as e:
        print(f"✗ Config import failed: {e}")
        return False
    
    try:
        from waste_classifier import WasteClassifier
        print("✓ WasteClassifier can be imported")
        return True
    except Exception as e:
        print(f"✗ WasteClassifier import failed: {e}")
        return False

def main():
    print("=" * 50)
    print("AI Waste Recognition System - Test Suite")
    print("=" * 50)
    print()
    
    tests_passed = 0
    total_tests = 3
    
    if test_imports():
        tests_passed += 1
    
    if test_files():
        tests_passed += 1
    
    if test_classifier():
        tests_passed += 1
    
    print("\n" + "=" * 50)
    print(f"Tests Passed: {tests_passed}/{total_tests}")
    print("=" * 50)
    
    if tests_passed == total_tests:
        print("\n✓ All tests passed! System is ready.")
        print("\nNext steps:")
        print("1. Run: python download_dataset.py")
        print("2. Run: python train_model.py (optional)")
        print("3. Run: streamlit run app.py")
    else:
        print("\n✗ Some tests failed. Please install missing dependencies:")
        print("   pip install -r requirements.txt")

if __name__ == "__main__":
    main()
