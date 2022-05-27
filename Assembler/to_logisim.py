import argparse
import os


def parse(input_file: str, output_file: str):
    with open(input_file, 'r') as in_file:
        data = in_file.read()

    with open(output_file, 'wb') as out_file:
        out_file.write(b'v2.0 raw\r\n')
        counter = 1
        for char in data:
            out_file.write(hex(ord(char))[2:].encode())
            if not counter % 8:
                out_file.write(b'\r\n')
            else:
                out_file.write(b' ')


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('input_file')
    argparser.add_argument('output_file')
    args = argparser.parse_args()

    if not os.path.isfile(args.input_file):
        raise FileNotFoundError(f'{args.input_file} does not exist')

    parse(args.input_file, args.output_file)


if __name__ == "__main__":
    main()
