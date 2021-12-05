instructions = [ (dir, int(val)) for dir, val in map(str.split, open('input.txt')) ]

horizontal = sum(val for dir, val in instructions if dir == 'forward') 
depth      = sum((1 - 2*(dir == 'up')) * val for dir, val in instructions if dir != 'forward')

solution_part1 = horizontal * depth

horizontal = depth = aim = 0

for dir, val in instructions:
    horizontal += (hor_val:=(dir == 'forward') * val)
    aim += (dir != 'forward') * (1 - 2*(dir == 'up')) * val
    depth += aim * hor_val

solution_part2 = horizontal * depth

print(solution_part1, solution_part2)