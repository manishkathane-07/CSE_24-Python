"""A)Develop a Python program that takes a voltage (V) and resistance (R) as inputs from the user and calculates the
current (I) using Ohm’s Law."""

V=int(input("Enter Voltage(V): "))
R=int(input("Enter Resistance(R): "))

#V=IR
I=V/R
print("Value of Current(I): ",I)

"""B)Modify the above program to display the nature of current:
If current<0.5 A, print “Low current”
If 0.5 A ≤ current ≤ 2 A, print “Normal current”
If current >2 A, print “High current"""

V=int(input("Enter Voltage(V): "))
R=int(input("Enter Resistance(R): "))

I=V/R

if (0.5>I):
    print("Low Current")
elif(0.5>=I and I<=2):
    print("Normal Current")
else:
    print("High Current")