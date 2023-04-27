def generate_bad_symbol_table() :
    for i in range(p_length-1) :
        bad_symbol[pattern[i]] = p_length - i - 1


if __name__ == "__main__" :
    text = "WHICH_FINALLY_HALTS. _ _ AT_THAT POINT"
    pattern = "AT_THAT"

    t_length = len(text)
    p_length = len(pattern)

    bad_symbol = {}
    generate_bad_symbol_table()

    for element in bad_symbol.items() :
        print(element)