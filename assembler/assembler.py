class AssemblerState:
    def __init__(self, source):
        self.source = source

        self.segments = {}
        self.current_segment = "code"
        self.segment_offset = 0

        self.instructions = []
        self.labels = {}


    def assemble(self):
        for line in self.source.splitlines():
            tokens = line.strip().split(" ")
            if tokens[0] == "":
                # Empty line
                continue
            
            if tokens[0][0] == "#":
                # Comment
                continue

            inst = tokens[0]

            if inst == "PUSH":
                print("It's a push")

            else:
                print(f"Unknown instruction! {inst}")




def assemble(code_str):
    state = AssemblerState(code_str)

    return state.assemble()