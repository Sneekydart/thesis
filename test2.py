# --- Define your functions ---
def Dispense(Number, Amount, Rate):
    print(Number, Amount, Rate)

def Stir(Speed):
    print("stir speed", Speed)


# --- Function registry (dispatcher) ---
FUNCTIONS = {
    "Dispense": Dispense,
    "Stir": Stir,
}


# --- Executor ---
def execute_commands(file_path):
    with open(file_path, "r") as file:
        for line_num, line in enumerate(file, start=1):
            parts = line.strip().split()

            if not parts:
                continue  # skip empty lines

            func_name = parts[0]
            args = parts[1:]

            if func_name not in FUNCTIONS:
                print(f"[Line {line_num}] Unknown function: {func_name}")
                continue

            try:
                FUNCTIONS[func_name](*args)
            except TypeError as e:
                print(f"[Line {line_num}] Argument error: {e}")


# --- Run it ---
execute_commands("commands.txt")