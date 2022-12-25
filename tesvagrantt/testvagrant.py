#importing iteratools
import itertools
#getting budjet from the user
budjet=int(input("enter your budjet"))
# declaring 
thisdict = {
  26:"TOI",
  20.5:"Hindu",
  34: "ET",
  10.5:"BM",
  16.4:"HT",
};
val=[26,20.5,34,10.5,16.4]
newspaper=[]
pairs=list(itertools.combinations(val, 2))
for i in pairs:
    if sum(i)<=budjet:
        newspaper.append(i)

newsp=[]
for i in range(len(newspaper)):
        value1=newspaper[i][0]
        value2=newspaper[i][1]
        newsp.append((thisdict[value1],thisdict[value2]))
print(newsp)
