# CVM ISA

## TL;DR
* Little endian.
* Bytecode format with variable length opcodes
    * Each instruction starts with a 1 byte opcode. Opcode type defines total instruction length.
* Addresses are 64 bit.
* Generally stack based
* Registers
    * PC
* Hardvard Architecture
    * Stack stored seperately from main memory space

## Call convention

All the different bits get pushed onto the stack. First return address, then all the arguments. Return value will be placed on top of the stack. Return addter and arguments will be left behind. It is the caller's responsiblity to clean up.

## rtcalls

Calls to the runtime.

### putc
Id: 0x0

arg1: byte, character
Pushes the first arg out stdout

## Memory Space

* Downward growing stack

## Instructions

### NOP
0x00

Total Length: 1 byte

It's a NOP, what you'd expect.

[ NOP ]

### JMP
0x01

Total Length: 9 bytes

Unconditionally jumps to the given address

[ JMP ] -> [8 byte addr]

### LOAD8
0x03

Total Length: 9 bytes

Loads a byte from addr and pushes it on the stack

[ LOAD8 ] -> [8 byte addr]

### LOAD16
0x04

Total Length: 9 bytes

Loads a 16 bit word from addr and pushes it on the stack.

[ LOAD16 ] -> [8 byte addr]

### LOAD32
0x05

Total Length: 9 bytes

Loads a 32 bit word from addr and pushes it on the stack.

[ LOAD32 ] -> [8 byte addr]

### LOAD64
0x06

Total Length: 9 bytes

Loads a 64 bit word from addr and pushes it on the stack.

[ LOAD64 ] -> [8 byte addr]

## STORE8
0x07

Total Length: 9 bytes

Pops one byte off the stack and stores it at addr.

[ STORE8 ] -> [8 byte addr]

## STORE16
0x08

Total Length: 9 bytes

Pops one 16 bit word off the stack and stores it at addr.

[ STORE16 ] -> [8 byte addr]

## STORE32
0x09

Total Length: 9 bytes

Pops one 32 bit word off the stack and stores it at addr.

[ STORE32 ] -> [8 byte addr]

## STORE64
0x0A

Total Length: 9 bytes

Pops one 64 bit word off the stack and stores it at addr.

[ STORE64 ] -> [8 byte addr]

## RTCALL
0x0B

Total Length: 2 bytes

Instructs the interpreter to execute a runtime call with the id stored in the operand byte. Arguments are stored on stack and the return value will be placed on the top of the stack on return.

[ SYSCALL ] -> [ SYSCALL ID ]


