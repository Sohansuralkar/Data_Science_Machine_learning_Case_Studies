from sklearn import tree

def main():
    BallFeatures = [[35,"rough"],[47,"rough"],[90,"smooth"],[48,"rough"],[90,"smooth"],[35,"rough"],[92,"smooth"],[35,"rough"],[35,"rough"],[35,"rough"],]
    
    BallNames = ["tennis","Tennis","cricket","tennis","cricket","tennis","cricket","tennis","tennis","tennis"]

    obj = tree.DecisionTreeClassifier()

    obj = obj.fit(BallFeatures, BallNames)              ### fit is used for build the moddel
    
    print(obj.predict([93,"smooth"]))  ##predict is used for predication### AI moddern approach book

if __name__ == "__main__":
    main()
