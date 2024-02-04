
# Getting current date and time using now().
 
# importing datetime module for now()
import datetime
 
# using now() to get current time
current_time = datetime.datetime.now()
 
# Printing value of now.
print(current_time.date())
print(str(current_time.hour)+":"+str(current_time.minute)+":"+str(current_time.second))
