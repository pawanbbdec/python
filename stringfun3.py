from data import story

print(f'total chars in the story:{len(story)}')
words = story.split()
print(f'total words in the story:{len(words)}')
print(words)
print(f'total unique words in the story:{len(set(words))}')

print(words)

sentences = story.split('.')
print(sentences)
lines = story.split('\n')
print(f'total lines in the story:{len(lines)}')
print(lines)

poem_list=[
    'twinkle,twinkle,little star,',
    'how in wonder what you are!',
    'up above the world so high,',
    'like a diamond in the sky.',
]
poem='\n'.join(poem_list)
print(poem)