import re

def main():
    s1 = "a b,c-d"
    s_list = re.split("[\s,-]", s1)
    print(s_list)


if __name__ == '__main__':
    main()