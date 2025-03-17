text = """
Everyone counts.
Everyone has access to great learning.
Every person's unique talents are valued equally.
Everyone takes responsibility for themselves and their community."""

skip = ['E', "'", ' ', '\n', '.']

letter_count = {}

for letter in text:
        if letter in skip:
             pass
        elif letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

print(letter_count)

# Make a dictionary where the keys are characters and the values are the number of times that character appears in the `text` print the dicitonary