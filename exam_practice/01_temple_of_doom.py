from collections import deque

tools = deque([int(x) for x in input().split()])
substances = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]


while tools and substances and challenges:
    tool = tools.popleft()
    substance = substances.pop()
    res = tool * substance
    for ch in challenges:
        if ch == res:
            challenges.remove(ch)
            break
    else:
        tools.append(tool + 1)
        substance -= 1
        if substance > 0:
            substances.append(substance)

if (not tools or not substances) and challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")

elif not challenges:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")


sequences_keys = ["Tools", "Substances", "Challenges"]
sequences_values = [tools, substances, challenges]

seq_dict = {sequences_keys[i]: sequences_values[i] for i in range(len(sequences_keys))}

output = ""
for k, v in seq_dict.items():
    if v:
        output += f"{k}: {', '.join(str(el) for el in v)}\n"

print(output)







