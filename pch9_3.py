for n in range(2,21):
     f=open("tables/multiplication_tables_"+str(n)+".txt",'w')
     for i in range(1,11):
        f.write(str(n)+"x"+str(i)+"="+str(n*i))
        if(i!=10):
            f.write("\n")
f.close()        
