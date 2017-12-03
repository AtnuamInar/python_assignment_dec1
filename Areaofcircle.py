def area_of_circle(radius):
     return 22/7*radius**2
 
radius = input('Enter the radius: ')
area = area_of_circle(float(radius))
 
print("\n\nRadius of circle = {0} cm.\nArea of circle = {1:.3f} sq. cm.".format(radius,area))
