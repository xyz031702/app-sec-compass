// vuln2.cpp
#include <cstdio>
#include <cstdlib>

void readFileToBuffer(const char* path)
{
    FILE* f = fopen(path, "rb");
    if (!f) return;

    char* buf = new char[256];           // heap allocation
    size_t n = fread(buf, 1, 512, f);    // Cppcheck: reading past buffer size, return value not checked properly
    (void)n;                             // pretend to use n

    fclose(f);
    delete buf;                          // Cppcheck: should be delete[] (mismatched deallocation)
}

int uninitExample()
{
    int x;                               // Cppcheck: uninitialized variable
    if (x > 0)                           // undefined behaviour
        return x;
    return -1;
}

void doubleFree()
{
    int* p = (int*)malloc(sizeof(int));
    *p = 7;
    free(p);
    free(p);                             // Cppcheck: double free
}

int main(int argc, char* argv[])
{
    if (argc > 1)
        readFileToBuffer(argv[1]);

    int val = uninitExample();
    printf("Value: %d\n", val);

    doubleFree();
    return 0;
}
