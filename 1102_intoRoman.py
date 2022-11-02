class Solution:
    def intToRoman(self, num: int) -> str:
        roman=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
        d={}
        d[1]="I"
        d[4]="IV"
        d[5]="V"
        d[9]="IX"
        d[10]="X"
        d[40]="XL"
        d[50]="L"
        d[90]="XC"
        d[100]="C"
        d[400]="CD"
        d[500]="D"
        d[900]="CM"
        d[1000]="M"
        res=""
        for i in range(len(roman)-1,-1,-1):
            if num/roman[i] > 0:
                for n in range(num//roman[i]):
                    res += d[roman[i]]
            num = num%roman[i]
        return res