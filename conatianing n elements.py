#list conatianing n elements
n = int(input("Enter the number of elements in the list: "))
numbers = [1,2,3,4,5,6,7,]

for i in range(n):
    num = float(input(f"Enter element {i+1}: "))
    numbers.append(num)
average = sum(numbers) / n
print(f"The average of the elements is: {average}")
