import os

# get current working directory path
cwd_path = os.getcwd()

import json
def read_data(file_name, field):
    with open (file_name, "r") as f:
        data=json.load(f)

    if field not in data:
        return None
    return data [field]

    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)


def linear_search(sequence, number):
    positions=[]
    count=0

    for index, item in enumerate (sequence):
        if item ==number:
            positions.append(index)
            count +=1

    return {"positions": positions, "count": count}


def main():
    sequential_data= read_data("sequential.json", "unordered_numbers")
    print (sequential_data)

    searched_num= 7
    result= linear_search(sequential_data, searched_num)
    print (f "pozicie"(idexy): {result ["positions"]})
    print (f "pocet vyskytov": {result["count"]})


if __name__ == '__main__':
    main()