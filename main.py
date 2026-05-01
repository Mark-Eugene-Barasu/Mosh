# infinite loop

while True:
    command = input(">")
    print("Echo:", command)
    if command.lower() == "exit":
        print("Exiting the program.")
        break