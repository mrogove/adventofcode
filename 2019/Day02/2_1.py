#file readin
text_file = open("./input.txt", "r")
lines = text_file.read().split(',')

#convert to int
for i in range(len(lines)):
  lines[i] = int(lines[i])

#per spec, initialize locs 1 and 2:
lines[1] = 12
lines[2] = 2

def part_one(lines):
  proc_arr = lines[:]

  #iterate over sets of 4
  for i in range(0, len(proc_arr), 4):
    #operator is the value that dictates what to do.
    operator = proc_arr[i]
    #and we behave accordingly on next two values
    firstVal = proc_arr[proc_arr[i + 1]]
    secndVal = proc_arr[proc_arr[i + 2]]

    #if 99, we fall out
    if operator == 99:
      return proc_arr[0]
      #else we add
    elif operator == 1:
      proc_arr[proc_arr[i + 3]] = firstVal + secndVal
    #else we stop
    elif operator == 2:
      proc_arr[proc_arr[i + 3]] = firstVal * secndVal

  return lines[0]

def part_two(lines):
  proc_arr = lines[:]

  for noun in range(100):
    for verb in range(100):
      proc_arr[1] = noun
      # print(proc_arr[1])
      proc_arr[2] = verb
      # print(proc_arr[2])

      output = part_one(proc_arr)
      # print(output)

      if output == 19690720: #check against this magic number
        return(100 * noun + verb)

if __name__ == "__main__":
  print(part_one(lines))
  print(part_two(lines))