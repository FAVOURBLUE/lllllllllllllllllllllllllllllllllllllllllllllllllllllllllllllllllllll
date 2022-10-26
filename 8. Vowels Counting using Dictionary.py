line=input() 
vowel=”aeiou
” vow=[] 
count=0 
space=0
for i in line: 
line=line.lower(
) if i in vowel:
vow.append(i
) count+=1
if i==’ ‘: 
space+=
1
per=count/5
dic={“No. of letters”:len(line)-
space, ”No. of 
Vowels”:count, 
“Percentage”:per*100
} 
print(dic)