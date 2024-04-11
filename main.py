# Andersen Wall

def encode(start):
    startlist = []
    endlist = []
    end = ""
    for i in range(len(start)):
        startlist.append(start[i])
    for i in range(len(startlist)):
        j = (int(startlist[i])+3) % 10
        endlist.append(str(j))
    for i in range(len(endlist)):
        end = end + endlist[i]
    return end


def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Exit")
        print()
        s = input("Please enter an option: ")

        if s == 1:
            start = input("Please enter your password to encode: ")
            end = encode(start)
            print("Your password has been encoded and stored!")

        elif s == 2:
            start = decode(end)
            print(f"The encoded password is {int(end)}, and the original password is {int(start)}.")
        elif s == 3:
            break


if __name__ == '__main__':
    main()
