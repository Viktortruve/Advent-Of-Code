x = 0
y = 0
aim = 0
forward = False
up = False
down = False
with open('input2.txt', 'r') as file:
    # reading each line
    for line in file:

        # reading each word
        for word in line.split():
            if forward:
                x += int(word)
                y += int(word)*aim
                forward = False
            if up:
                aim -= int(word)
                up = False
            if down:
                aim += int(word)
                down = False


            if word == "forward":
                forward = True
            if word == "up":
                up = True
            if word == "down":
                down = True
    print(x*y)
