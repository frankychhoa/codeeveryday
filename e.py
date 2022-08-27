class Solution:
    def addBinary(self, a: str, b: str) -> str:
        total = int(a) + int(b)
        total = str(total)
        index = len(total)-1
        
        add1 = 0

        for i in range(len(total)):

            if total[index] == "2":
                total= total[:index] + "0"
                add1 = 1
            
            elif total[index] == "1" and add1 == 1 and index==0 :
                total= total[:index] + "0"+ total[index+1:]
                total = "1" + total 
            elif total[index] == "1" and add1 == 1:
                total = total[:index] + "0"
            else:
                 break
            index -=1
        return total