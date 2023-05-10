number = 46275

units = number % 10  # количество единиц 
tens = (46275 // 10) % 10  # количество десятков   
hundreds = (number // 100) % 10  # количество сотен  
thousands = (number // 1000) % 10  # количество тысяч 
tens_thousands = (number // 10000) % 10  # количество десятков тысяч 
tens_power_units = tens ** units  # десятки в степени единиц 16807
result = tens_power_units * 2 /(tens_thousands - thousands)
print (result)
