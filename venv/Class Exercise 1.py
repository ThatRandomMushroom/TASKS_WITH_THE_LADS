

def gen_pattern(word, length):
    for i in range(0, length):
        for j in range(length - i - 1):
        print(' ', end="")
        for j in range(0, i + 1):
            print(word[j], end="")
        for k in range(i - 1, -1, -1):
            print(word[k], end="")
        print()
    for l in range(1, length):
        for j in range(l):
         print(' ', end="")
        for m in range(0, length - l - 1):
            print(word[m], end="")
        for n in range(length - l - 1, -1, -1):
            print(word[n], end="")
        print()

def call():
    word=input("Enter characters: ")
    length=len(word)
    gen_pattern(word, length)

call()


def gen_pattern(char, length):
    dots = (length*2 - 1)*2 - 1
    string = ''
    string_list = []
    for i in range(length):
        string1 = ''
        string += char[i]
        length1 = len(string)
        for j in range(0, length1):
            if j % 2 != 0:
                string1 += char[length -1 - j].center(3, '.')
            else:
                string1 += char[length - 1 - j]
        for k in range(i - 1, -1, -1):
            if k % 2 != 0:
                string1 += char[length - 1 - k].center(3, '.')
            else:
                string1 += char[length - 1 - k]
        string1 = string1.center(dots, '.')
        string_list.append(string1)
    return string_list


def run():
    char = input("Enter characters")
    length =len(char)
    string_list = gen_pattern(char, length)
    print('\n'.join(string_list))
    bottom_of_diamond_string_list = list(reversed(string_list))[1:]
    print('\n'.join(bottom_of_diamond_string_list))

run()