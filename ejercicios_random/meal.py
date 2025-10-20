def calculate_tips(meal_price, custom_tip):
    
    meal_price = float(meal_price.replace("$", ""))
    tip1 = meal_price * 15/100
    tip2 = meal_price * 20/100
    custom_tip = meal_price * float(custom_tip.replace("%", "")) / 100
   
    return f"El valor total es: ${tip1:.2f}, ${tip2:.2f} o ${custom_tip:.2f}"

print(calculate_tips("$20.00","40%"))