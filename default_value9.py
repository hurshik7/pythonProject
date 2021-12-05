def append_to(element, to=None):
    if to == None:
        to = []
    to.append(element)
    return to


def main():
    my_list = append_to(12)
    print(my_list)

    my_other_list = append_to(42)
    print(my_other_list)


if __name__ == "__main__":
    main()

