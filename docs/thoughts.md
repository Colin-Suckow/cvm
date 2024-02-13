## Encoding

There's an interesting trade off between placing complexity in the ISA or in the generated code. Moving complexity into the ISA specification can make the generated code quite a bit smaller, but at the cost of a slower, more complicated runtime.

For example, let's consider jumping into a subroutine and back again. The easiest way to provide runtime support would be to just add an unconditional jump. Obivously this would be pretty easy to implement. However doing so would force the compiler to generate code to keep track of the return address, then jump back to it after the function was complete. 

This the simplicity might be worth the program length cost because it leaves more options open to the compiler. For now I'll add instructions under this assumption. If it doesn't work out then we can re-evalulate.