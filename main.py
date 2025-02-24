def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(input_year, input_month):
#   This is doc string
  """This function take two input and then gave the days in month"""
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  leap_year_check = is_leap(input_year)
  if leap_year_check and input_month == 2:
    days = 29
  else:
    days = month_days[input_month - 1]
  return days




  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)












