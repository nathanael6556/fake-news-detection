import numpy as np
import pandas as pd
import pickle
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

def predict_logistic(X, cutoff=0.5):
    with open('models/logistic.pkl', 'rb') as f:
        logistic_model = pickle.load(f)
    with open('models/logistic_vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)

    # Convert X to list to match the expected input format
    X_vectorized = vectorizer.transform([X])
    y = logistic_model.predict_proba(X_vectorized)[:, 1]
    y_pred = (y >= cutoff).astype(int)
    return y_pred

def predict_pac(X, cutoff=0.5):
    with open('models/pac_pipeline.pkl', 'rb') as f:
        pac_model = pickle.load(f)

    y = pac_model.predict([X])  # Convert X to list
    y_pred = (y >= cutoff).astype(int)
    return y_pred

def predict_svm(X, cutoff=0.5):
    with open('models/svc_pipeline.pkl', 'rb') as f:
        svm_model = pickle.load(f)

    y = svm_model.predict([X])  # Convert X to list
    y_pred = (y >= cutoff).astype(int)
    return y_pred

def predict_decision_tree(X, cutoff=0.5):
    with open('models/decision_tree_model.pkl', 'rb') as f:
        dtc_model = pickle.load(f)
    with open('models/decision_tree_vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)

    X_vectorized = vectorizer.transform([X])  # Convert X to list
    y = dtc_model.predict(X_vectorized)
    y_pred = (y >= cutoff).astype(int)
    return y_pred

def predict_random_forest(X, cutoff=0.5):
    with open('models/random_forest_model.pkl', 'rb') as f:
        rfc_model = pickle.load(f)
    with open('models/random_forest_vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)

    X_vectorized = vectorizer.transform([X])  # Convert X to list
    y = rfc_model.predict(X_vectorized)
    y_pred = (y >= cutoff).astype(int)
    return y_pred

def predict_gradient_boosting(X, cutoff=0.5):
    with open('models/gradient_boosting_model.pkl', 'rb') as f:
        gbc_model = pickle.load(f)
    with open('models/gradient_boosting_vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)

    X_vectorized = vectorizer.transform([X])  # Convert X to list
    y = gbc_model.predict(X_vectorized)
    y_pred = (y >= cutoff).astype(int)
    return y_pred

def predict_xgboost(X, cutoff=0.5):
    with open('models/xgboost_pipeline.pkl', 'rb') as f:
        xgboost_model = pickle.load(f)

    y = xgboost_model.predict([X])  # Convert X to list
    y_pred = (y >= cutoff).astype(int)
    return y_pred

def vote(X, cutoff=0.5):
    logistic_pred = predict_logistic(X, cutoff)
    pac_pred = predict_pac(X, cutoff)
    svm_pred = predict_svm(X, cutoff)
    dtc_pred = predict_decision_tree(X, cutoff)
    rfc_pred = predict_random_forest(X, cutoff)
    gbc_pred = predict_gradient_boosting(X, cutoff)
    xgboost_pred = predict_xgboost(X, cutoff)

    y_pred = (logistic_pred + pac_pred + svm_pred + dtc_pred + rfc_pred + gbc_pred + xgboost_pred)
    y_status = np.array([])
    for i in range(len(y_pred)):
        if y_pred[i] >= 4:
            y_status = np.append(y_status, f"Berita palsu dengan probabilitas {y_pred[i] / 7 * 100:.2f}%")
        else:
            y_status = np.append(y_status, f"Berita asli dengan probabilitas {(7 - y_pred[i]) / 7 * 100:.2f}%")
    y_pred = (y_pred >= 4).astype(int)
    return y_pred, y_status