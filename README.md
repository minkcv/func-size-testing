# func-size-testing

This repository aims to answer the question:

How much space does it take up on disk and in memory when you have lots of classes with virtual functions?

### A longer explanation perhaps?

For private member fields you can expect the size to be consistent with the member's type. Example:

    class Class0 {
        private:
            uint64_t data; // I think it's going to be 64 bits for each instance at runtime
    }

But how much space does an empty virtual function take up?

class0.h

    #ifndef CLASS_0_H
    #define CLASS_0_H
    class Class0 {
        public:
            virtual void foo();
    };
    #endif

class0.cpp

    #include "class0.h"
    void Class0::foo() {
    }

The python script [virtual-lookup-table-size-for-many-classes.py](./virtual-lookup-table-size-for-many-classes.py) contains code to generate a great number of classes, as well as a main file that includes them all.

The make file [Makefile](./Makefile) allows them to be compiled on linux with g++

    cd size_fsckery
    make
    ./main

Output:

    it works

The results can be controlled by the variable `n` in the python script.

    n = 10 # number of classes to output

Lets create 1000 C++ classes with virtual functions and see how big the final binary is.

# Some approximate results:

Just including 10 classes with virtual functions:

    15 KB

10 classes with non virtual functions:

    9 KB

10 classes with no function:

    9 KB

1000 classes with virtual functions:

    398 KB

1000 classes with non virtual functions:

    139 KB

1000 classes with no function:

    45 KB

# The real results

Yeah, virtual functions made our binary larger, but 1000 classes took a decent amount of time to compile and that's also annoying.

TODO: compile with -g and attach with gdb and check runtime memory consumption