#!/usr/bin/env python3

# Created by: Davin Rousseau
# Created on September 2019
# This proogram calculates perimeter and area of a rectangle
# with dimensions 5cm and 3cm

import constants


def main():
    # This function calculates circumference 
    
    # input
    radius = int(input("Enter radius of the circle (mm): "))
    
    # process
    circumference = constants.TAU*radius
    
    # output
    print("")
    print("circumference is {}mm".format(circumference))
    
    
if __name__ == "__main__":
    main()
