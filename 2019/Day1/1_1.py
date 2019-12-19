

def fuel(mass):
  return mass // 3 - 2

def total_fuel(mass):
  total_mass = 0
  # simple while loop - continue while mass not gone.
  while True:
    mass = fuel(mass)
    if mass <= 0:
      break
    total_mass += mass

  return total_mass

def part_one():
  with open(r"../Day1/input.txt") as file:
    return sum(fuel(int(i)) for i in file.readlines())

def part_two():
  with open(r"../Day1/input.txt") as file:
    return sum(total_fuel(int(i)) for i in file)


if __name__ == "__main__":
  print(part_one())
  print(part_two())