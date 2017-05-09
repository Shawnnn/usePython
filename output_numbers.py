sum=0
for i in range(1,5):
    #print "i=",i
    for j in range(1,5):
        
        if i==j:
            continue
        #print "j=",j
        for k in range(1,5):
            if k==i or k==j:
                continue
            #print "k=",k
            num=100*k+10*j+i
            sum+=1
            print num
print 'sum=',sum
