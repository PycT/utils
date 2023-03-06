chars = {
    "0": [
        "  000000000000  ",
        " 00000000000000 ",
        " 0000      0000 ",
        " 0000      0000 ",
        " 0000      0000 ",
        " 0000      0000 ",
        " 00000000000000 ",
        "  000000000000  "
    ],
    "1": [
        "     111111     ",
        "    1111111     ",
        "   11111111     ",
        "  111111111     ",
        "     111111     ",
        "     111111     ",
        " 11111111111111 ",
        " 11111111111111 "
    ],
    "2": [
        "   22222222222  ",
        "  2222     2222 ",
        "           2222 ",
        "   222222222222 ",
        "  222222222222  ",
        "  22222         ",
        "  22222         ",
        "  2222222222222 "
    ],
    "3": [
        "  333333333333  ",
        " 333      33333 ",
        "          33333 ",
        "     333333333  ",
        "          33333 ",
        "            333 ",
        " 333       3333 ",
        "  333333333333  "
    ],
    "4": [
        " 4444      4444 ",
        " 4444      4444 ",
        " 4444      4444 ",
        " 44444444444444 ",
        " 44444444444444 ",
        "           4444 ",
        "           4444 ",
        "           4444 "
    ],
    "5": [
        " 55555555555555 ",
        " 55555          ",
        " 55555          ",
        " 5555555555555  ",
        "         555555 ",
        "          55555 ",
        "         555555 ",
        " 5555555555555  "
    ],
    "6": [
        "   66666666666  ",
        "  6666     6666 ",
        " 66666          ",
        " 6666666666666  ",
        " 66666     6666 ",
        " 66666     6666 ",
        " 66666     6666 ",
        "  666666666666  "
    ],
    "7": [
        " 77777777777777 ",
        " 7777777777777  ",
        "        77777   ",
        "       77777    ",
        "      77777     ",
        "     77777      ",
        "    77777       ",
        "   77777        "
    ],
    "8": [
        "  888888888888  ",
        " 8888      8888 ",
        " 8888      8888 ",
        "  888888888888  ",
        "  888888888888  ",
        " 8888      8888 ",
        " 8888      8888 ",
        "  888888888888  "
    ],
    "9": [
        "  999999999999  ",
        " 9999      9999 ",
        " 9999      9999 ",
        " 9999      9999 ",
        "  9999999999999 ",
        "          99999 ",
        " 9999     99999 ",
        "  999999999999  "
    ]
}

def print_grandes(the_string):
    print(" --{}-- ".format("-" * len(the_string) * 16))
    print("|  {}  |".format(" " * len(the_string) * 16))
    for i in range(0, 8):
        output = ""
        for k in range(0, len(the_string)):
            if the_string[k] in chars:
                output += chars[the_string[k]][i]
        print("|  {}  |".format(output))
    print("|  {}  |".format(" " * len(the_string) * 16))
    print(" --{}-- ".format("-" * len(the_string) * 16))
 