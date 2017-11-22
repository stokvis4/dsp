# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

>>import datetime
>>a = datetime.date(int(date_start[6:len(date_start)]),int(date_start[1]),int(date_start[4:5]))
>>b = datetime.date(int(date_stop[6:len(date_start)]),int(date_stop[1]),int(date_stop[4:5]))
>>print (b-a)


####b)  
date_start = '12312013'  
date_stop = '05282015'  

>>import datetime
>>a = datetime.date(int(date_start[5:len(date_start)]),int(date_start[:2]),int(date_start[2:4]))
>>b = datetime.date(int(date_stop[5:len(date_start)]),int(date_stop[:2]),int(date_stop[2:4]))
>>print (b-a)

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

key = {"Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,"Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12}
import datetime
a = datetime.date(int(date_start[7:len(date_start)]),key[date_start[3:6]],int(date_start[:2]))
b = datetime.date(int(date_stop[7:len(date_start)]),key[date_stop[3:6]],int(date_stop[:2]))
print (b-a)
