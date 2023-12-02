def calculate_calibration_sum(filename="input.txt"):
  total_calibration = 0
  with open(filename) as f:
    for line in f:
      line = line.strip()
      print(line)
      first_digit = None
      last_digit = None
      for char in line:
        if char.isdigit():
          last_digit = char
          if first_digit is None:
            first_digit = char
      if first_digit and last_digit:
        calibration_value = int(f"{first_digit}{last_digit}")
        print(calibration_value)
        total_calibration += calibration_value
  return total_calibration

total_sum = calculate_calibration_sum()
print(total_sum)