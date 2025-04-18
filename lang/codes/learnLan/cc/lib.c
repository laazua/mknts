// c常用头文件
/**
////////////////////////// <ctype.h>
// int iscntrl(int c)
// int isalnum(int c)
// int isascii(int c)
// int isblank(int c)
// int isdigit(int c)
// int isgraph(int c)
// int islower(int c)
// int isprint(int c)
// int ispunct(int c)
// int isspace(int c)
// int isupper(int c)
// int isxdigit(int c)
// int toasscii(int c)
// int tolower(int c)
// int toupper(int c)
////////////////////////// <time.h>
// clock_t clock(void)                         确定处理器时间函数
// time_t time(time_t *tp)                     返回当前日历时间
// time_t mktime(struct tm *tp)                将分段时间值转换为日历时间值
// char *asctime(const struct tm *tblock)      转换日期和时间为ASCII码
// char *ctime(const time_t *time)             把日期和时间转换为字符串
// struct tm *gmtime(const time_t *timer)      把日期和时间转换为格林尼治标准时间
// struct tm *localtime(const time_t *timer)   把日期和时间转为结构
// double difftime(time_t time2, time_t time1) 计算两个时刻之间的时间差
// size_t strftime(char *s, size_t smax, const char *fmt, const struct tm *tp) 根据fmt的格式要求将*tp中的日期与时间转换为指定格式
///////////////////////// <stdio.h>
// int printf(char *format...)   产生格式化输出的函数
// int getchar(void)             从键盘上读取一个键,并返回该键的值
// int putchar(char c)           在屏幕上显示字符c
// int fflush(FILE *stream)      清除一个流
// int fclose(FILE *stream)      关闭一个文件
// int remove(char *filename)    删除一个文件
// FILE *tmpfile(void)           以二进制方式打开暂存文件
// char *tmpname(char *sptr)     创建一个唯一的文件名
// int setvbuf(FILE *stream, char *buf, int type, unsigned size)   把缓冲区与流相关
// int fprintf(FILE *stream, char *format[, argument, ...])        传送格式化输出到一个流中
// int scanf(char *format[,argument,...])                          执行格式化输入
// int fscanf(FILE *stream, char *format[, argument, ...])         从一个流中执行格式化输入
// int fgetc(FILE *stream)                                         从流中读取字符
// char *fgets(char *string, int n, FILE *stream)                  从流中读取字符串
// int fputc(int ch, FILE *stream)                                 送一个字符到流中
// int fputs(char *string, FILE *stream)                           送一个字符串到流中
// int getc(FILE *stream)                                          从流中取字符
// int getchar(void)                                               从stdin流中读取字符
// char *gets(char *string)                                        从流中取字符串
// int putchar(int ch)                                             在stdout上输出字符
// int puts(char *string)                                          送一字符串到流中
// int ungetc(char c, FILE *stream)                                把一个字符退回到输入流中
// int fread(void *ptr, int size, int nitems, FILE *stream)        从流中读取数据
// int fwrite(void *ptr, int size, int nitems, FILE *stream)       写内容到流中int fseek
// (FILE *stream, long offset, int fromwhere)                      重新定位流上的文件指针
// long ftell(FILE *stream)                                        返回当前文件指针
// int rewind(FILE *stream)                                        将文件指针重新指向一个流的开头
// int fgetpos(FILE *stream, const fpos_t *pos)                    定位流上的文件指针
// void clearerr(FILE *stream)                                     复位错误标志
// int feof(FILE *stream)                                          检测流上的文件结束符
// int ferror(FILE *stream)                                        检测流上的错误
// void perror(char *string)                                       系统错误信息
// FILE *freopen(char *filename, char *type, FILE *fp)             打开一个文件,并将该文件关联到fp指定的流
// FILE *fopen(char *filename, char *type)                         打开一个文件
// int rename(char *oldname, char *newname)                        重命名文件
/////////////////////////////////////////////// <stdlib.h>
// char *itoa(int i)     把整数转换成字符串
// void exit(int retval) 结束程序
// double atof(const char *s)                                      将字符串s转换为double类型
// int atoi(const char *s)                                         将字符串s转换为int类型
// long atol(const char *s)                                        将字符串s转换为long类型
// double strtod(const char *s, char **endp)                       将字符串s前缀转换为double型
// long strtol(const char *s, char **endp, int base)               将字符串s前缀转换为long型
// unsinged long strtol(const char *s, char **endp, int base)      将字符串s前缀转换为unsinged long型
// int rand(void)       产生一个0-RAND_MAX之间的伪随机数
// void srand(unsigned int seed)                                   初始化随机数发生器
// void *calloc(size_t nelem, size_t elsize)                       分配主存储器
// void *malloc(unsigned size)                                     内存分配函数
// void *realloc(void *ptr, unsigned newsize)                      重新分配主存
// void free(void *ptr)                                            释放已经分配的内存块
// void abort(void)                                                异常终止一个进程
// void exit(int status)                                           终止应用程序
// int atexit(atexit_t func)                                       注册终止函数
// char *getenv(char *envvar)                                      冲环境中读取字符串
// void *bsearch(const void *key, const void *base, size_t *nelem, size_t width, int(*fcmp)(const void *, const *))  二分法搜索函数
// void qsort(void *base, int nelem, int width, int(*fcmp)())      使用快速排序例程进行排序
// int abs(int i)
// long labs(long n)
// div_t div(int number, int denom)                                将两个整除相除,返回商和余数
// ldiv_t ldiv(long lnumber, long ldenom)                          将两个长整型数相除,返回商和余数
////////////////////////////////////////////////////// <math.h>
// float fabs(faloat x)  求浮点数x的绝对值
// int abs(int x)        求整数x的绝对值
// float acos(float x)   求x(弧度表示)的反余弦值
// float asin(float x)   求x(弧度表示)的反正弦值
// float atan(float x)   求x(弧度表示)的反正切值
// float atan2(float y, float x)  求y/x(弧度表示)的反正切值
// float ceil(float x)   求不小于x的最小整数
// float cos(float x)    求x(弧度表示)的余弦值
// float cosh(float x)   求x的双曲余弦值
// float exp(float x)    求e的x次幂
// float floor(float x)  求不大于x的最大整数
// float fmod(float x, float y)  计算x/y的余数
// float frexp(float x, int *exp)  把浮点数x分解成尾数和指数
// float ldexp(float x, int exp)   返回x*2^exp的值
// float modf(float num, float *i) 将浮点数num分解成整数部分和小数部分
// float hypot(float x, float y)   对于给定的直角三角形的两个直角边,求斜边长度
// float log(float x)    计算x的自然对数
// float log10(float x)  计算x的常用对数
// float pow(float x, float y)     计算x的y次幂
// float pow10(float x)  计算10的x次幂
// float sin(float x)    计算x(弧度表示)的正弦值
// float sinh(float x)   计算x(弧度表示)的双曲线值
// float sqrt(float x)   计算x的平方根
// float tan(float x)    计算x(弧度表示)的正切值
// float tanh(float x)   求x的双曲正切值
////////////////////////////////////////////////// <string.h>
// int bcmp(const void *s1, const void *s2, int n)                        比较字符串s1和s2的前n个字节是否相等
// void bcopy(const void *src, void *dest, int n)                         将字符串src的前n个字节复制到dest中
// void bzero(void *s, int n)                                             将字节字符串s的前n个字节置为零
// void *memccpy(void *dest, void *src, unsigned char ch, unsigned int count) 有src所指内存区域复制不多于count个字节到dest所指内存区域,如果遇到字符ch则停止复制
// void *memcpy(void *dest, void *src, unsigned int count)                由src所指内存区域复制count个字节到dest所指内存区域
// void *memchr(void *buf, char ch, unsigned count)                       从buf所指内存区域的前count个字节查找字符ch
// int memcmp(void *buf1, void *buf2, unsigned int count)                 比较内存区域buf1和buf2的前count个字节
// int memicmp(void *buf1, void *buf2, unsigned int count)                比较内存区域buf2和buf2的前count个字节但不区分字母的大小写
// void *memmove(void *dest, const void *src, ungigned int count)         由src所指内存区域复制count个字节到dest所指内存区域 
// void *memset(void *buffer, int c, int count)                           把buffer所指内存区域的前count个字节设置成字符o
// void setmem(void *buf, unsigned int count, char ch)                    把buf所指内粗区域前count个字节设置成字符ch
// void movmem(void *src, void *dest, unsigned int count)                 由src所指内存区域复制count个字节到dest所指内存区域
// char *stpcpy(char *dest, char *src)                                    把src所指由NULL结束的字符复制到dest所指的数组中
// char *strcpy(char *dest, char *src)                                    把src所指由NULL结束的字符复制到dest所指的数组中
// char *strcat(char *dest, char *src)                                    把src所指的字符串添加到dest结尾处(覆盖dest结尾处的'\0')并添加'\0'
// char *strchr(char *s, char c)                                          查找字符串s中首次出现字符c的位置
// int strcmp(char *s1, char *s2)                                         比较字符串s1和s2
// int stricmp(char *s1, char *s2)                                        比较字符串s1和s2,但不区分大小写
// int strcspn(char *s1, char *s2)                                        在字符串s1中搜寻s2中出现的字符
// char *strdup(char *s)                                                  复制字符串s
// int strlen(char *s)                                                    计算字符串s的长度
// char *strlwr(char *s)                                                  将字符串s转换成小写
// char *strupr(char *s)                                                  将字符串s转换成大写
// char *strncat(char *dest, char *src, int n)                            把src所指zifuc的前n个字符添加到dest结尾处(覆盖dest结尾处的'\0')并在结尾处添加'\0'
// int strcmp(char *s1, char *s2, int n)                                  比较字符串s1和s2的前n个字符
// int strnicmp(char *s1, char *s2, int n)                                比较s1和s2的前n个字符但不区分大小写
// char *strncpy(char *dest, char *src, int n)                            把src所指由NULL结束的字符串的前n个字节复制到dest所指的数组中
// char *strpbrk(char *s1, char *s2)                                      在字符串s1中寻找字符串s2中任何一个字符相匹配的第一个字符的位置,空字符NULL不包括在内
// char *strrev(char *s)                                                  把字符串s的所有字符的顺序颠倒过来(不包括NULL)
// char *strset(char *s, chr c)                                           把字符串s中的所有字符都设置成字符c
// char *strstr(char *haystack, char *needle)                             从字符串haystack中寻找needle第一次出现的位置(不比较结束符NULL)
// char *strtok(char *s, char *delim)                                     分解字符串为一组标记串,s为要分解的字符串,delim为分割字符串
// int strnicmp(char *s1, char *s2, int n)                                比较字符串s1和s2的前n个字符但不区分大小写
**/