word = input("Word: ")

frame_width = 30

total_spaces = frame_width - len(word) - 2
spaces_left = total_spaces // 2
spaces_right = total_spaces - spaces_left

print('*' * frame_width)

print('*' + ' ' * spaces_left + word + ' ' * spaces_right + '*')

print('*' * frame_width)
