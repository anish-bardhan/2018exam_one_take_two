average = (85, 85, 85, 85, 85, 85, 85,)

#made a method so it can be called
def donuts(arr):
    #made a value to hold the average
    avg = 0
    #used a for loop to cycle through the arr
    for grade in arr:
        #added each grade to the average so it can be divided
        avg += grade
    #made the average an actual average
    avg = avg/len(arr)
    #repeatedly used if/else statements to identify the exact code i needed
    if avg >= 90:
        food = (len(arr)*1)
    elif avg >= 80 and avg < 90:
        food = (len(arr)*1/2)
    elif avg >= 70 and avg < 80:
        food = (len(arr)*1/3)
    else:
        food = (len(arr)*-1/2)
    #printed the value for food
    print(food)

#called the method
donuts(average)
