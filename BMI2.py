#asks the question
print "What is my BMI?"

# asks for the subjects stats in US units
#print "What is your weight, in pounds?",
w = float(raw_input("What is your weight, in pounds? "))
#print "What is your height, in inches?",
h = float(raw_input("What is your height, in inches? "))

# do the math
print "Divide your weight, in pounds, by the square of your height, in inches. Then multiply the result by 703, because we live in a medieval backwater"
print "(weight/height^2)*703 =", (w / h**2) * 703

#outputs the statements
print "For those of you in more enlightened countries the problem looks a little different."
print "Your mass, in kilograms, is divided by the square of your height, in meters. No silly correction factor is needed."

#Asks for stats in SI units
#print "What is your weight, in kilos?",
k = float(raw_input("What is your weight, in kilos? "))
#print "What is your height, in meters?",
m = float(raw_input("What is your height, in meters? "))

#Does the math
print "kg/m^2=", k / m**2

