# scale = list(map(int, input().split()))

# ascending = sorted(scale)

# descending = sorted(scale, reverse=True)

# if scale == ascending:
#     print("ascending")

# elif scale == descending:
#     print("descending")

# else:
#     print("mixed")

scale = list(map(int, input().split()))

ascending = True
descending = True

for i in range(1, 8):
    if scale[i] > scale[i-1] :
        descending =False
    elif scale[i] < scale[i-1]:
        ascending = False

if ascending:
    print("ascending")

elif descending:
    print("descending")

else:
    print("mixed")
