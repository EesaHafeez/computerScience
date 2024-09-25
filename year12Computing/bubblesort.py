#compare n valye to value n untill range end
#if it is greater, shift up
# store in a temp variable

numbers=[10,9,8,7,6]
for i in range(len(numbers)):
        for i in range(len(numbers)-1):
            if numbers[i] > numbers[i+1]:
                temp = numbers[i]
                numbers[i] = numbers[i+1]
                numbers[i+1] = temp
print(numbers)
