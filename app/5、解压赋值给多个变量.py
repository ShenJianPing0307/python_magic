
def main():
    s1 = "abcde"
    first, *middle, five = s1
    print(first, five)
    print(middle)

def test(*args, **kwargs):
    pass

if __name__ == '__main__':
    main()