from sklearn import tree

# rough 0
#smooth 1

def main():
    BallFeatures = [[35,0],[47,0],[90,1],[48,0],[90,1],[35,0],[92,1],[35,0],[35,0],[35,0],]
    
    BallNames = ["tennis","Tennis","cricket","tennis","cricket","tennis","cricket","tennis","tennis","tennis"]

    obj = tree.DecisionTreeClassifier()

    obj = obj.fit(BallFeatures, BallNames)              ### fit is used for build the moddel
    
    print(obj.predict([93,1]))  ##predict is used for predication### AI moddern approach book

if __name__ == "__main__":
    main()