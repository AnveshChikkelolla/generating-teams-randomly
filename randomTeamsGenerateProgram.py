import random
while(1):
         filename=input("Enter file name: ")
         f=filename.split(".")
         if f[-1]=='json':
              break;
         else:
             print("!!!!!!!!!!!!!!!!!!!please enter json file!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ");
try:
   x=open(filename)
except OSError as e:
   print("you enter wrong file path")
   exit();
count=0;l=[];size=0;z=0;rem1=0;
file=(x.read())
for i in file:
    if i=='{':
        count+=1;
if  count==1 or count==0:
    print ("file is empty");
    quit();
count=count-1;
print("number of students are in your json file are ",count)
while(1):
   n=(input("Enter no of teams you want  "))
   if (n==""):
        print ("!!!!!!!!!!!!!!!!!!!!!!!please enter  numbers of teams you want !!!!!!!!")
   elif (n.isdigit()):
         break
   else:
     print ("!!!!!!!!!!!!!!!!!!!!!!!please enter valid numbers of teams you want !!!!!!!!")
n=int(n);
print("input file contents are ")
print(file)
length=len(file)
file=file[1:length-1] #remove { at staring, } at  end in file content
file=file.split()# file content convert to list
r=(int)(count/n)#r gives the minimum no of students requried in each team
rem=int(count % n)
x=1;
with open ('output.txt','w')as m:
        m.write("team %s \n"%str(x))
        while(z<count):                          # it runs upto number of students in file
            d=random.randint(0,count-1)
            if d in l:
               continue;
            else:
              l.append(d);                       # to generate unique random number
              z=z+1
              if(size!=r):                        #r=minimum number of each team
               m.write(str(file[d]))
               m.write("\n")
               size=size+1
              elif (rem!=0):               #elif loop adding extra students if required
                 m.write(str(file[d]))
                 m.write("\n")
                 rem1=rem-1;
                 rem=0
              else :
               m.write("\n")
               x=x+1;
               m.write("team %s \n"%str(x))
               m.write(str(file[d]))
               m.write("\n")
               size=1;
               rem=rem1;
print("output file contents are ")
content=open("output.txt")
print(content.read())
