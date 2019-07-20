# what have I done >:(
# This is a python script that generates c++ classes, each in their own file.
# It creates a ton of files so be careful. I tested 1000 classes (2000 files) and 
# survived but your storage media might not or your operating system might not be 
# able to handle listing the folder. NO WARRANTY
n = 10 # number of classes to output
mainFile = open("main.cpp", "w")
mainFile.write("#include <stdio.h>\n")
for i in range(n):
    hFile = open(f"class{i}.h", "w")
    hFile.write(f"#ifndef CLASS_{i}_H\n")
    hFile.write(f"#define CLASS_{i}_H\n")
    hFile.write(f"""class Class{i} {{
    public:
        virtual void foo();
}};\n""")
    hFile.write(f"#endif")
    hFile.close()
    srcFile = open(f"class{i}.cpp", "w")
    srcFile.write(f"#include \"class{i}.h\"\n")
    srcFile.write(f"""void Class{i}::foo() {{
}}""")
    srcFile.close()

    mainFile.write(f"#include \"class{i}.h\"\n")


mainFile.write("int main() {\n")
for i in range (n):
    continue
    #mainFile.write(f"    Class{i} class{i};\n")
    #mainFile.write(f"    class{i}.foo();\n")

mainFile.write("""    printf("it works\\n");\n    return 0;\n}""")
mainFile.close()