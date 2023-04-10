from __future__ import print_function
import pandas as pd
import numpy as np
import sklearn
from sklearn.metrics import classification_report
from sklearn import metrics
from sklearn import model_selection
import warnings
warnings.filterwarnings('ignore')
import pickle

# Load the trained model
RF_pkl_filename = 'RandomForest.pkl'
RF_Model_pkl = open(RF_pkl_filename, 'rb')
RF = pickle.load(RF_Model_pkl)

# Load the crop recommendation dataset
PATH = 'Crop_recommendation.csv'
df = pd.read_csv(PATH)

# Define the crop list
crops = ['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas', 'coffee', 'mungbean', 'blackgram', 'lentil', 'pomegranate', 'banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple', 'orange', 'papaya', 'coconut', 'cotton', 'jute', 'mothbeans']

# Make a prediction using the input values
input_values = np.array([[104,18, 30, 23.603016, 60.3, 6.7, 140.91]])
prediction = RF.predict(input_values)

# Sort the crops in order of decreasing probability
probabilities = RF.predict_proba(input_values)
sorted_indices = np.argsort(probabilities)[0][::-1]

# Create a list of recommended crops in order of decreasing probability
recommended_crops = []
for i in range(len(sorted_indices)):
    best_crop = crops[sorted_indices[i]]
    recommended_crops.append(best_crop)
    
# Output the recommended crops
print("Based on the input values, we recommend the following crops (in order of best to worst):")
for crop in recommended_crops:
    print("- " + crop)

print(prediction)