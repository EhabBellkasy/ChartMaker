import alpaah
from alpaah import betra
import TimeStamp as TS

print (alpaah.betra)
print (betra)
EZA=[1,5,7,4,6]
BZA=[42,79,31,54]
print(EZA)
EZA.append(2)
print(EZA)
EZA.extend(BZA)
print(EZA)


print("###################################################################")

index = 0
index1 =TS.fun(scope="5s",indexType =1)
index2 =TS.fun(scope="5s",indexType =2)
index3 =TS.fun(scope="5s",indexType =3)

print (len(index1))

for index in range(len(index1)):
    print(index1[index] ,index2[index] ,index3[index])
