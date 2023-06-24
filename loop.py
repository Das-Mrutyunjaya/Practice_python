PLANET = "earth"

for i in PLANET:
    print(i)

vaccines = ("moderna", "flue", "covaxin", "covishield")
for i in vaccines:
    print(i[:-2])

# While loop
x = 0
while x < 10:
    print(x)
    x += 1

import time

while True:
    print(time.localtime())
    time.sleep(2)
