#pragma once

#include <vector>

#include "I_memory.hpp"
#include "types.hpp"
#include "executable.hpp"

const uint32_t MAX_STACK_SIZE = 32768;

class Interpreter
{
public:
    Interpreter();
    ~Interpreter();
    void reset();
    void load_executable(CvmExe& exe);
    void execute_instruction(I_Memory& mem);
private:
    std::vector<uint8_t> mStack{};
};