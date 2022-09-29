# -*- coding: utf-8 -*-
"""Numpy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_xsdeP5MQTnTzRkmFaLEZ-D-DIb5J49V

# NumPy

Numpy introduction
------------------

The NumPy package (read as NUMerical PYthon) provides access to

-   a new data structure called `array`s which allow

-   efficient vector and matrix operations. It also provides

-   a number of linear algebra operations (such as solving of systems of linear equations, computation of Eigenvectors and Eigenvalues).

### History

Some background information: There are two other implementations that provide nearly the same functionality as NumPy. These are called “Numeric” and “numarray”:

-   Numeric was the first provision of a set of numerical methods (similar to Matlab) for Python. It evolved from a PhD project.

-   Numarray is a re-implementation of Numeric with certain improvements (but for our purposes both Numeric and Numarray behave virtually identical).

-   Early in 2006 it was decided to merge the best aspects of Numeric and Numarray into the Scientific Python (<span>`scipy`</span>) package and to provide (a hopefully “final”) `array` data type under the module name “NumPy”.

We will use in the following materials the “NumPy” package as provided by (new) SciPy. If for some reason this doesn’t work for you, chances are that your SciPy is too old. In that case, you will find that either “Numeric” or “numarray” is installed and should provide nearly the same capabilities.[5]

### Arrays

We introduce a new data type (provided by NumPy) which is called “`array`”. An array *appears* to be very similar to a list but an array can keep only elements of the same type (whereas a list can mix different kinds of objects). This means arrays are more efficient to store (because we don’t need to store the type for every element). It also makes arrays the data structure of choice for numerical calculations where we often deal with vectors and matricies.

Vectors and matrices (and matrices with more than two indices) are all called “arrays” in NumPy.

#### Vectors (1d-arrays)

The data structure we will need most often is a vector. Here are a few examples of how we can generate one:

# Array Creation and Properties

There are a lot of ways to create arrays.  Let's look at a few

Here we create an array using `arange` and then change its shape to be 3 rows and 5 columns.
"""

import numpy as np

a=np.arange(15)
b=np.arange(20)

a
b

a=np.arange(15).reshape(3,5)
a

"""A NumPy array has a lot of meta-data associated with it describing its shape, datatype, etc."""

print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)
print(a.itemsize)
print(type(a))

help(a)

"""we can create an array from a list"""

b=np.array([1,2,3,4])
print(b)
print(b.dtype)
print(type(b))

"""we can create a multi-dimensional array of a specified size initialized all to 0 easily.  There is also an analogous ones() and empty() array routine.  Note that here we explicitly set the datatype for the array. 

Unlike lists in python, all of the elements of a numpy array are of the same datatype
"""

c=np.eye(10)
dtype=np.float64
c

"""`linspace` (and `logspace`) create arrays with evenly space (in log) numbers.  For `logspace`, you specify the start and ending powers (`base**start` to `base**stop`)"""

d=np.linspace(-1,2,15,endpoint=True)
print(d)

e=np.logspace(-1,2,15,endpoint=True,base=10)
print(e)

"""As always, as for help -- the numpy functions have very nice docstrings"""

help(np.logspace)

"""we can also initialize an array based on a function"""

f=np.fromfunction(lambda i,j:i==j,(3,3),dtype=int)
print(f)

"""# Array Operations

most operations (`+`, `-`, `*`, `/`) will work on an entire array at once, element-by-element.

Note that that the multiplication operator is not a matrix multiply (there is a new operator in python 3.5+, `@`, to do matrix multiplicaiton.

Let's create a simply array to start with
"""

a=np.arange(12).reshape(3,4)
print(a)

"""Multiplication by a scalar multiplies every element"""

a*2

"""adding two arrays adds element-by-element"""

a+a

"""multiplying two arrays multiplies element-by-element"""

a*a

"""We can think of our 2-d array a was a 3 x 5 matrix (3 rows, 5 columns).  We can take the transpose to geta 5 x 3 matrix, and then we can do a matrix multiplication"""

b=a.transpose()
b

a@b

"""We can sum along axes or the entire array"""

print(a)
a.sum(axis=1)

a.sum()

"""Also get the extrema"""

print(a.min(),a.max())

