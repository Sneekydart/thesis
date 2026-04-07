def Dispense(Number, Amount, Rate):
    print(Number, Amount, Rate)

# Open the file in read mode
with open("example.txt", "r") as file:
    # Loop through each line in the file
    for line in file:
        # Print the line (strip removes extra newline characters)
        print(line.strip())
    
Dispense(10, 15, 20)