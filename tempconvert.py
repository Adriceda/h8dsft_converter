##VER 1##
# def tempconvert(temperature, unit='Celcius'):
#     if unit == "Celcius":
#         KELVIN = temperature + 273.15
#         unit = "KELVIN"
#         return [KELVIN, unit]
#     elif unit == "KELVIN":
#         Celcius = temperature - 273.15
#         unit = "Celcius"
#         return [Celcius, unit]


# def toFahrenheit(temperature, unit = "Celcius"):
#     if unit == "Celcius":
#         fahrenheit = [temperature * (9/5)] + 32
#     elif unit == "KELVIN":
#         fahrenheit = [(tempconvert(temperature, unit='KELVIN')) * (9/5)] + 32
#     unit = "Fahrenheit"
#     return [fahrenheit, unit]


# def fromFahrenheit(fahrenheit):
#     celcius = (fahrenheit - 32) * (5/9)
#     kelvin = celcius + 273.15
#     return [fahrenheit, celcius, kelvin]

##############################################################################################################

##VER 2##
# FROM Celcius to KELVIN
def cel2K(temperature):                                         #Celcius to KELVIN Function
    Kelvin = temperature + 273.15                               #Calculation Formula
    return Kelvin                                               #return KELVIN value

# FROM KELVIN to Celcius
def k2Cel(temperature):                                         #KELVIN to Celcius Function
    Celcius = temperature - 273.15                              #Calculation Formula
    return Celcius                                              #return Celcius value


#Convert Celcius/KELVIN to Fahrenheit
def toFahrenheit(temperature):
    i = 0                                                       #WHILE LOOP condition
    while (i != 1):                                             #While function for user input
        unit = input("please input unit (Celcius/KELVIN): ")    #User input to determine    
        if unit == "Celcius":                                   #IF loop to check if input condition met
            i += 1                                              #breaking WHILE loop
        elif unit == "KELVIN":                                  #IF loop to check if input condition met
            i += 1                                              #breaking WHILE loop
    
    print("--> ", temperature, " ", unit)                       #PRINT input value and unit
    if unit == "Celcius":                                       #IF function to check whether to convert from Celcius
        fahrenheit = (temperature * 9/5) + 32                   #Calculation Formula
    elif unit == "KELVIN":                                      ##IF function to check whether to convert from KELVIN
        fahrenheit = (k2Cel(temperature) * 9/5) + 32            #Calculation Formula while using the established KELVIN to Celcius function k2Cel
    unit = "Fahrenheit"                                         #Ovverride variable unit into "Fahrenheit"
    print("--> ", fahrenheit, " Fahrenheit")                    #PRINT output value and unit
    return fahrenheit                                           #return fahrenheit value



#Convert temperature values into Fahrenheit using Celcius and KELVIN calculations
def fromFahrenheit(fahrenheit):
    celcius = (fahrenheit - 32) * 5/9                                                       #Calculation Formula
    kelvin = cel2K(celcius)                                                                 #Calculation Formula while using the established Celcius to KELVIN function cel2K
    output = {"Fahrenheit" : fahrenheit, "Celcius" : celcius, "Kelvin" : kelvin}            #OUTPUT contains all temperature values
    return output                                                                           #return output dictionary
