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
    for i in range(len(list)-1):
        for j in range(len(list)-1-i):
            if list[j]["published"] > list[j+1]["published"]:
                temporary = list[j]
                list[j] = list[j+1]
                list[j+1] = temporary
    return list


bubble_sorting(books)
print(json.dumps(books, indent=1))
