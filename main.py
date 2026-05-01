def greet(name):
    return f"Hello, {name}!"

# we use a return to return a value from the function, instead of printing it directly. This allows us to use the returned value in other parts of our code, or to store it in a variable for later use.

def get_greeting(name):
    return f"Hello, {name}!"

message = get_greeting("Eugene")
print(message)  # Output: Hello, Eugene!
# In this example, the get_greeting function returns a greeting message, which we then store in the variable message and print it. This approach is more flexible than printing the message directly within the function, as it allows us to use the returned value in different contexts.

file = open("file.txt", "w")
file.write(message)
file.close()
