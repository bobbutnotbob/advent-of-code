def main():
    with open("2021/Day_1/input.txt") as depths_file:
        depths_list = depths_file.readlines()
        depths_list = [int(line.rstrip()) for line in depths_list]

    count = 0
    for i in range(len(depths_list)):
        if i == 0:
            print("(N/A - no previous measurement)")
            continue

        if depths_list[i] > depths_list[i - 1]:
            print("(increased)")
            count += 1
        elif depths_list[i] < depths_list[i - 1]:
            print("(decreased)")
        else:
            print("(equal)")
    print(count)

if __name__ == "__main__":
    main()

