def order_weight(strng):
    list_of_weights = []
    weights = strng.split()

# Check if the given argument is digit.
# Then create list of dictionaries that contain given weight and sum of digits in the weight.

    if strng and strng[0].isdigit():
        for weight in weights:
            total_sum = sum([int(n) for n in weight])
            list_of_weights.append({"weight": weight, "sum": total_sum})

# Sorting the list by sum of digits in the weight in Ascending order then by alphabetical order.

        list_of_weights.sort(key=lambda e: (e["sum"], e["weight"]))
        result = " ".join([list_of_weights[num]["weight"] for num in range(len(list_of_weights))])
        return result
    else:
        return ''
