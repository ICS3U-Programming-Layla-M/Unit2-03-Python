#!/usr/bin/env python3
# Created by: Layla Michel
# Created on: May 4, 2021
# This program calculates and displays the circumference
# of a circle using Tau and user input.

import constants


def main():
    # Ask the user for the radius
    global radius
    print("Hello today we will calculate the circumference of a circle!")
    radius = float(input("First, enter the radius of the circle (cm): "))
    calc_circum()


def calc_circum():
    # Calculate and display the circumference
    print("The circumference of the\
 circle is: {:.2f} cm^2". format(constants.TAU*radius))


if __name__ == "__main__":
    main()
