import collections

index=1
with open("q.txt","r",encoding="utf-8") as f:
    lines=f.readlines()
    for line in lines:
        if line.find("Q")==0:

            line=line.strip()
            print(str(index)+"."+line[2:])
            index+=1

