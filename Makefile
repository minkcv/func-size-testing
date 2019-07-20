main:
	g++ -Wall *.cpp -o main

all:
	clean main

clean:
	rm -rf main