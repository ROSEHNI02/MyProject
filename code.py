def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    print(f"Executing: Converting {celsius}°C to Fahrenheit...")
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    print(f"Executing: Converting {fahrenheit}°F to Celsius...")
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    """Converts Celsius to Kelvin."""
    print(f"Executing: Converting {celsius}°C to Kelvin...")
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    """Converts Kelvin to Celsius."""
    print(f"Executing: Converting {kelvin}K to Celsius...")
    return kelvin - 273.15

print("\n🌡️ Temperature Converter 🌡️")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")
print("5. Exit")

while True:
    choice = input("\nEnter your choice: ")

    if choice == "1":
        temp = float(input("Enter temperature in Celsius: "))
        result = celsius_to_fahrenheit(temp)
        print(f"✅ Result: {temp}°C = {result:.2f}°F")
    elif choice == "2":
        temp = float(input("Enter temperature in Fahrenheit: "))
        result = fahrenheit_to_celsius(temp)
        print(f"✅ Result: {temp}°F = {result:.2f}°C")
    elif choice == "3":
        temp = float(input("Enter temperature in Celsius: "))
        result = celsius_to_kelvin(temp)
        print(f"✅ Result: {temp}°C = {result:.2f}K")
    elif choice == "4":
        temp = float(input("Enter temperature in Kelvin: "))
        result = kelvin_to_celsius(temp)
        print(f"✅ Result: {temp}K = {result:.2f}°C")
    elif choice == "5":
        print("👋 Exiting Temperature Converter. Goodbye!")
        break
    else:
        print("❌ Invalid choice! Please try again.")

#ShenalK02 Modified the code



