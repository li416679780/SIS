#####逆向分析静态编译并裁减了符号表的二进制文件
1. 使用lscan来比对引入函数量的动态库
2. 把识别出的签名库拷贝到IDA的sig文件夹下，使用File\->Load File\->FLIRT signature file功能，加载这个签名库，来识别出一些静态编译在程序中的函数
   https://github.com/maroueneboubakri/lscan

