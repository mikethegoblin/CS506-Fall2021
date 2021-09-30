def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    dataset = []
    with open(csv_file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            # split the line into list of strings
            str_data = line.strip('\n').split(',')
            data = []
            for val in str_data:
                if not_numeric(val):
                    data.append(val.strip('\"'))
                    continue
                val = float(val) if val != '' else float('NaN')
                data.append(val)
            dataset.append(data)
    return dataset

def not_numeric(s):
    '''
    returns True if any of the character in the string is not a number
    the period(.) character counts as a number in this case
    '''
    for char in s:
        if char.isalpha() and char != '.':
            return True

    return False
