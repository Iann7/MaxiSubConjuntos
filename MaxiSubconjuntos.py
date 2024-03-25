# 0<=i<len(M)

def main():
    M= [[0,10,10,1]
      ,[10,0,5,2]
      ,[10,5,0,2]
     ,[1,2,2,0]]
    print(iCombinations(M,[],0,len(M)-1))


def iCombinations(M:list,usedi:list,i:int,k:int)->int:
    if i==k:
        print((GetSum(M,usedi),usedi))
        return (GetSum(M,usedi),usedi)
    else:
        return max(iCombinations(M,usedi+[i],i+1,k)    
              ,iCombinations(M,usedi,i+1,k),key=lambda e:e[0])

    
def GetSum(M:list,indexes:int)->int:
    sum:int=0
    usedIndexes=[]
    for a in indexes:
        for b in indexes:
            if not(a in usedIndexes):
                elem:int=M[a][b]
                sum+=elem
                elem=M[b][a]
                sum+=elem
            else: continue
        if(not(a in usedIndexes)): usedIndexes.append(a)
    return sum

main()
