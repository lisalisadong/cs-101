# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def days_of_month(month):
	days_of_month = 0
	if month > 1:
		month = month - 1
		days_of_month = days_of_month + 31	
	if month > 1:
		month = month - 1
		days_of_month = days_of_month + 28
	if month > 1:
		month = month - 1
		days_of_month = days_of_month + 31
	if month > 1:
		month = month - 1		
		days_of_month = days_of_month + 30
	if month > 1:
		month = month - 1
		days_of_month = days_of_month + 31
	if month > 1:
		month = month - 1
		days_of_month = days_of_month + 30
	if month > 1:
		month = month - 1
		days_of_month = days_of_month + 31
	if month > 1:
		month = month - 1
		days_of_month = days_of_month + 31
	if month > 1:
		month = month - 1
		days_of_month = days_of_month + 30
	if month > 1:
		month = month - 1
		days_of_month = days_of_month + 31
	if month > 1:
		month = month - 1
		days_of_month = days_of_month + 30
	return days_of_month

def isLeapYear(year):
	if year % 100 != 0:
		if year % 4 == 0:
			return True
	if year % 400 == 0:
		return True
	return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):   
	result = (year2 - year1) * 365 + days_of_month(month2) - days_of_month(month1) + day2 - day1
	year = year1
	while True:
		if isLeapYear(year):
			result = result + 1
			year = year + 1
			if year > year2:
				break
		year = year + 1
		if year > year2:
			break
	if isLeapYear(year1):
		if month1 > 2:
			result = result - 1
	if isLeapYear(year2):
		if month2 < 3:
			result = result - 1
	return result

# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()