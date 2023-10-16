# to calculate the area of a circle 
def area_of_circle(r):
    pi = 3.147  
    area = pi*r*r
    return area 

radius = float(input("Enter Radius: "))
print ( " Area : ",area_of_circle(radius))

# to calculate the circumfrence of a circle 
def circum_of_circle(r):
     pi = 3.147  
     circum = 2*pi*r
    

radius = float(input("Enter Radius: "))
print ( " Circum : ",circum_of_circle(radius))