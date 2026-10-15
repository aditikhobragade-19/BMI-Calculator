def calculate_bmi(weight,height):
	return weight / (height**2)
print("==== BMI CALCULATOR ====")
try:
	weight=float(input("Enter your weight in kg:"))
	height=float(input("Enter your height in meters:"))

	if weight <=0 or height<=0:
		print("Weight and height must be positive!")
	else:
		bmi=calculate_bmi(weight,height)
		print(f"Your BMI is :{bmi:.2f}")
		if bmi<18.5:
			print("Category:Uderweight")
		elif bmi<25:
			print("Category:Normal Weight")
		elif bmi<30:
			print("Category:OverWeight")
		else:
			print("Category:Obese")
except ValueError:
	print("Please enter valid numbers!")

