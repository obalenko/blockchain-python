import hashlib
import json

def crypto_hash(*args):
    '''
    Return a sha-256 hash of the given arguments
    :param data:
    :return:
    '''
    strngified_args = sorted(map(lambda data: json.dumps(data), args))
    joined_data = ''.join(strngified_args)
    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()


def main():
    print(f'crypto_hash(1, 2, 3): {crypto_hash(1, 2, 3)}')

if __name__ == '__main__':
    main()