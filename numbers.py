# data type in Python

#1) None:- variable and memory location is alocated but empty

#2) NUmeric data type

#integer data type

a = 10
print(type(a))
print(id(a))

#binary
#0b/0B01010->binary
#type conversion int->binary
b = bin(a)
print(b)

#wpp to convert binaray data into integer data
c = 0b1111
d = int(c)
print("binary to integer=",d)


#wpp to convert integer to octal
#0o/0Oxx
e= oct(a)
print("ocatl=",e)

#wpp to covert octal to integer
f= 0O23
g = int(f) 

#wpp to convert binary data into integer data
x = 0b1010
print(int(x))

#wpp to comvert integer to octal
#0o/0O

k = oct(f)
#wpp to convert octal into integer
k = 0o45
print(int(k))


#wpp to contert form intger to hexadecimal and vice versa
#0x/0X
h= hex(a)
print(h)

#hex to integer
i = 0x12af
print(int(i))

#float value
f = 3.14
print(type(f))
print(id(f))

#float-> integer
fi=int(f)
print(fi)


#integer->float

#3.8

#complex

#real part, imaginary part

h = complex(5,10)
print(h)


# float to int type conversion

m = 4.1
fi = int(m)
print(fi)

n=4.9
fi= int(n)
print(fi)

d = 4.5
fi = int(d)
print(fi)

#integer to float
p = 22
i = float(p)
print(i)

vivek = 84
chavan = float(vivek)
print(chavan)

print(id(vivek))