"""### universal functions

Up until now, we have been discussing some of the basic nuts and bolts of NumPy; now, we will dive into the reasons that NumPy is so important in the Python data science world.
Namely, it provides an easy and flexible interface to optimized computation with arrays of data.

Computation on NumPy arrays can be very fast, or it can be very slow.
The key to making it fast is to use *vectorized* operations, generally implemented through NumPy's *universal functions* (ufuncs).
This section motivates the need for NumPy's ufuncs, which can be used to make repeated calculations on array elements much more efficient.
It then introduces many of the most common and useful arithmetic ufuncs available in the NumPy package.

universal functions work element-by-element.  Let's create a new array scaled by `pi`
"""

b=a*np.pi/12.0
print(b)

c=np.cos(b)
print(c)

d=b+c

print(d)

"""## Array Slicing: Accessing Subarrays

Just as we can use square brackets to access individual array elements, we can also use them to access subarrays with the *slice* notation, marked by the colon (``:``) character.
The NumPy slicing syntax follows that of the standard Python list; to access a slice of an array ``x``, use this:
``` python
x[start:stop:step]
```
If any of these are unspecified, they default to the values ``start=0``, ``stop=``*``size of dimension``*, ``step=1``.
We'll take a look at accessing sub-arrays in one dimension and in multiple dimensions.
"""

a=np.arange(9)
a

"""Now look at accessing a single element vs. a range (using slicing)

Giving a single (0-based) index just references a single value
"""

a[3]

print(a[2:3])

a[2:4]

a[:]

"""## Multidimensional Arrays

Multidimensional arrays are stored in a contiguous space in memory -- this means that the columns / rows need to be unraveled (flattened) so that it can be thought of as a single one-dimensional array.  Different programming languages do this via different conventions:


Storage order:

* Python/C use *row-major* storage: rows are stored one after the other
* Fortran/matlab use *column-major* storage: columns are stored one after another

The ordering matters when 

* passing arrays between languages (we'll talk about this later this semester)
* looping over arrays -- you want to access elements that are next to one-another in memory
  * e.g, in Fortran:
  <pre>
  double precision :: A(M,N)
  do j = 1, N
     do i = 1, M
        A(i,j) = …
     enddo
  enddo
  </pre>
  
  * in C
  <pre>
  double A[M][N];
  for (i = 0; i < M; i++) {
     for (j = 0; j < N; j++) {
        A[i][j] = …
     }
  }  
  </pre>
  

In python, using NumPy, we'll try to avoid explicit loops over elements as much as possible

Let's look at multidimensional arrays:
"""

import numpy as np

a=np.arange(15).reshape(3,5)
a



"""Notice that the output of `a` shows the row-major storage.  The rows are grouped together in the inner `[...]`

Giving a single index (0-based) for each dimension just references a single value in the array
"""

a[1,1]

"""Doing slices will access a range of elements.  Think of the start and stop in the slice as referencing the left-edge of the slots in the array."""

a[0:2,0:2]

"""Access a specific column"""

a[:,1]

"""Sometimes we want a one-dimensional view into the array -- here we see the memory layout (row-major) more explicitly"""

a=a.flatten()
print(a)

"""we can also iterate -- this is done over the first axis (rows)"""

#print (a)
for raksha in a:
  print(raksha)
a=np.arange(15).reshape(3,5)
print(a)

"""or element by element"""

for e in a.flat:
  print(e)

help(a.flatten())

"""# Copying Arrays

simply using "=" does not make a copy, but much like with lists, you will just have multiple names pointing to the same ndarray object

Therefore, we need to understand if two arrays, `A` and `B` point to:
* the same array, including shape and data/memory space
* the same data/memory space, but perhaps different shapes (a _view_)
* a separate cpy of the data (i.e. stored completely separately in memory)

All of these are possible:
* `B = A`
  
  this is _assignment_.  No copy is made. `A` and `B` point to the same data in memory and share the same shape, etc.  They are just two different labels for the same object in memory
  

* `B = A[:]`

  this is a _view_ or _shallow copy_.  The shape info for A and B are stored independently, but both point to the same memory location for data
  
  
* `B = A.copy()`

  this is a _deep_ copy.  A completely separate object will be created in memory, with a completely separate location in memory.
  
Let's look at examples
"""

a=np.arange(10)
print(a)

