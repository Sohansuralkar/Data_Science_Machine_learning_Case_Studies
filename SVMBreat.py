import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix,classification_report
from sklearn.preprocessing import StandardScaler

def MarvellousCancerDetection():
    cancer = load_breast_cancer()                 # dataset load kela ithe
    X = cancer.data
    Y = cancer.target

    data = pd.DataFrame(X, columns=cancer.feature_names)
    data["target"] = Y
    print(data.shape)
    print("Classes : ",dict(zip(cancer.target_names, [0,1])))

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train , X_test, Y_train ,Y_test = train_test_split(X_scaled,Y, test_size= 0.2,random_state=42)
    model = SVC(kernel="linear",C=1)    # SVC support vector classifer
    model.fit(X_train,Y_train)
    y_Pred = model.predict(X_test)
    print("Accuracy score is  : ",accuracy_score(Y_test,y_Pred)*100)
    print("Confusion Matrix  : ",confusion_matrix(Y_test,y_Pred)*100)

def main():
    MarvellousCancerDetection()

if __name__ == "__main__":
    main()
