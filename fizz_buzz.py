
def fizz_buzz(number):

	# divisiblity by 3 only
	if number % 3 == 0 and number % 5 > 0:
		return "Fizz"

	# divisiblity by 5 only
	elif number % 5 == 0 and number % 3 > 0:
		return "Buzz"

	# divisiblity by 3 and 5
	elif number % 3 == 0 and number % 5 == 0:
		return "FizzBuzz"

	# divisiblity by neither 3 and 5
	elif number % 3 !=0 or number % 5 != 0:
		return number
