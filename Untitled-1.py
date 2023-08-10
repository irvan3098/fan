
soal1 = [10,20,20,10,10,30,50,10,20]
soal2 = [6,5,2,3,5,2,2,1,1,5,1,3,3,3,5]
soal3 = [1,1,3,1,2,1,3,3,3,3]

res = {}

def findSameNumber(arr) :
    for i in arr:
        res[i] = arr.count(i)
    
    print(res)
    cek =0 
    for i in res:
        print(i, " => ", (int(res[i] / 2)))
        if (int(res[i] / 2)) != 0:
            cek = int(res[i] / 2) + cek
    
    print("Data sepasang = ",cek)
findSameNumber(soal3)
