 # what have I done >:(
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

mainFile.write(f"""int main() {{
    Class{i} class{i};
    printf("it works\\n");
    return 0;
}}
""")
mainFile.close()