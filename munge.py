# place your code to clean up the data file below.

input_file = "data/bezdekIris.data"
output_file = "data/clean_data.csv"

# Add a header row
header = "sepal_length,sepal_width,petal_length,petal_width,class\n"

with open(input_file, 'r') as file:
    data = file.read()

data_w_header = header + data

with open(output_file, 'w') as file:
    file.write(data_w_header)

# Add an index column
with open(output_file, 'r') as file:
    lines = file.readlines()

lines[0] = "index," + lines[0]

for i, line in enumerate(lines[1:-1], start=1):  
    lines[i] = f"{i}, " + line

with open(output_file, 'w') as file:
    file.writelines(lines)
