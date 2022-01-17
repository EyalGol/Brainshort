from config import OPCODE_MAP
import argparse
import struct
import os


def get_opcode(char: chr) -> bytes:
    try:
        opcode = OPCODE_MAP[char]
    except KeyError:
        raise RuntimeError(f'{char} is an invalid character')
    return struct.pack('>H', opcode)[:1]

def parse(input_file: str, output_file: str, logism_format: bool = False):
    with open(input_file, 'r') as in_file:
        data = in_file.read()
    
    with open(output_file, 'wb') as out_file:
        if logism_format:
            out_file.write(b'v2.0 raw\r\n')
            couter = 1
            for char in data:
                out_file.write(hex(OPCODE_MAP[char])[2].encode())
                if not couter % 8:
                    out_file.write(b'\r\n')
                elif not couter % 2:
                    out_file.write(b' ')
                couter = (couter % 8) + 1
        else:
            for char in data:
                out_file.write(get_opcode(char))

def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('input_file')
    argparser.add_argument('output_file')
    argparser.add_argument('-ls','--logism_format', action='store_true', help='This is to create an output file Logism (the program I use for simulation) accepts')

    args = argparser.parse_args()

    if not os.path.isfile(args.input_file):
        raise FileNotFoundError(f'{args.input_file} does not exist')

    parse(args.input_file, args.output_file, args.logism_format)


    









if __name__ == "__main__":
    main()