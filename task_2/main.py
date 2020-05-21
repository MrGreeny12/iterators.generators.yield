import hashlib

def generator(file_path):
    with open(file_path, 'r') as target_file:
        for file_str in target_file:
            line = target_file.readline()
            hash_obj = hashlib.md5(line.encode())
            yield hash_obj

if __name__ == '__main__':
    for hash_obj in generator('test.txt'):
        print(hash_obj.hexdigest())