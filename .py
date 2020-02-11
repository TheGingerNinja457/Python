print ('##################################')
print ('##### Max\'s Herbs and spices ####')
print ('##################################')
#Printing banner
username=input('What is your name?')
print('Hi ' + username)
print('I will need to know your age')
age=input('What is your age?')
#Asking what and name is etc
if float(age) < 18.0: 
  print ('Sorry bud you\’re too young')
elif float(age) >= 18.0:
 price= input('How much you willing to spend?')
if float(price) < 5.0:
  print('Not enough money come back with more')
  elif float(price) > 5:
    print('You can buy a simple herb')
