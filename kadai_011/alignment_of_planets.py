# %%
planets = [
    "水",
    "金",
    "地",
    "火",
    "木",
    "土",
    "天",
    "海",
    "冥"
    ]

print("for文")
[print(planet) for planet in planets]

print("while文")
i = 0
while len(planets) > i:
    print(planets[i])
    i += 1
print(planets)

print("while文（pop）")
while planets:
    planet = planets.pop(0)
    print(planet)
print(planets)

# %%
