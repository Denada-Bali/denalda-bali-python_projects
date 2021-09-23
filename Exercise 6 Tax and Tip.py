#Exercise 6: Tax and Tip                                   (Solved—17 Lines)

#The program that you create for this exercise will begin by reading the cost of a meal
#ordered at a restaurant from the user. Then your program will compute the tax and
#tip for the meal. Use your local tax rate when computing the amount of tax owing.
#Compute the tip as 18 percent of the meal amount (without the tax). The output from
#your program should include the tax amount, the tip amount, and the grand total for
#the meal including both the tax and the tip. Format the output so that all of the values
#are displayed using two decimal places.

Tax = 0.10
Tip = 0.18

cost = float(input("Enter the cost of the meal: " ))

Tax_Amount = cost * Tax
Tip_Amount = cost * Tip
Toatl = Tax_Amount + Tax_Amount

print ("The Tax Amount is %.2f " %Tax_Amount)
print ("The Tip Amount is %.2f " %Tip_Amount)
print ("The total Amount is %.2f " %Toatl)
