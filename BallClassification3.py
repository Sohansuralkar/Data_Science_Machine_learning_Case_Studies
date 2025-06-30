from sklearn import tree

# rough 0
#smooth 1
#1 tennis
#2 cricket

def main():
    BallFeatures = [[35,0],[47,0],[90,1],[48,0],[90,1],[35,0],[92,1],[35,0],[35,0],[35,0],]
    BallNames = [1,1,2,1,2,1,2,1,1,1]
    obj = tree.DecisionTreeClassifier()
    obj = obj.fit(BallFeatures, BallNames)              ### fit is used for build the moddel train the model also
    print(obj.predict(([[93,1]])))  ##predict is used for predication### AI moddern approach book
    #print(obj.predict(([[93,1]])))

if __name__ == "__main__":
    main()