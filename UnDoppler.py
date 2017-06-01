from lib.signatures import SIGNATURES


def is_jpeg(filepath):
    with open(filepath, 'rb') as file:
        first_four_bytes = file.read(4)

        if first_four_bytes in SIGNATURES.get('jpg').get_signatures():
            print("JPEG detected.")
        else:
            print("File does not look like a JPEG.")


def compare_binary(file_1, file_2):
    with open(file_1, 'rb') as file1, open(file_2, 'rb') as file2:
        data1 = file1.read()
        data2 = file2.read()

    if data1 != data2:
        print("Files do not match.")
    else:
        print("Files match.")
