my_string = 'Names: Romeo, Juliet'

# split the string at ':'
step_0 = my_string.split(':')

# get the first slice of the list
step_1 = step_0[1]

# split the string at ','
step_2 = step_1.split(',')

# strip leading and trailing edge spaces of each item of the list 
step_3 = [name.strip() for name in step_2]

# do all the above operations in one go
one_go = [name.strip() for name in my_string.split(':')[1].split(',')]

for idx, item in enumerate([step_0, step_1, step_2, step_3]):
    print("Step {}: {}".format(idx, item))

print("Final result in one go: {}".format(one_go))