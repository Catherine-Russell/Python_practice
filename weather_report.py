def as_sun_lover(temperature):
    if temperature > 25:
        return "great"
    else:
        return "not great"
    
def as_snow_lover(temperature):
    if temperature < 1:
        return "great"
    else:
        return "not great"
    
def report_weather(temp, pov):
    opinion = pov(temp)
    return f"The temperature today is {temp} which is {opinion} in my opinion."

rep_weather = report_weather

print(rep_weather(30, as_snow_lover))
print(rep_weather(30, as_sun_lover))
print(rep_weather(-3, as_snow_lover))
print(rep_weather(-3, as_sun_lover))

