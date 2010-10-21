#
# median.py
#
from sys import argv

nums = argv[1:]
z = len(nums)
medianeven = (z - 1) / 2.0
medianodd = z / 2.0

#for index, value in enumerate(nums):
#    nums[index] = float(value)

if not z%2.0:
        print medianodd
else:
        print medianeven

#if ((len(nums) -1) / 2.0) % 2 == 0:
#    print nums[medianeven]
#else:
#        print nums[medianodd]



