s = "ab"
t = "A"
ans=s
k=list(t)
c=[]
l="  "
for i in range(len(s)):
      k=list(t)
      l=""
      for j in range(i,len(s)):
            l+=s[j]
            if s[j] in k:
                  k.remove(s[j])
            if k==[]:
                  if len(l)<len(ans):
                        ans=l
                  break
if s==l:
      print("")
else:
      print(ans)
