#pragma once

#include "types.hpp"

class I_Memory
{
public:
    I_Memory(){};

    virtual uint8_t read8(addr_t addr) = 0;
    virtual void write8(addr_t addr, uint8_t val) = 0;
};