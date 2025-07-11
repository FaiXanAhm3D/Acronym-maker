#calculating the age
y=int(input("Enter year of birth : "))
m=int(input("Enter your month of birth : "))
d=int(input("Enter your day of birth : "))
age_in_year = 2022-y
age_in_month = 8-m
age_in_day = 20-d
if age_in_day < 0:
    print('Your age is:', age_in_year, " years " , age_in_month, 'months and ' ,'0 days')

elifj age_in_month < 0:
    print('Your age is:', age_in_year, " years " ,'0 months and ' , age_in_day, 'days')
else :
    print('Your age is:', age_in_year, " years " , age_in_month, 'months and ' , age_in_day, 'days')
