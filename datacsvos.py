
import os
# list the files in directory
lis = os.listdir('C:\\Users\\Sridhar Diva\\Downloads\\Engineering Test Risk Analytics\\Engineering Test Risk Analytics\\Engineering Test Files')
print(lis)
tgt = os.listdir('C:\\Users\Sridhar Diva\\Downloads\\Engineering Test Risk Analytics\\Engineering Test Risk Analytics\\Engineering Test Files')
  
file_dir ='C:\\Users\\Sridhar Diva\\Downloads\\Engineering Test Risk Analytics\\Engineering Test Risk Analytics\\Engineering Test Files''
out_file = r'C:\\Users\\Sridhar Diva\\Downloads\\Engineering Test Risk Analytics\\Engineering Test Risk Analytics\\Engineering Test Files\\Combined.csv'
ct = 0
  
print('target file :', tgt)
try:
    # check for if file exists
    # if yes delete the file 
    # otherwise data will be appended to existing file
    if len(tgt)>0:
        os.remove('C:\\Users\\Sridhar Diva\\Downloads\\Engineering Test Risk Analytics\\Engineering Test Risk Analytics\\Engineering Test Files\\Combined.csv')
  
        open(tgt, 'a').close()
    else:
        # create an empty file
        open(tgt, 'a').close()
except:
    head = open('C:\\Users\\Sridhar Diva\\Downloads\\Engineering Test Risk Analytics\\Engineering Test Risk Analytics\\Engineering Test Files\\Combined.csv', 'a+')
  
    line ='Source IP,Count,Events per Second'
    # write header to output
    print(head, line)
    head.close()
    # below loop to write data to output file
    for line1 in lis:
        f_dir = file_dir+'\\'+line1
        # open files in read mode
        in_file = open(f_dir, 'r+')
  
        # open output in append mode
        w = open(out_file, 'a+')
        d = in_file.readline()
        d = in_file.readlines()
        w.write("\n")
        for line2 in d:
            print(line2)
            w.write(line2)
            
        ct = ct + 1  
    w.close() 