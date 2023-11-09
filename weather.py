import my_utils

if __name__ == '__main__':
    loop = 0
    temperatures = []
    while True:
        temp = input(f"enter temp {loop} followed by f or c (e.g. 10c) {loop + 1} : ")
        if temp == '':
            break
        unit = temp[-1]
        temp = temp[:-1]
        temp = int(temp)
        if unit == 'f':
            temp = my_utils.fahrenheit_to_celcius(temp)
        temperatures.append(temp)
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    sum_temp = sum(temperatures)
    length_temps = len(temperatures)
    average_temp = sum_temp / length_temps

    print(f"Highest temp : {max_temp}C")
    print(f"Lowest temp : {min_temp}C")
    print(f"Average temp : {average_temp}C")