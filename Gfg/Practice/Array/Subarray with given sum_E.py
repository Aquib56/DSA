class Solution:
    def subArraySum(self,arr, n, s): 
        i=0
        res=0
        for r in range(n):
            res=0
            while(res<s):
                if(r>n-1):
                    break
                else:
                    res=res+arr[r]
                    print(f"{res},{arr[r]},({i},{r})")
                    r=r+1
            i+=1
            if res==s:
                return i,r
        return -1
if __name__=="__main__":
    e1=Solution()
    arr=[142 ,112 ,54 ,69 ,148 ,45 ,63 ,158 ,38 ,60 ,124 ,142 ,130 ,179 ,117 ,36 ,191 ,43 ,89 ,107 ,41 ,143 ,65 ,49 ,47 ,6 ,91 ,130 ,171 ,151 ,7 ,102 ,194 ,149 ,30 ,24 ,85 ,155 ,157 ,41 ,167 ,177 ,132 ,109 ,145 ,40 ,27 ,124 ,138 ,139 ,119 ,83 ,130 ,142 ,34 ,116 ,40 ,59 ,105 ,131 ,178 ,107 ,74 ,187 ,22 ,146 ,125 ,73 ,71 ,30 ,178 ,174 ,98 ,113]
    print(e1.subArraySum(arr,len(arr),665))