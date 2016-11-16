#proj euler problem 33

for i in range(10, 101):
    print i
    for j in range(10, 101):
        if (i/float(j) < 1) and ('0' not in (str(i) and str(j))):


            l = [eval(k) for k in list(str(i))] # numer
            js = [eval(h) for h in list(str(j))]
            ai, bi = l[0], l[1]
            
            if (ai in js):
                js.remove(ai)
                jc1 = js[0]
                if (float(bi)/ jc1) == float(i)/float(j):
                    print "===========> ", i, j
            js = [eval(h) for h in list(str(j))]
            if (bi in js):
                js.remove(bi)
                jc2 = js[0]
                if (float(ai)/jc2) == float(i)/float(j):
                    print "===========> ",i, j
