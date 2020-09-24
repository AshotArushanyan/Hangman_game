import json
books = [
{
    "author": "Dan Brown",
    "name": "The Da Vinci Code",
    "published": 2003
},
{
    "author": "Dan Brown",
    "name": "The Lost Symbol",
    "published": 2009
},
{
    "author": "Dan Brown",
    "name": "Angels & Demons",
    "published": 2000
}
]


def bubble_sorting(list):
    for i in range(len(list)):
        for j in range(len(list)-1):
            if list[j]["published"] > list[j+1]["published"]:
                list[j],list[j+1] = list[j+1],list[j]
    return list


bubble_sorting(books)
print(json.dumps(books, indent=1))