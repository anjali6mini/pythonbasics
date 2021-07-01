s='You are awesome.'

s1='''You are the 
      creator of your own destiny.'''

print (s, s1)
#indexing
print(s[0],s1[2])
print(s1*3, s*2)
print(len(s1))
print(len(s))

#slicing
print(s[0:1]) #prints the string from index 0 to index-1
print(s1[3:19])
print(s[0:]) #prints from beginning to end
print(s[:6]) #print starts from the beginning i.e. 0 till the index-1
print(s[-5:-2]) #prints from the last of the string
print(s[1:10:2])
print(s[len(s)::-1])