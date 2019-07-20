# size_fsckery

This repository aims to answer the question:

How much space does it take up on disk and in memory when you have lots of classes with virtual functions?

### A longer explanation perhaps?

For private member fields you can expect the size to be consistent with the member's type. Example:

    class Class0 {
        private:
            uint64_t data; // I think it's going to be 64 bits
    }

But how much space does an empty virtual function take up.

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


