def generate_bad_symbol_table() :
    for i in range(p_length-1) :
        bad_symbol[pattern[i]] = p_length - i - 1


def generate_good_suffix_table() :
    i = p_length 
    j = p_length + 1
    bpos = [0] * (p_length + 1)
    bpos[i] = j

    while i > 0 :
        while j <= p_length and pattern[i-1] != pattern[j-1] :
            if good_suffix[p_length-j] == 0 :
                good_suffix[p_length-j] = j - i

            j = bpos[j]
        
        i -= 1
        j -= 1
        bpos[i] = j


    j = bpos[0]
    for i in range(p_length  + 1) :
        if good_suffix[p_length-i] == 0 :
            good_suffix[p_length-i] = j

        if i == j :
            j = bpos[j]

    good_suffix[p_length] = p_length



if __name__ == "__main__" :
    text = "WHICH_FINALLY_HALTS. _ _ AT_THAT POINT"
    pattern = "AT_THAT"

    t_length = len(text)
    p_length = len(pattern)

    bad_symbol = {}
    good_suffix = [0] * (p_length + 1)

    generate_bad_symbol_table()
    generate_good_suffix_table()

    for element in bad_symbol.items() :
        print(element)

    for i in good_suffix :
        print(i)