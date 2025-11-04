while True:
    user_name = input("Enter your name: ")
    
    if len(user_name) >= 3 and not user_name.isdigit():
        print("thank you")
        break
    else:
        print("give the correct name")
