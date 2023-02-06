import pandas as pd
import numpy as np


if __name__ == '__main__':
    #to display all of our columns otherwise we get ....
    pd.set_option('display.max_columns',None)
    #this isnt needed because there isnt that many columns
    #pd.set_option('display.max_rows', None)
    #read text file from my github
    df = pd.read_csv("https://raw.githubusercontent.com/Skyfallup/Summer-CSCI381-11/main/cars-sample35.txt", header = None, names = ['Price','Maintenance Cost','Number of doors', 'Number of passengers', 'Luggage capacity', 'Safety rating','Classification of vehicle'])
    #prints the dataframe just to see if it worked
    #print(df)

    #we create a list for all the columns in the dataframe
    priceList = df['Price'].tolist()
    maintenanceList = df['Maintenance Cost'].tolist()
    doorsList = df['Number of doors'].tolist()
    passengersList = df['Number of passengers'].tolist()
    luggageList = df['Luggage capacity'].tolist()
    safetyList = df['Safety rating'].tolist()
    classificationList = df['Classification of vehicle'].tolist()

    medpriceList = []

    priceIndex = 0

    for x in priceList:
        if x == "med":
            #print(x)
            #print(priceIndex)
            #adds the index number to the new list
            medpriceList.append(priceIndex)
            #loop counter for index
        priceIndex += 1
    print(medpriceList)
    #empty list to store the passengers with med
    medpassengersList = []
    #loop so that we can go through our medprice and for each locate a number of passenger for it
    for x in medpriceList:
        #print(passengersList[x])
        #essentially adding passenger number to the passenger list here
        medpassengersList.append(passengersList[x])
    #printing the new list we made
    print(medpassengersList)

    priceandmaintIndex = 0
    priceandmaintList = []

    for x in priceList:
        if x == 'high' and maintenanceList[priceandmaintIndex] != 'low': #if statement to create rule
            priceandmaintList.append(priceandmaintIndex)#add indices if statement is true
        priceandmaintIndex +=1
    print(priceandmaintList)

    #https://stackoverflow.com/questions/39413359/finding-indices-from-list-comprehension-in-python-3
    medpricelistComp = [i for i, x in enumerate(priceList) if x == 'med']
    #prints list we just made
    print(medpricelistComp)

    #using previously made medpricelistcomp we know indices for passengers list with med
    medpassengerslistComp= [passengersList[i] for i in medpricelistComp]
    print(medpassengerslistComp)

    #borrowing the idea from question 6 i just adjusted it by adding any extra if statement
    pricehighmaintlowComp =[i for i, x in enumerate(priceList) if x=='high' and maintenanceList[i] != 'low']
    print(pricehighmaintlowComp)


    nlist = [[1,2,3],['A','B','C'],[4,5],['D','E']]
    #keeps the 2d array
    nlistNew = [[x for x in nlist], x in nlist]
    print(nlist)