


# def remove_character(string, ch):

#     if ( len(string)==0 or string==""):

#         return string
    
#     small_answer = remove_character(string[1:],ch)

#     if (string[0]==ch):

#         return small_answer
    
#     else:

#         return string[0] + small_answer
    


# string = " .. "
# print(remove_character(string,"z"))


# string = "malayalam"

# palindrom = ""

# for i in range(len(string)):

#     last_char = string[len(string)-1-i]

#     palindrom+=last_char

# if palindrom==string:

#     print("These string is palindrome")

# else:

#     print("Not")



# def palindrome_string(string):

#     if (len(string)==0 or len(string)==""):

#         return string
    
#     palindrome = palindrome_string(string[1:])

#     return palindrome+string[0]


# print(palindrome_string(string="malayalam"))



# def palindrome(s1,start,end):

#     if start>=end:

#         return True
    
#     if s1[start]!=s1[end]:

#         return False
    
#     return palindrome(s1,start+1,end-1)


# string = "malayalam"

# print(palindrome(string,0,len(string)-1))



def subsequence(string):

    if (len(string)==0 or string== "" ):

        return [""]
    
    small_ans = subsequence(string[1:])

    my_char = string[0]

    ans = []


    for each_seq in small_ans:

        ans.append(my_char + each_seq)

    
    ans.extend(small_ans)

    return ans



s = "abc"

print(subsequence(s))


