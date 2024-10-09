#compare n valye to value n untill range end
#if it is greater, shift up
# store in a temp variable



#list of unsorted numbers 
numbers=[5,4,3,2,1]
#initialising swap=1 to enter while loop
swap = 1
# while a swap has been made in the for loop
while swap !=0:
        # swap = 0 so if no swaps made exits while loop
        swap = 0
        # iterating throigh each value in the list
        for i in range(len(numbers)-1):
            #if number bafore is greater than number after
            if numbers[i] > numbers[i+1]:
                # store bigger number in a temp variable
                temp = numbers[i]
                #smaller number moves down a p place in the list
                numbers[i] = numbers[i+1]
                numbers[i+1] = temp
                #if no swaps are made list is sorted so will exit the while loop
                swap = swap +1
            
print(numbers)

