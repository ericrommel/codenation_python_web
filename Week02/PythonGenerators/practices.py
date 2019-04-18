# Build and return a list
def firstn(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums

def firstn_with_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

sum_of_first_n = sum(firstn_with_generator(1000000))

print(sum_of_first_n)

print('# list comprehension')
doubles = [2 * n for n in range(50)]
print(doubles)

print('# same as the list comprehension above')
doubles = list(2 * n for n in range(50))
print(doubles)


def double_(L):
    return [x*2 for x in L]

eggs = double_([1, 2, 3, 4, 5])
print(eggs)

def double(L):
    for x in L:
        yield x*2

print('# eggs will be a generator')
eggs = double([1, 2, 3, 4, 5])
print(eggs)

print('# the above is equivalent to ("generator comprehension"?)')
eggs = (x*2 for x in [1, 2, 3, 4, 5])
print(eggs)

print('# need to do this if you need a list')
eggs = list(double([1, 2, 3, 4, 5]))
print(eggs)

print('# the above is equivalent to (list comprehension)')
eggs = [x*2 for x in [1, 2, 3, 4, 5]]
print(eggs)
