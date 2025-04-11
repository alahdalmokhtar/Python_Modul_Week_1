def calculate_weight_index():
    # Ask user for weight (in kg) and height (in meters)
    weight = float(input("Enter your weight in kilograms (kg): "))
    height = float(input("Enter your height in meters (m): "))
    
    # Calculate weight index: 
    weight_index = weight / (height ** 2)
    
    # Determine the category based on BMI
    if weight_index < 25:
        category = "underweight"
    elif 25 <= weight_index < 30:
        category = "normal"
    elif 30 <= weight_index < 40:
        category = "overweight"
    else:  # weight_index >= 40       
        category = "obese"  
    # Display the result
    print(f"\nYour weight_index is: {weight_index:.2f}")
    print(f"According to the weight_index, you are: {category}")

# Run the function
calculate_weight_index()