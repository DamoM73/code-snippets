light_on = True

while True:
    # Display current state
    if light_on:
        print("The light is ON")
    else:
        print("The light is OFF")
    
    # Get user input
    command = ""
    while command != "on" and command != "off":
        command = input("Turn light on or off? ").strip().lower()
    
    # Update state based on input
    if command == "on":
        light_on = True
    else:
        light_on = False
    