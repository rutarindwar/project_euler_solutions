# peuler19.py

dnames = ['Monday', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']
mnames = ['jan', 'feb', 'mars', 'apr', 'may', 'jun', 'jul', 'aug', \
          'sept', 'oct', 'nov', 'dec'] 

leapd = [ 0 , 31, 60, 91, 121,  152, 182, 213, 244, 274, 305, 335, 366]
nleapd= [0, 31] + [ i-1 for i in leapd[2:]]

p = 0

sundaycounter = 0


for y in range(1900, 2001):
    if (y%100) == 0:
        if (y%400) == 0:
##            print '2000'
            for m in range(12):
                pi = (p + leapd[m])%7
                d = dnames[pi]
##                print 'The first day of %s %i is %s' % (mnames[m], y, d)

                if d == 'Sun': sundaycounter+= 1
            
            pi = (p + leapd[m+1])%7
            
        else:
##            print 'here'
            for m in range(12):
                pi = (p + nleapd[m])%7
                d = dnames[pi]
##                print 'The first day of %s %i is %s' % (mnames[m], y, d)
            
            pi = (p + nleapd[m+1])%7

    elif (y%4) == 0:
##        print 'leap year'
        for m in range(12):
            pi = (p + leapd[m])%7
            d = dnames[pi]
##            print 'The first day of %s %i is %s' % (mnames[m], y, d)
            if d == 'Sun': sundaycounter+= 1
        
        pi = (p + leapd[m+1])%7

    else:
##        print 'non-leap year'
        for m in range(12):
            pi = (p + nleapd[m])%7
            d = dnames[pi]
##            print 'The first day of %s %i is %s' % (mnames[m], y, d)
            if d == 'Sun': sundaycounter+= 1
            
        pi = (p + nleapd[m+1])%7

    p = pi

print sundaycounter
