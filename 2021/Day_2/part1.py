def main():
    with open("2021/Day_2/input.txt") as moves_file:
        moves_list = moves_file.readlines()
        moves_list = [line.rstrip() for line in moves_list]

    hori_pos = 0
    vert_pos = 0
    for line in moves_list:
        direction, distance = line.split()
        distance = int(distance)

        if direction == "forward":
            hori_pos += distance
        elif direction == "up":
            vert_pos -= distance
        elif direction == "down":
            vert_pos += distance
        else:
            print("Invalid Direction")

    print(hori_pos * vert_pos)
    
if __name__ == "__main__":
    main()