"""
File: weather_master.py
Name: Alice Liu
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant controls when to stop
EXIT = -100


def main():
	"""
	This program finds the minimum, maximum among user inputs
	"""
	print('stanCode\"Weather Master 4.0"!')
	temperature = int(input('Next Temperature:(or' + str(EXIT) + 'to quit)?'))
	if temperature == EXIT:
		print('No temperatures were entered.')
	else:
		minimum = temperature
		maximum = temperature
		total = temperature
		days = 1
		cold = 0                 #多設days&cold 兩個盒子
		if temperature < 16:
			cold += 1

		while True:
			temperature = int(input('Next Temperature:(or' + str(EXIT)+'to quit)?'))
			if temperature == EXIT:
				break
			if temperature < minimum:
				minimum = temperature
			if temperature > maximum:
				maximum = temperature
			if temperature < 16:
				cold += 1
			days = days + 1
			total = temperature + temperature

		print('Highest temperature = '+str(maximum))
		print('Lowest temperature ='+str(minimum))
		print('Average =' + str(total/days))
		print(str(cold)+'cold day(s)')

# def average():
# 	temperature = (maximum+minimum)/2


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
