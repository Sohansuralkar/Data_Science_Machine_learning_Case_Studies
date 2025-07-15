import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn .linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix,classification_report
def MarvellousLogistic(DatasetPath):
    df = pd.read_csv(DatasetPath)

    print("Dimension of dataframe is :",df.shape)
    print("Initial data is : ")
    print(df.head())  # first 5 element visible in output window

    df["Gender"] = df["Gender"].map({"Female" : 0, "Male" : 1})
    print("ENcoded data is :" ,)
    print(df.head())

    plt.figure(figsize=(8,6))
    sns.scatterplot(data = df,x = "Height", y = "Weight", hue = "Gender",palette = "Set1")
    plt.title("Marvellous Weight Height ")
    plt.xlabel("Height")
    plt.ylabel("Weight")
    plt.grid(True)
    plt.show()

    X = df[["Height","Weight"]]
    Y = df["Gender"]

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
    model = LogisticRegression()
    model.fit(X_train,Y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(Y_test,y_pred)
    print("Accuracy is :", accuracy*100)
    conf_matrix = confusion_matrix(Y_test,y_pred)
    print("Confusion matrix is :",conf_matrix)

    report = classification_report(Y_test,y_pred)
    print("classification report is :",report)

def main():
    MarvellousLogistic("weight-height.csv")

if __name__ == "__main__":
    main()

#https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html