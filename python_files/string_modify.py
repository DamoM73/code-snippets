sample = "A long time ago in a galaxy far far away"
sample_list = ["Use", "the", "Force"]
sample_whitespace = "    Jawa    "
sample_lines = "Help me Obi Wan Kenobi\nYou are my only hope"

print(" ".join(sample_list))
print(sample_whitespace.lstrip())
print(sample.replace("Force", "fork"))
print(sample.rsplit(" ",3))
print(sample_whitespace.rstrip())
print(sample.split(" ",3))
print(sample.rsplit(" "))
print(sample_lines)
print(sample_lines.splitlines())
print(sample_whitespace.strip())