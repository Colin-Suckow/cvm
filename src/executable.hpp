#pragma once

#include "types.hpp"
#include <vector>

class CvmExe
{
private:
    addr_t mCodeLocation;
    std::vector<uint8_t> mCodeData;
};