#Program Output
#You are xx years, yy months, zz days old. 
#50% productive life remaining.

import datetime
from datetime import datetime, date, time
import dateutil #not available in standard python installation. Use [pip install django-dateutil].
from dateutil.relativedelta import relativedelta

dob = datetime(year=1992, month=7, day=5) #Nishant's date of birth
current_date = datetime.now() #Present Date

#Difference for calculating % time in life spent.
difference  = current_date - dob 
difference_in_years = (difference.days + difference.seconds/86400)/365.2425

#Age
print 'You are', relativedelta(current_date, dob).years, 'years,', relativedelta(current_date, dob).months, 'months and', relativedelta(current_date, dob).days, 'days old.'

#Calculating % life spent.
#Productive age is here assumed to be 0-50 years.
#Conservative estimate. Both upper and lower limit are a bit off.

print '\n%.2f' %(100-(difference_in_years*100)/50), '% productive life remaining.\n'

e = raw_input("Press enter to exit.") #grin

