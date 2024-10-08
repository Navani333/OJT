
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix,precision_score,recall_score,f1_score
from sklearn.model_selection import GridSearchCV

data=pd.read_csv('loan_data1.csv')
x=data[['loan_amount','interest_rate','term','income','credit_score','age','employment_length']]
y=data['loan_repaid']

#split train_tests

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)

#initiate a model

model=DecisionTreeClassifier(random_state=42)

#train the model
model.fit(x_train,y_train)

#make a prediction

y_pred = model.predict(x_test)


accuracy = accuracy_score(y_test,y_pred)
print(f"accuracy:{accuracy:.2f}")
print("classification_report:")
print(classification_report(y_test,y_pred))

# print("confusion matrix:")
conf_matrix=confusion_matrix(y_test,y_pred)
print(conf_matrix)

precision=precision_score(y_test,y_pred)
print("precision:",precision)

recall=recall_score(y_test,y_pred)
print("recall:",recall)

F1score=f1_score(y_test,y_pred)
print("F1score:",f1_score)
