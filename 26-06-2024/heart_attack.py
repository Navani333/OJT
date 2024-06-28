import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

# Creating the dataset
data = {
    'age': [55, 60, 45, 50, 65],
    'gender': [1, 0, 1, 0, 1],  # male=1, female=0
    'cholesterol': [220, 180, 190, 200, 230],
    'bp': [140, 130, 110, 120, 150],
    'smoking': [1, 0, 1, 0, 1],  # yes=1, no=0
    'diabetes': [0, 1, 0, 0, 1],  # yes=1, no=0
    'exercise': [1, 0, 1, 1, 0],  # yes=1, no=0
    'heart_attack': [1, 1, 0, 0, 1]
}

df = pd.DataFrame(data)

# Splitting the data into features and target
X = df.drop('heart_attack', axis=1)
y = df['heart_attack']

# Splitting the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

# Training the logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Making predictions on the test set
y_pred = model.predict(X_test)

# Calculating the evaluation metrics
conf_matrix = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# Printing the results
print("Confusion Matrix:")
print(conf_matrix)
print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1 Score: {f1}")
