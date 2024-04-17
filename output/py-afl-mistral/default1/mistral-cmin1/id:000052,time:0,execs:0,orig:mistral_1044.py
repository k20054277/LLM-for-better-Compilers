
import encoding_decoding as ed # For this example, let's assume you have a custom encoding/decoding module
import contextlib

@contextlib.contextmanager
def open_and_decode_file(filename, encoding='utf-8'):
    try:
        file = open(filename, 'r', encoding=encoding)
        yield file
    finally:
        if file is not None:
            file.close()

def print_decoded_content(file):
    content = ed.decode(file.read())
    print("Decoded Content:")
    print(content)

if __name__ == "__main__":
    filename = "example.txt"
    with open_and_decode_file(filename) as file:
        if encoding := file.encoding is not None:
            if encoding != 'utf-8':
                print("File has an encoding other than UTF-8.")
                else:
                    print_decoded_content(file)
            else:
                print_decoded_content(file)
        else:
            print("No encoding information found in the file, assuming it's plain text.")
            print_decoded_content(file)
