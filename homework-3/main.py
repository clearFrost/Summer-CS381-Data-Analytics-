import numpy as np
from collections import Counter
import pandas as pd


if __name__ == '__main__':
    #initializing arrays
    a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
    b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
    #gathering the common values
    answer1 = np.intersect1d(a,b)
    print(answer1)

    #arange builds the values and then we reshape the array
    answer2=np.arange(1, 16).reshape(5,3)
    print(answer2)

    #flatten to make the array into a 1d array
    answer3=answer2.flatten()
    print(answer3)

    #reshape to create a 3d array from our previously generated 2d array
    answer4=np.reshape(answer2,(5,3,-1))
    print(answer4)

    #reshaping the 3d array first then we transpose to receive a 2d array similar to our previous
    answer5=answer4.transpose(2, 0, 1).reshape(5, -1)
    print(answer5)

    #https://stackoverflow.com/questions/58383274/removing-matching-elements-from-two-numpy-arrays
    #initialize arrays
    ad = np.array([12, 5, 7, 15, 3, 1, 8])
    bd = np.array([14, 6, 3, 11, 19, 12, 5])
    #counter for the arrays
    ac = Counter(ad)
    bc = Counter(bd)
    #from there we minus the smilar elements
    result_a = sorted((ac - bc).elements())
    result_b = sorted((bc - ac).elements())
    #print the results
    print(result_a)
    print(result_b)

    #Problem 7 I found the answers using excel commands in xlsx
    #1.213 =MAX(D2:D42)
    #2.39 =COUNT(A2:A40)
    #3. mean=160.307 =SUM(D2:D40)/39 | standard deviation= 31.930 =STDEV.S(D2:D40)
    #4

    #turning xlsx to text then reading it through csv does not work
    #df=pd.read_csv("https://raw.githubusercontent.com/Skyfallup/Summer-CSCI381-11/main/Module6_Data.txt")
    #print(df)
