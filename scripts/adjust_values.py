import re

labels = [("AO",32),("AI",16),("DO",32),("DI",32)]

with open("../HIL Breakout Board 3.3.kicad_sch", "r") as file:
    content = file.read()

for prefix, count in labels:
    # Go backwards to avoid overwrite collisions (important!)
    for i in range(count, 0, -1):
        old_label = f"{prefix}{i-1}"
        new_label = f"{prefix}{i}"

        pattern = rf'(\(global_label\s+"){old_label}(")'
        replace = rf'\1{new_label}\2'

        content = re.sub(pattern, replace, content)
        print(f"Replaced {old_label} with {new_label}")

with open("../HIL Breakout Board 3.3.kicad_sch", "w") as file:
    file.write(content)

print("Done.")