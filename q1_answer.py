# Create a function in python to read the text file and replace specific content of the file.

def replace_content(file_name, old_content, new_content):
    with open(file_name, 'r') as f:
        data = f.read()
        data = data.replace(old_content, new_content)
        with open(file_name, 'w') as f:
            f.write(data)


if __name__ == '__main__':
    replace_content('example.txt', 'placement', 'screening')
    print('File content has been replaced')