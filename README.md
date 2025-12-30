# ✊🤚✌️ Rock Paper Scissors Classifier - Portfolio Project

Check out the [Live Website](https://faqihalam.vercel.app/) for a preview.

The Rock-Paper-Scissors (RPS) project is a comprehensive portfolio piece demonstrating the end-to-end Machine Learning lifecycle—from data preprocessing and training to a live web deployment.

**Dataset:** [Kaggle - Rock Paper Scissors](https://www.kaggle.com/datasets/drgfreeman/rockpaperscissors)


![Dataset Preview](\src\Images\datasetPreview.png)


---

## 🚀 Key Features

* **Real-time Image Classification**: Upload or capture images to get instant predictions using a Deep Learning model.
* **Transfer Learning Implementation**: Utilized pre-trained architectures (e.g., MobileNet/ResNet) to achieve high accuracy with shorter training time.
* **Streamlit Web Interface**: A clean, interactive UI built entirely in Python, allowing for seamless user interaction.
* **Data Augmentation**: Robust preprocessing to handle various lighting conditions and hand positions.

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
│   └── 02_About.py         # Project methodology
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
```

## 👨🏻‍💻 On Progress (Note for Me) 🚧 ✔
* Build Model: Import Dataset ✔
* Build Model: Get/Save the Model ✔
* Build Model: Evaluate Model on Validation Data 🚧
* Test Model: Test Predict New Data 🚧
* Build Streamlit: Create UI for Deploy the Model 🚧
* Deploy Streamlit: Make it access to public 🚧
* demo.gif: A 5-second recording of you playing against the AI. 🚧