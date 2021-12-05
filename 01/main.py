# Solution made by me with improvements taken from u/NoFapWarrior570 on Reddit.

lines = list(map(int, open('input.txt')))

solution_part1 = sum(map(int.__lt__, lines[:-1], lines[1:]))

solution_part2 = sum(map(int.__lt__, sums:=list(map(sum, zip(lines[:-2], lines[1:-1], lines[2:]))), sums[1:]))

print(solution_part1, solution_part2)