"""Here is assignment -- we can just use the `is` operator to test for equality"""

b=a
b is a

"""Since `b` and `a` are the same, changes to the shape of one are reflected in the other -- no copy is made."""

b.shape=(2,5)
print(b)
a.shape

b is a

print(a)

"""a shallow copy creates a new *view* into the array -- the data is the same, but the array properties can be different"""

a=np.arange(12)
c=a[:]
a.shape=(3,4)
print(a)
print(c)

"""since the underlying data is the same memory, changing an element of one is reflected in the other"""

c[1]=-1
print(a)
print(c)

"""Even slices into an array are just views, still pointing to the same memory"""

d=c[3:8]
d

d[:]=0

print(a)
print(c)
print(d)

"""There are lots of ways to inquire if two arrays are the same, views, own their own data, etc"""

print(c is a)
print(c.base is a)
print(c.flags.owndata)
print(a.flags.owndata)

"""to make a copy of the data of the array that you can deal with independently of the original, you need a deep copy"""

d=a.copy()
d[:,:]=0.0
print(a)
print(d)

"""# Boolean Indexing

There are lots of fun ways to index arrays to access only those elements that meet a certain condition
"""

a=np.arange(12).reshape(3,4)
a

"""Here we set all the elements in the array that are > 4 to zero"""

a[a>4]=0
a

"""and now, all the zeros to -1"""

a[a==0]=-1
a

a==-1

"""if we have 2 tests, we need to use `logical_and()` or `logical_or()`"""

a=np.arange(12).reshape(3,4)
print(a)
a[np.logical_and(a>3,a<=9)]=0.0
a

"""Our test that we index the array with returns a boolean array of the same shape:"""

a>4

"""# Avoiding Loops

Python's default implementation (known as CPython) does some operations very slowly.
This is in part due to the dynamic, interpreted nature of the language: the fact that types are flexible, so that sequences of operations cannot be compiled down to efficient machine code as in languages like C and Fortran.
Recently there have been various attempts to address this weakness: well-known examples are the [PyPy](http://pypy.org/) project, a just-in-time compiled implementation of Python; the [Cython](http://cython.org) project, which converts Python code to compilable C code; and the [Numba](http://numba.pydata.org/) project, which converts snippets of Python code to fast LLVM bytecode.
Each of these has its strengths and weaknesses, but it is safe to say that none of the three approaches has yet surpassed the reach and popularity of the standard CPython engine.

The relative sluggishness of Python generally manifests itself in situations where many small operations are being repeated – for instance looping over arrays to operate on each element.

In general, you want to avoid loops over elements on an array.

Here, let's create 1-d x and y coordinates and then try to fill some larger array
"""

M=32
N=62
xmin=ymin=0.0
xmax=ymax=1.0

x=np.linspace(xmin,xmax,M,endpoint=False)
y=np.linspace(ymin,ymax,N,endpoint=True)

print(x.shape)
print(y.shape)
y

"""we'll time out code"""

import time
import numpy as np
M=32
N=62
xmin=ymin=0.0
ymax=ymax=1.0
x=np.linspace(xmin,xmax,M,endpoint=False)
y=np.linspace(ymin,xmax,N,endpoint=False)

t0=time.time()

g=np.zeros((M,N))

for i in range(M):
    for j in range(N):
        g[i,j]=np.sin(2.0*np.pi*x[i]*y[j])

t1=time.time()
print("time elapsed: {} s".format(t1-t0))

"""Now let's instead do this using all array syntax.  First will extend our 1-d coordinate arrays to be 2-d"""

x2d,y2d=np.meshgrid(x,y,indexing="ij")
print(x2d[:,0])
print(x2d[0,:])

print(y2d[:,0])
print(y2d[0,:])

t0=time.time()
g2=np.sin(2*.0*np.pi*x2d*y2d)
t1=time.time()
print("time elapsed: {} s".format(t1-t0))

