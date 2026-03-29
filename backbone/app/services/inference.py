import joblib
import os
from core.preprocessing import TextPreprocessor

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

model_path      = os.path.join(BASE_DIR, 'model/svm_model.pkl')
vectorizer_path = os.path.join(BASE_DIR, 'model/vectorizer.pkl')

model      = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path) 

preprocessor = TextPreprocessor()

def predict_sentiment_batch(texts):
    processed = [preprocessor.preprocessed(t) for t in texts]
    vectors = vectorizer.transform(processed)
    return model.predict(vectors)