def average(data):
    numbers = [int(num) for num in data.split(';')]
    return sum(numbers) / len(numbers)

