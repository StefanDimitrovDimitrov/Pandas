import pandas as pd

first = 'Opiate.txt'
second = 'Undertow.txt'
third = 'Aenima.txt'
fourth = 'Lateralus.txt'
fifth = '10000_days.txt'
sixth = 'Fear_Inoculum.txt'

list_endpoints = [first, second, third, fourth, fifth, sixth]

for endpoint in list_endpoints:

    df = pd.read_csv(endpoint, sep='delimiter', header=None, encoding='cp1252')

    list_words = []
    df.columns = ['Column']

    for row in df['Column']:
        content = row.split()
        for word in content:
            word = word.replace(".", "")
            word = word.replace(",", "")
            word = word.replace("!", "")
            word = word.replace("?", "")
            word = word.replace("(", "")
            word = word.replace(")", "")
            word = word.replace(";", "")
            word = word.replace('"', "")
            word = word.replace('".', "")
            word = word.replace('",', "")
            word = word.replace(":", "")
            list_words.append(word.lower())

    dict = {}

    for word in list_words:
        if word not in dict:
            dict[word] = 0
        dict[word] += 1

    dict = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse=True)}

    # new_df = pd.DataFrame.from_dict(dict, orient='index')
    new_df = pd.DataFrame(dict, index=[0])

    print(f"{endpoint} {new_df.shape}")
    # print(f"{new_df.iloc[:, :16]}")

    # new_df.to_csv(f"{endpoint}_words")

