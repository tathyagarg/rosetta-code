# https://rosettacode.org/wiki/Read_a_specific_line_from_a_file

def main(file, line=12):
    with open(file, 'r') as f:
        text = f.readlines()
    print(text[line].strip())

if __name__ == '__main__':
    main('file.txt')
