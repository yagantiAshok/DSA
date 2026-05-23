




def remove_character(string, ch):

    if ( len(string)==0 or string==""):

        return string
    
    small_answer = remove_character(string[1:],ch)

    if (string[0]==ch):

        return small_answer
    
    else:

        return string[0] + small_answer
    


string = " .. "
print(remove_character(string,"z"))