#peuler102

f = open('triangles.txt', 'r')
d = f.readlines()
d = [i[:-1] for i in d]

counta = 0
countb = 0
countc = 0
for k in range(len(d)):
    l = [eval(i) for i in d[k].split(',')]

    ax, ay, bx, by, cx, cy = l

    if (ax != bx) and (ax !=cx) and (bx != cx):        
        sab = (ay-by)/float(ax-bx)
        sac = (ay-cy)/float(ax-cx)
        sbc = (by-cy)/float(bx- cx)

        iab = by - (sab * bx) # using ax, ay
        iac = ay - (sac * ax)
        ibc = by - (sbc * bx)

    else:
##        print "one side is vertical ***********"
        if (ax == bx):
            iab = -100
        elif (ax == cx):
            iac = -100
        else:
            ibc = -100
####    print iab, iac, ibc

    if sum([1 if i > 0 else 0 for i in [iab, iac, ibc]]) == 1:
##        print [1 if i > 0 else 0 for i in [iab, iac, ibc]]
        if iab > 0:
            if (ax * bx) < 0:
##                print "accepted"
                counta += 1
            else:
                print "ab does not cross y", ax, bx
                
        elif iac > 0:
            if (ax * cx) < 0:
##                print "accepted"
                countb += 1
            else:
                print "ac does not cross y"
        elif ibc > 0:
            if (bx * cx) < 0:
                print "accepted"
                countc += 1
            else:
                print "bc does not cross y"