"""## NumPy Standard Data Types

NumPy arrays contain values of a single type, so it is important to have detailed knowledge of those types and their limitations.
Because NumPy is built in C, the types will be familiar to users of C, Fortran, and other related languages.

The standard NumPy data types are listed in the following table.
Note that when constructing an array, they can be specified using a string:

```python
np.zeros(10, dtype='int16')
```

Or using the associated NumPy object:

```python
np.zeros(10, dtype=np.int16)
```

| Data type	    | Description |
|---------------|-------------|
| ``bool_``     | Boolean (True or False) stored as a byte |
| ``int_``      | Default integer type (same as C ``long``; normally either ``int64`` or ``int32``)| 
| ``intc``      | Identical to C ``int`` (normally ``int32`` or ``int64``)| 
| ``intp``      | Integer used for indexing (same as C ``ssize_t``; normally either ``int32`` or ``int64``)| 
| ``int8``      | Byte (-128 to 127)| 
| ``int16``     | Integer (-32768 to 32767)|
| ``int32``     | Integer (-2147483648 to 2147483647)|
| ``int64``     | Integer (-9223372036854775808 to 9223372036854775807)| 
| ``uint8``     | Unsigned integer (0 to 255)| 
| ``uint16``    | Unsigned integer (0 to 65535)| 
| ``uint32``    | Unsigned integer (0 to 4294967295)| 
| ``uint64``    | Unsigned integer (0 to 18446744073709551615)| 
| ``float_``    | Shorthand for ``float64``.| 
| ``float16``   | Half precision float: sign bit, 5 bits exponent, 10 bits mantissa| 
| ``float32``   | Single precision float: sign bit, 8 bits exponent, 23 bits mantissa| 
| ``float64``   | Double precision float: sign bit, 11 bits exponent, 52 bits mantissa| 
| ``complex_``  | Shorthand for ``complex128``.| 
| ``complex64`` | Complex number, represented by two 32-bit floats| 
| ``complex128``| Complex number, represented by two 64-bit floats|

More advanced type specification is possible, such as specifying big or little endian numbers; for more information, refer to the [NumPy documentation](http://numpy.org/).
NumPy also supports compound data types, which will be covered in [Structured Data: NumPy's Structured Arrays](02.09-Structured-Data-NumPy.ipynb).

## Array Concatenation and Splitting

All of the preceding routines worked on single arrays. It's also possible to combine multiple arrays into one, and to conversely split a single array into multiple arrays. We'll take a look at those operations here.

### Concatenation of arrays

Concatenation, or joining of two arrays in NumPy, is primarily accomplished using the routines ``np.concatenate``, ``np.vstack``, and ``np.hstack``.
``np.concatenate`` takes a tuple or list of arrays as its first argument, as we can see here:
"""

x=np.array([1,2,3,4])
y=np.array([4,3,2,1])
np.concatenate([y,x])

"""You can also concatenate more than two arrays at once:"""

z=[9,4,6]
print(np.concatenate([x,y,z]))

"""It can also be used for two-dimensional arrays:"""

grid=np.array([[10,20,30],
              [40,50,60]])

# concatenate along the first axis
np.concatenate([grid,grid])

# concatenate along the second axis (zero-indexed)
np.concatenate([grid,grid],axis=1)

"""### Splitting of arrays

The opposite of concatenation is splitting, which is implemented by the functions ``np.split``, ``np.hsplit``, and ``np.vsplit``.  For each of these, we can pass a list of indices giving the split points:
"""

x=[1,2,3,4,4,3,2,1,9,4,6]
x1,x2,x3,x4=np.split(x,[3,5,8])
print(x1,x2,x3,x4)

"""Notice that *N* split-points, leads to *N + 1* subarrays.
The related functions ``np.hsplit`` and ``np.vsplit`` are similar:
"""

grid=np.arange(25).reshape((5,5))
grid

left,right=np.hsplit(grid,[2])
print(left)
print(right)

"""### Aggregates

For binary ufuncs, there are some interesting aggregates that can be computed directly from the object.
For example, if we'd like to *reduce* an array with a particular operation, we can use the ``reduce`` method of any ufunc.
A reduce repeatedly applies a given operation to the elements of an array until only a single result remains.

For example, calling ``reduce`` on the ``add`` ufunc returns the sum of all elements in the array:
"""

x=np.arange(1,9)
print(x)
np.add.reduce(x)

"""Similarly, calling ``reduce`` on the ``multiply`` ufunc results in the product of all array elements:"""

np.multiply.reduce(x)

"""If we'd like to store all the intermediate results of the computation, we can instead use ``accumulate``:"""

np.add.accumulate(x)

np.multiply.accumulate(x)

