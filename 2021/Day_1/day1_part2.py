def main():
    with open("2021/Day_1/input.txt") as depths_file:
        depths_list = depths_file.readlines()
        depths_list = [int(line.rstrip()) for line in depths_list]

    count = 0
    for i in range(len(depths_list)):
        if i <= 1:
            continue
        
        depth_sum = depths_list[i] + depths_list[i - 1] + depths_list[i - 2]
        print(depth_sum)
        if i == 2:
            print("(N/A - no previous sum)") 
            previous_sum = depth_sum
            continue

        if depth_sum > previous_sum:
            print("(increased)")
            count += 1
        elif depth_sum < previous_sum:
            print("(decreased)")
        else:
            print("(no change)")
        previous_sum = depth_sum
    print(count)

if __name__ == "__main__":
    main()