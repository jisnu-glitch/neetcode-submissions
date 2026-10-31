class Solution:

    def encode(self, strs: List[str]) -> str:

        if not strs:
            return ''

        sizes=[]

        for i in strs:
            t=len(i)
            sizes.append(str(t))
        
        encoded = ','.join(sizes)
        encoded+= '#'
        encoded += ''.join(strs)

        return encoded



    def decode(self, s: str) -> List[str]:
        
        if not s:
            return []
        
        sizes=[]
        rec=''
        for i in s:
            if i=='#':
                break
            rec+=i
        
        sizes= rec.split(',')

        decoded=[]
        i= len(rec)+1
        k=0

        while k< len(sizes):
            decoded.append(s[i: i + int(sizes[k])])
            i+= int(sizes[k])
            k+=1
        
        return decoded
