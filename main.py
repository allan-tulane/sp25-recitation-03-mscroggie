"""
CMPS 2200  Recitation 3.
See recitation-03.md for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    if len(x) < len(y):
        x = ['0'] * (len(y) - len(x)) + x

    elif len(y) < len(x):
        y = ['0'] * (len(x) - len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x, y


def quadratic_multiply(x, y):
    # this just converts the result from a BinaryNumber to a regular int
    return _quadratic_multiply(x,y).decimal_val

def _quadratic_multiply(x, y):
    xvec = x.binary_vec
    yvec = y.binary_vec
    xval = x.decimal_val
    yval = y.decimal_val


    xvec,yvec = pad(xvec, yvec)

    if (xval <= 1) and (yval<=1):
        return BinaryNumber(xval*yval)
    else:
        x_left, x_right = split_number(xvec)
        y_left, y_right = split_number(yvec)
        n = len(xvec)
        xlyl = _quadratic_multiply(x_left, y_left)
        xlyr = _quadratic_multiply(x_left, y_right)
        xryl = _quadratic_multiply(x_right, y_left)  # Corrected line
        xryr = _quadratic_multiply(x_right, y_right)
        exp = bit_shift(BinaryNumber(2),n)
        esp2 = bit_shift(BinaryNumber(2),n//2)

        return BinaryNumber(bit_shift(xlyl,n).decimal_val + bit_shift(BinaryNumber(xlyr.decimal_val + xryl.decimal_val),n//2).decimal_val + xryr.decimal_val)

    ###


    
    
def get_test_quadratic_multiply(x,y,f):
    start = time.time()
    # multiply two numbers x, y using function f
    res = f(x,y)
    return (time.time() - start)*1000

x = BinaryNumber(10)
y = BinaryNumber(2)
print(quadratic_multiply(x,y))

print(get_test_quadratic_multiply(x,y,quadratic_multiply))

