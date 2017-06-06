def compare_binary(file_1, file_2):
    with open(file_1, 'rb') as file1, open(file_2, 'rb') as file2:
        data1 = file1.read()
        data2 = file2.read()

    if data1 != data2:
        return False
    return True


def is_in(pattern, file_1):
    with open(file_1, 'rb') as file1:
        data1 = file1.read()

    return pattern in data1


def same_filesize():
    pass


def same_datetime():
    pass


def same_filename():
    pass


def same_extension():
    pass
