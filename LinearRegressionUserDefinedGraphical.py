import numpy as np
import pandas
import matplotlib.pyplot as plt

def MarvellousPredictor():
    #load the data
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("values of Independent variables :",X)
    print("values of Dependent variables :",Y)
    mean_x = np.mean(X)
    mean_y = np.mean(Y)

  #  XSum = 0
  #  YSum = 0
#
  #  for i in range(len(X)):
   #     XSum = XSum + X[i]
  #      YSum = YSum + X[i]

       # mean_x = XSum / len(X)
       # mean_y = YSum / len(Y)

    print("X_mean is :",+mean_x)
    print("Y_mean is :",+mean_y)

    n = len(X)

    numerator =  0
    denomenator = 0
# Y = mx + c
    for i in range(n):
        numerator = numerator + (X[i]- mean_x)*(Y[i]- mean_y)
        denomenator = denomenator + (X[i] - mean_x)**2

        m = numerator / denomenator

        print("Slope of line m is :",+m)

        C = mean_y - (m * mean_x)

        print("Y intercept of line is :",C)

        x = np.linspace(1,6,n)

        y = C + m * X
        
        plt.plot(x,y,color = "g", label = "Regression Line")
        plt.scatter(X,Y,color = "r",label = "Scatter plot")

        plt.xlabel("X: Indenpendent Variable")
        plt.ylabel("Y: Denpendent Variable")

        plt.legend()
        plt.show()
            
        
def main():
    MarvellousPredictor()


if __name__ == "__main__":
    main()