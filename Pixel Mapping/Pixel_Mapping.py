#Gianni Lake 5/26/2022
#Unauthorized reuse/modification/copying is prohibited!

# This is a program that calculates pixel coordinate values for an image that is to be displayed
# on a two dimensional surface given the dimensions of the image (assuming a square or rectangular image)
# and the corner points of the image as it is to be displayed.

import numpy as np

#Input of Values
Col = int(input("Enter Number of Columns:\n"))   #Accepts Column Count Value as Float
print(f'You entered {Col} Columns')         #Column Count Confirmation
Row = int(input("Enter Number of Rows:\n"))      #Accepts Row Count Value as Float
print(f'You entered {Row} Rows')            #Row Count Confirmation
pixgrid = (Col,Row)     #Tuple of Column and Row Count
lowerleft = input("Input Lower Left Point Coordinates Separated By A Comma (eg: x,y):")     #Accepts Lower Left Coordinates
lowerleft = lowerleft.split(",")    #Separates Coordinates and Stores Them In A List
x1 = float(lowerleft[0])    #Converts x Value to Float and Assigns it Corner Point List
y1 = float(lowerleft[1])    #Converts y Value to Float and Assigns it Corner Point List
lowerright = input("Input Lower Right Point Coordinates Separated By A Comma (eg: x,y):")   #Accepts Lower Right Coordinates
lowerright = lowerright.split(",")  #Separates Coordinates and Stores Them In A List
x2 = float(lowerright[0])   #Converts x Value to Float and Assigns it Corner Point List  
y2 = float(lowerright[1])   #Converts y Value to Float and Assigns it Corner Point List
upperleft = input("Input Upper Left Point Coordinates Separated By A Comma (eg: x,y):")     #Accepts Upper Left Coordinates
upperleft = upperleft.split(",")    #Separates Coordinates and Stores Them In A List
x3 = float(upperleft[0])    #Converts x Value to Float and Assigns it Corner Point List
y3 = float(upperleft[1])    #Converts y Value to Float and Assigns it Corner Point List
upperright = input("Input Upper Right Point Coordinates Separated By A Comma (eg: x,y):")   #Accepts Upper Right Coordinates
upperright = upperright.split(",")  #Separates Coordinates and Stores Them In A List
x4 = float(upperright[0])   #Converts x Value to Float and Assigns it Corner Point List
y4 = float(upperright[1])   #Converts y Value to Float and Assigns it Corner Point List

cornerpoints = [
                [x1,y1], #Lower Left Point
                [x2,y2], #Lower Right Point
                [x3,y3], #Upper Left Point
                [x4,y4]  #Upper Right Point
]

#User Logic/Order Error Fix (Corner points can be provided in any order)
cornerpoints.sort()           #Sorts Corner Points in Ascending Order
cornerporder = [0,2,1,3]      #Sorting Order of Lower Left, Lower Right, Upper Left, Upper Right
cornerpoints = [cornerpoints[i] for i in cornerporder]      #Reorder Corner Points to Maintain Consistency Incase of User Error 
print (f'Corner Points:{cornerpoints}')   #Corner Point List Confirmation

#Calculations and Interpretations
xvalues = [i[0] for i in cornerpoints]    #Grabs All Corner x Values Into a List
xvalues.sort()    #Sorts List of x Values in Ascending Order
yvalues = [i[1] for i in cornerpoints]    #Grabs All Corner y Values Into a List
yvalues.sort()    #Sorts List of y Values in Ascending Order
minx = xvalues[0] #Smallest x Value
maxx = xvalues[3] #Largest x Value
miny = yvalues[0] #Smallest y Value
maxy = yvalues[3] #Largest y value

#Creating, Grouping and Reordering List of Coordinates
fullgrid = []     #Final Output List
cords = []  #Raw List of Coordinates for Manipulation
for y in np.linspace(miny,maxy,Row):            #Loop for Completing Each Row of Coordinates 
      for x in np.linspace(minx,maxx,Col):      #Loop for Adding Each Coordinate for Selected Row 
            cords.append([x,y])     #Appendinging New x,y Coordinates     
cords.reverse()   #1st Reordering of Coordinates for Readability
c=0 #Counter for cords List
for i in range (Row):   #Loop for Reording Each Row of Coordinates
      fullgrid.append([]) #Empty List
      for j in range(Col):    #Loop for Populating Each Row           
            fullgrid[i].append(cords[c]) #Appending Coordinates to Final Grid for Output
            c+=1 
      fullgrid[i].reverse() #Reordering of Current Row

print(f'Here Are Your Coordinates Bounded By Corner Points:\n {fullgrid}')
input("Press ENTER to exit.")









