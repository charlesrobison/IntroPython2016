"""Nov 26, 2016 args and kwargs lab."""


def color(fore_color='green', back_color='orange', link_color='white', visited_color='red'):
    print("{}, {}, {}, {}". format(fore_color, back_color, link_color, visited_color))

regular = ('red', 'blue')
links = {'link_color': 'chartreuse'}


def color_tuple_dict(*regular, **links):
    print("the regular colors are:", regular)
    print("the link colors are:", links)


def color_args_kwargs_t(*args, **kwargs):
    colors = []
    # print('Colors in args are:', args)
    colors.append('Colors in args are:' + str(args))
    if not kwargs:
        # print('Colors in kwargs are:', kwargs)
        return ("No colors in kwargs!")
    else:
        for key, value in kwargs.items():
            if (key == 'fore_color' or key == 'back_color' or key == 'link_color' or key == 'visited_color'):
                colors.append('Colors in kwargs are:' + str(key) + str(value))
                # print(key, value, '\n')
            else:
                # print(key, ':key not accepted')
                colors.append('Key not accepted:' + str(key))
            continue
    return "\n".join(colors)


    # test input1: color_args_kwargs('yellow', fore_color = 'green', back_color= 'orange', link_color='white', visited_color = 'red')
    # test input2: color_args_kwargs(fore_color = 'green', back_color= 'orange', link_color='white', visited_color = 'red')
    # test input3: color_args_kwargs().
    # test input4: color_args_kwargs('yellow', link_color='white', visited_color = 'red')
    # test input5: color_args_kwargs('yellow', other_color='silver', visited_color = 'red')
    # test input6: color_args_kwargs('yellow', fore_color = 'green', back_color= 'orange', link_color='white', visited_color = 'red', other_color = 'silver')
    # test input7: color_args_kwargs('yellow', fore_color = 'green', fore_color = 'orange')
