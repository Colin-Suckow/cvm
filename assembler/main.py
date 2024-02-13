# This is a dumb assembler just for testing.
import argparse
import assembler

def main():
    parser = argparse.ArgumentParser(
        prog="CvmAsm",
        description="Poorly assembles programs"
    )

    parser.add_argument('filename')

    args = parser.parse_args()

    with open(args.filename, "r") as f:
        file_str = f.read()
    
    assembler.assemble(file_str)

if __name__ == "__main__":
    main()