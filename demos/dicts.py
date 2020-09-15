nested_list = [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[["I'm nested"]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

levels = 0


def traverse(the_list):
    global levels
    if type(the_list[0]) == list:
        levels += 1
        traverse(the_list[0])

    else:
        print(the_list[0], levels, "times")


traverse(nested_list)
