text = "I like apples"

def my_func():
    global text
    # We'll try joining another string to 'text'
    text = text + "... but I love oranges better!"
    print("text from the inside: " + text)

my_func()
print("text from the outside: " + text)