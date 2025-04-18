#include "led.h"
#include "light.h"

int LedOn(struct LedImpl *self);
int LedOff(struct LedImpl *self);
int LedState(struct LedImpl *self);

struct LightInterface LedInf = {
        .on = (LightOnFun)LedOn,
        .off = (LightOffFun)LedOff,
        .state = (LightStateFun)LedState,
};


int LedOn(struct LedImpl *self)
{
    self->state = 1;
    return 0;
}

int LedOff(struct LedImpl *self)
{
    self->state = 0;
    return 0;
}

int LedState(struct LedImpl *self)
{
    return self->state;
}

int NewLedImpl(struct LedImpl *self)
{
    self->inf = &LedInf;
    self->state = 0;
    return 0;
}
