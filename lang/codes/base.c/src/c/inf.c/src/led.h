#ifndef __LED_H
#define __LED_H

#include "light.h"

struct LedImpl {
    struct LightInterface *inf;
    int state;
};

int NewLedImpl(struct LedImpl *self);

#endif // __LED_H
