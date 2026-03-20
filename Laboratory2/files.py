def read_and_sum_numbers(filename):
    f = open(filename, "r")
    data = f.read().split()
    sum = 0
    for i in data:
        sum += int(i)
    f.close()
    return sum

def write_numbers(filename):
    f = open(filename, 'w')
    f.write(input())
    f.close()

if __name__ == "__main__":
    file = "temp-" + input("File name : ") + ".txt"
    print(file)
    write_numbers(file)
    result = read_and_sum_numbers(file)
    print(result)