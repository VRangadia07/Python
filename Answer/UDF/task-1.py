# user will input the string

# 1) word wise reverse

def word_reverse(s):
    
    word = s.split()
    
    reverse_word = word[::-1]
    
    return ' '.join(reverse_word)


input_string = input("Enter a string: ")


reverse_string = word_reverse(input_string)
print("Word wise reverse string:", reverse_string)




# 2) two characters interchange

def chr_interchange(ls):
    i = 1
    j = 11
      
    if i < 0 or j < 0 or i >= len(ls) or j >= len(ls):
        return "Index out of range"
    
    
    change_char = list(ls)
    change_char[i], change_char[j] = change_char[j], change_char[i]
    return  "".join(change_char)

ls = input("Enter a string: ")

result = chr_interchange(ls)

print("String interchange: ", result)

