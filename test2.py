# --- Define your functions ---
def dispense(number, amount, rate):
    print("pump", number, amount, rate)

def stir(speed):
    print("stir speed", speed)

def heat(temperature):
    print("temperature", temperature)

def wait(seconds):
    print("wait", seconds)


# --- Function registry (dispatcher) ---
FUNCTIONS = {
    "dispense": dispense,
    "stir": stir,
    "heat": heat,
    "wait": wait
}


# --- Executor ---
def execute_commands(file_path):
    with open(file_path, "r") as file:
        print("File name:", file_path)
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
execute_commands("50nm Spherical AuNP")