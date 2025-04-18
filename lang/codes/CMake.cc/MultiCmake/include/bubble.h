// 冒泡
//
//

#ifndef _BUBBLE_H_
#define _BUBBLE_H_

class Bubble
{
private:
    int len;
    int *numbers;
public:
    Bubble(int len, int *numbers);
    void sort(void);
};

#endif // _BUBBLE_H_
