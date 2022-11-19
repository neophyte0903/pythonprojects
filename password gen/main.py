import string
import random     #imported string and random modules


if __name__=="__main__":
    s1=string.ascii_lowercase
    
    s2=string.ascii_uppercase       #created a data set 
    
    s3=string.digits
    
    s4=string.punctuation
    

plen=int(input("enter password length\n"))
s=[]
s.extend(list(s1))
s.extend(list(s2))       #combined all the datasets into a single dataset
s.extend(list(s3))
s.extend(list(s4))

print("".join(random.sample(s,plen)))  #randomly picked a sample and joined without any delimiter :)
