def write_file(file_name, file_content):
    with open(f'{file_name}.txt', 'w') as x:
        x.write(file_content)


def append_file(file_name, append_content):
    with open(f'{file_name}.txt', 'a') as x:
        x.write(append_content)

def read_file(file_name):
    with open(f'{file_name}.txt', 'r') as x:
        return x.read()
