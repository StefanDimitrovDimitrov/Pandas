import pandas as pd

first_album = 'ToolLyrics_Opiate.txt'
last_album = 'ToolLyrics_Fear_Inoculum.txt'

df = pd.read_csv('ToolLyrics_Fear_Inoculum.txt', sep=";", header=None, encoding='cp1252')

list_words = []
df.columns = ['Column']

for row in df['Column']:
    content = row.split()
    for word in content:
        word = word.replace(".", "")
        word = word.replace(",", "")
        word = word.replace("!", "")
        word = word.replace("?", "")
        list_words.append(word)

dict = {}

for word in list_words:
    if word not in dict:
        dict[word] = 0
    dict[word] += 1

dict = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse=True)}

new_df = pd.DataFrame.from_dict(dict, orient='index')
print(new_df.shape)
new_df.to_csv('20_most_frequently_words_in_album_Fear_Inoculum')

# for k, v in dict.items():
#     print(f"{k} - {v}")
