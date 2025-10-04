def get_num_words(text):
    x = text.split()
    count = 0
    for i in x:
        count += 1
    return count
def count_occurances(text):
    occurances = {}
    x = text.split()
    y = list(text) 
    for k in y:
        k = k.lower()
        if k not in occurances:
            occurances[k] = 1
        else:
            occurances[k] += 1
    return occurances
def sort_on(items):
    return items["num"]
def sort_dict(text):
    list_dict = []
    for k, v in text.items():
        if k.isalpha():
            list_dict.append({"char": k, "num": v})
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict
        


