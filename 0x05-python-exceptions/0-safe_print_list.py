#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    i = 0
    printed = 0

    for i in range(0, x):

       try:
            print("{}".format(my_list[i]), end="")
            printed += 1
       except:
            continue
<<<<<<< HEAD
print()
return printed
=======
    print()
    return printed
>>>>>>> 99a8dc55397dcb9cf6746985b64370eae4dbb0c9
