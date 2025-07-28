import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,classification_report



def main():
    df = pd.read_csv("Telco-Customer-Churn.csv")

    df.drop(["customerID","gender"], axis = 1, inplace=True)

    for col in df.select_dtypes(include="object"):
        df[col] = LabelEncoder().fit_transform(df[col])

    #print(df.head())

    X =df.drop("Churn", axis=1)
    Y =df["Churn"]

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    model = RandomForestClassifier(n_estimators=150, max_depth=30,random_state=42)

    model.fit(X_train,Y_train)

    y_pred = model.predict(X_test)

    print("Accuracy score is :",accuracy_score(Y_test,y_pred))

if __name__ == "__main__":
    main()
