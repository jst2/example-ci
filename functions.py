def add(a, b):
    return a + b

def subtract(a, b):
    return a - b  # <--- fix this in step 7

def multiply(a, b):
    return a * b

def convert_fahrenheit_to_celsius(fahrenheit):
    dgf = multiply(subtract(fahrenheit, 32), 5 / 9) 
    if dgf < -273.15:
        raise ValueError("Input must be larger than -459.67")
    return dgf
