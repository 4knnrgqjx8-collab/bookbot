def file_opener(file_path):
    with open(file_path) as f:
        return f.read()
def number_words(path):
    text = file_opener(path)
    words = text.split()
    return len(words)
def characters(path1):
    charac = {}
    text_low = file_opener(path1).lower()
    for i in range(0, len(text_low)):
        if text_low[i] in charac:
            charac[text_low[i]] += 1
        else:
            charac[text_low[i]] = 1
    return charac
def prep(dic):
    list_dic = []
    for i in dic:
        list_dic.append({"character" : i, "count" : dic[i]}
                        )
    return list_dic
def sort_on(what):
    return what["count"]
def sortifying(dic1):
    what_sort = prep(dic1)
    what_sort.sort(reverse = True, key = sort_on)
    return what_sort

