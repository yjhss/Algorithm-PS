while True:
    password = input()
    if password == "END":
        break
    else:
        result = password[::-1]
        print(result)