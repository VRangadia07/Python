s="this is string example"

# 1)reverse the string
r = s[::-1]
print(r)

# 2) word wise reverse
word_reverse = ' '.join(s.split()[::-1])
print(word_reverse)

# 3) 2 characters interchange
# ls = "this is string example"
change_char = list(s)
i = 3
j = 9
change_char[i], change_char[j] = change_char[j], change_char[i]
ls = "".join(change_char)
print(ls)

# 4) space split join the string with *
split_space = s.split()
join_string = "*".join(split_space)
print(split_space)
print(join_string)

# 5) replace is -> was substring->this this is  was

s = s.replace("this", "THIS").replace("is", "was")

s = s.replace("THIS", "this")

print(s)



