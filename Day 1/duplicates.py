nums = [1, 2, 3, 1]

for idx in range(len(nums)):
    num = nums[idx]
    print('Number :',num)
    print('Checking values:')
    for i in range(idx+1, len(nums)):
        print(nums[i])
        if num == nums[i]:
            print(True)
