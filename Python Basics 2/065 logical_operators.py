# Logical operators <, >, ==

# print('a' > 'A')
# print(1 != 0)

is_magician = True
is_expert = False

# check if magician AND expert: "you are a master magician"
if is_magician and is_expert:
    print("you are a master is_magician")

# check if magician but not expert: "at least you are getting there"
elif is_magician and not is_expert:
    print("at least you are getting there")

# if you are not a magician: " you need magic power"
elif not is_magician:
    print("you need magic power")
