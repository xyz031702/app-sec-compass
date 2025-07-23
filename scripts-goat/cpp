// vulnerable.cpp
#include <cstdio>
#include <cstring>
#include <cstdlib>

void copyUserInput(const char* input)
{
    char buf[64];
    // CWE‑120: buffer overflow – Cppcheck: 'strcpy' called with dest size 64
    strcpy(buf, input);
    printf("You entered: %s\n", buf);
}

int* danglingPointer()
{
    int local = 42;
    // Cppcheck: returning address of local variable
    return &local;
}

void leakMemory()
{
    int* data = new int[100];
    // do something with data …
    // Cppcheck: memory leak – ‘data’ not freed
}

int main(int argc, char* argv[])
{
    if (argc > 1)
        copyUserInput(argv[1]);

    int* ptr = danglingPointer();
    // dereferencing an invalid pointer – undefined behaviour
    printf("Dangling value: %d\n", *ptr);

    leakMemory();
    return 0;
}
