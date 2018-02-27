/**
 * arm-linux-androideabi-gcc test.c -o test -ldl -pie
 * export LD_LIBRARY_PATH=./
 * cp test /path/to/libclient.so
 */
#include <stdio.h>
#include <dlfcn.h>
int main(int argc, char *argv[]){  
    void (*Py_Initialize)();
    void (*PyRun_SimpleString)(char *);
    void (*Py_Finalize)();
    if (argc < 2) {
        printf("Usage: %s script.py\n", argv[0]);
        return;
    }
    FILE *fp = fopen(argv[1], "rb");
    fseek(fp, 0, SEEK_END);
    int file_len = ftell(fp);
    char *buf = (char *)malloc(file_len + 1);
    fseek(fp, 0, SEEK_SET);
    fread(buf, file_len, 1, fp);
    buf[file_len] = 0;
    void *libm_handle = dlopen("libclient.so", RTLD_LAZY );
    if (!libm_handle){
        printf("Open Error:%s.\n", dlerror());
        return 0;
    }
    Py_Initialize = dlsym(libm_handle, "Py_Initialize");
    Py_Initialize();
    PyRun_SimpleString = dlsym(libm_handle, "PyRun_SimpleString");
    PyRun_SimpleString(buf);
    Py_Finalize = dlsym(libm_handle, "Py_Finalize");
    Py_Finalize();
    dlclose(libm_handle);
    free((void *)buf);
    return 0;
}