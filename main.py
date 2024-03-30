while True:
    age = input("How old are you? ")
    try:
        age = int(age)
        if age >= 18:
            print("Accept allowed")
            break
        else:
            print("Accept denied")
            break
    except ValueError:
        print(f"{age} is not number, please write number!")
    finally:
        print("-"*14)