#Exercise 11: Fuel Efficiency                                (13 Lines)

#In the United States, fuel efficiency for vehicles is normally expressed in miles-pergallon (MPG).
#In Canada, fuel efficiency is normally expressed in liters-per-hundred kilometers (L/100 km).
#Use your research skills to determine how to convert from MPG to L/100 km.
#Then create a program that reads a value from the user in American
#units and displays the equivalent fuel efficiency in Canadian units.

Liters_per_Hundred_Kilometers = 235.215 

MPG = int(input("Enter miles-pergallon (MPG): "))

Result = Liters_per_Hundred_Kilometers/MPG

print (MPG,"Miles-pergallon (MPG) convertet in liters-per-hundred kilometers(L/100 km) was ", Result )
