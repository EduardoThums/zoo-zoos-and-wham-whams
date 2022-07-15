import sys

BASE_2_TABLE = [128, 64, 32, 16, 8, 4, 2, 1]


def main():
    if len(sys.argv) < 2:
        print('Missing decimal argument')
        exit(1)

    try:
        decimal = original_decimal = int(sys.argv[1])

        if decimal > 255:
            print('Eight bit decimal out of range. Valid ranges are 0-255')
            exit(1)

    except Exception as e:
        print('Invalid decimal argument')
        raise e

    binary = ''

    for base_2 in BASE_2_TABLE:
        if decimal >= base_2:
            decimal -= base_2
            binary += '1'

        else:
            binary += '0'

    print(f'The binary of {original_decimal} is {binary}')


if __name__ == '__main__':
    main()
