import textwrap
text="I Love Python Programming"
wrapped_text = textwrap.wrap(text,width=10)

print(wrapped_text)

for line in wrapped_text:
    print(line)
