import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
#symbols = "!@#$%^&*?/\?|~"
use_for = lower_case + upper_case + number
lenth_for_password = 9
password = "".join(random.sample(use_for,lenth_for_password))
print("Your generated password : ", password)


