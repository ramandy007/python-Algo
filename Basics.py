import os
# 1


def q1():
    s = input("Enter a string: ")

    # s=s.split(" ");
    str_Capitalize = [x.capitalize() for x in s.split(" ")]

    # print(str_Capitalize)
    s = ""
    for x in str_Capitalize:
        s = s + " " + x

    print(s)


def q2():
    store = dict()
    _exit = "yes"
    while exit != "exit":
        option = input(
            "Enter 1 to input data \n  \t 2 to search\n  \t 3 to exit :")
        if option == '1':
            name = input("name: ")
            num = input("num: ")
            store[num] = name

        if option == '2':
            search = input("mobile no ")
            print(store[num])

        if option == '3':
            _exit = "exit"
            print("turned to dust")


def q3():
    lis_ele = [1, 2, 3, 3, 1, 1, 4, 5, 6]
    set_ele = set(lis_ele)
    print(set_ele)


def q4():
    upper, lower = 0, 0
    example = input("enter a sentence :")
    for x in example:
        if x.islower():
            lower = lower + 1
        elif x.isupper():
            upper = upper + 1
    print('lower= {} upper = {}'.format(lower, upper))


def q5():
    s1 = input("string1 ")
    s2 = input("string2 ")
    set_s1 = set(s1)
    set_s2 = set(s2)
    print(set_s1.intersection(set_s2))


def q6():
    def reversed_def(string):
        string = "".join(reversed(string))
        return string

    def reversed_recur(S, start, stop):
        if start <= stop - 1:
            S[start], S[stop - 1] = S[stop - 1], S[start]
            reversed_recur(S, start + 1, stop - 1)

    s1 = input("string1 ")
    s2 = input("string2 ")
    if s1 == reversed_def(s2):
        print("its a anagram")
    else:
        print("its not an anagram")


def q7():
    a = [1, 2, 3, 4, 5, 6, 7]
    ret = [(x, x ** 2) for x in a]
    print(ret)


def q8():
    # print(os.getcwd())
    store = dict()
    not_word = "is, an, the, for, be, to, in, are, and, has, from, i, am, of, then, if, do, with, at, a, or, as".split(
        ", ")
    print(not_word)
    with open("textinput.txt", 'r+') as file:
        for each_line in file.readlines():
            for each_word in each_line.split(" "):
                if each_word not in not_word:
                    if each_word not in store.keys():
                        store[each_word] = 1
                        print(store)
                    elif each_word in store.keys():
                        store[each_word] = store[each_word]+1
    print(store)


def q9():
    num = False
    symbol = False
    lowerandupper = False  # type: bool

    name = input("username ")
    password = input("password")
    if len(password) < 8:
        print("length check failed")

    else:
        print("length check passed")
        num = True

    if name.isalnum() and password.isalnum():
        print("alpanumeric test passed ")
    else:
        print("alphanumeric test failed")
    for x in password:
        if x.isupper() or x.islower():

            lowerandupper = True
        if not x.isalnum():

            symbol = True
    print(num)
    print(symbol)
    print(lowerandupper)


def q10():
    names = ['adam', 'bob', 'eve', 'alice',
             'robert', 'susan', 'jeremy', 'alex', 'siri']
    x = input("enter  a letter ")
    for name in names:
        if name.startswith(x):
            print(name)


def q11():
    text = input("enter a line: ")
    bad_chars = [';', ':', '!', '*', '\n', '\t', '.', '-', '_']
    for x in bad_chars:
        text = text.replace(x, '')
    print(text)


if __name__ == "__main__":
    q11()
