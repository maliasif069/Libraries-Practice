import numpy as np
#fancy slicing 
a=(np.arange(20).reshape(5,4))

print(a[0:2,[0,2,3]])
# bool slicing
b=np.random.randint(1,100,24).reshape(6,4)
print(b)
print(b>50)
print(b[b>50])
print(b[(b%2==0) & (b>50) ])
print((~(b%7==0)&(b>50)))

# broadcasting
a=np.arange(12).reshape(3,4)
b=np.arange(4).reshape(4)
print(a+b)

# Sigmoid function
def sigmoid(array):
    return 1/(1+np.exp(-(array)))

a=np.arange(10)
print(sigmoid(a))
\
# GRaphs using numpy and matplotlib
import matplotlib.pyplot as plt
x=np.linspace(-50,50,10)
y=x**2
plt.grid()
plt.plot(x,y)
plt.show()

