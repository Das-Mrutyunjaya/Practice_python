planet1 = "Closest to the sun"

print(planet1)
print(planet1[0])
print(planet1[1])
print(planet1[2])
print(planet1[-2])
print(planet1[-1])
print(planet1[5])

# slicing a string

print("Substring: " + planet1[1:5])
print("Substring: " + planet1[:])
print("Substring: " + planet1[:7])
print("Substring: " + planet1[:8])
print("Substring: " + planet1[7:])
print("Substring: " + planet1[-6:])

# Slicing Tupple

devops = ("git", "bash scripting", "jenkins", "Docker")

print(devops[1:4])
print(devops[1:][-2:])
print(devops[1:][-2:][0])
print(devops[1:][-2:][0][-2:])

# Dictionary Examples

skills = {"devops": ["git", "bash scripting", "jenkins", "Docker"], "Development": ("java", "NodejS", "Python")}
print(skills)
print(skills["devops"])
print(skills["devops"][0])
