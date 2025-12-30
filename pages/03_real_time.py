import cv2
import numpy as np
from tensorflow.keras.models import load_model

# 1. Load your trained model
model = load_model('rps_model_v1.keras')
labels = ['Paper', 'Rock', 'Scissors']

# 2. Setup Webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret: break

    # 3. Preprocessing (Must match your training steps!)
    # Define a 'Region of Interest' (the box where you put your hand)
    roi = frame[100:400, 100:400] 
    img = cv2.resize(roi, (150, 150))
    img = img / 255.0  # Normalize
    img = np.expand_dims(img, axis=0)

    # 4. Predict
    prediction = model.predict(img)
    class_idx = np.argmax(prediction)
    confidence = np.max(prediction)

    # 5. Display Results
    label_text = f"{labels[class_idx]} ({confidence*100:.1f}%)"
    cv2.rectangle(frame, (100, 100), (400, 400), (0, 255, 0), 2)
    cv2.putText(frame, label_text, (100, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    cv2.imshow('RPS Real-Time Classifier', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()