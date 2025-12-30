# ✊🤚✌️ Rock Paper Scissors Classifier - Portfolio Project

Check out the [Live Website](https://rockpapersciapprsclassifier-8tfms7raghjzd586z58bqq.streamlit.app/) for a preview.

The Rock-Paper-Scissors (RPS) project is a comprehensive portfolio piece demonstrating the end-to-end Machine Learning lifecycle—from data preprocessing and training to a live web deployment.

**Dataset:** [Kaggle - Rock Paper Scissors](https://www.kaggle.com/datasets/drgfreeman/rockpaperscissors)


![Dataset Preview](https://github.com/faqih28alam/RockPaperScissorsClassifier/blob/main/src/Images/datasetPreview.png)



---

## 🚀 Key Features

* **Real-time Image Classification**: Upload or capture images to get instant predictions using a Deep Learning model.
* **Transfer Learning Implementation**: Utilized pre-trained architectures (e.g., MobileNet/ResNet) to achieve high accuracy with shorter training time.
* **Streamlit Web Interface**: A clean, interactive UI built entirely in Python, allowing for seamless user interaction.
* **Data Augmentation**: Robust preprocessing to handle various lighting conditions and hand positions.

---

## Model Result

**Confusion Matrix**:

![Confusion Matrix](https://github.com/faqih28alam/RockPaperScissorsClassifier/blob/main/src/Images/Confusion%20Matrix%20Result.png)

```text
              precision    recall  f1-score   support

           0       0.99      0.99      0.99       145
           1       0.97      1.00      0.99       143
           2       1.00      0.97      0.98       150

    accuracy                           0.99       438
   macro avg       0.99      0.99      0.99       438
weighted avg       0.99      0.99      0.99       438
```

---

## 📂 Project Structure



```text
RockPaperScissorsClassifier/
├── .streamlit/             # Streamlit configuration & theme settings
├── models/                 # Serialized models (.h5 or .keras format)
│   └── rps_model_v1.keras       
├── notebooks/              # Research & Development
│   └── training_v1.ipynb   # Model architecture and training logs
├── src/                    # Reusable Logic
│   ├── data_loader.py      # Script to preprocess image bytes
│   └── model_utils.py      # Prediction and confidence score logic
├── pages/                  # Multi-page App (optional)
│   ├── 01_Analytics.py     # Model performance metrics
│   ├── 02_About.py         # Project methodology
│   └──03_real_time.py      # Real Time Prediction
├── app.py                  # MAIN ENTRY POINT for Streamlit
├── requirements.txt        # Production dependencies
└── .gitignore              # Files to ignore (e.g., .venv/, __pycache__/)
```

## 🛠️ Local Setup
```text
- git clone [https://github.com/yourusername/rps-classifier.git](https://github.com/yourusername/rps-classifier.git) # Clone Repository
- python -m venv .venv              # Create Virtual Environment with .venv name on Powershell
- .\.venv\Scripts\Activate.ps1      # Activate environmet on Powershell
- pip install -r requirements.txt   # Install Dependencies
- streamlit run app.py              # Run the App
- deactivate                        # Deactivate environment on Powershell
- python pages/03_real_time.py      # to run localy realtime prediction
- streamlit run app.py              # to run streamlit
```

## 👨🏻‍💻 On Progress (Note for Me) 🚧 ✔
* Build Model: Import Dataset ✔
* Build Model: Get/Save the Model ✔
* Build Model: Evaluate Model on Validation Data ✔
* Test Model: Test Predict New Data ✔
* Build Realtime Prediction ✔
* Build Streamlit: Create UI for Deploy the Model ✔
* Deploy Streamlit: Make it access to public 🚧
* demo.gif: A 5-second recording of you playing against the AI. 🚧
