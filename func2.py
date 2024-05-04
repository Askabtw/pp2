# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]


#1
def imdb55TRUE(movies, movie):
    for i in movies:
        if i["name"] == movie:
            if i["imdb"]  >= 5.5:
               print(True)

movie = "Hitman"
imdb55TRUE(movies, movie)



#2
def imdb55SUBLIST(movies):
    for i in movies:
            if i["imdb"] >= 5.5:
               print(i)

imdb55SUBLIST(movies)


#3
def category(movies, categ):
    for i in movies:
            if i["category"] == categ:
               print(i["name"])

categ = "Romance"
category(movies, categ)


#4
def av_score(movies, list_of_movie):
    all = float(0)
    for i in movies:
        if i["name"] in list_of_movie:
           all += float(i["imdb"])
    return all/ len(list_of_movie)

list_of_movie = ["Hitman", "We Two", "Exam"]
a = av_score(movies, list_of_movie)
print(round(a, 3))


#5
def av_score(movies, cat):
    all = float(0)
    cnt =0
    for i in movies:
        if i["category"] in cat:
           cnt +=1
           all += float(i["imdb"])
    return all/ cnt

cat = "Romance"
a = av_score(movies, cat)
print(round(a, 3))
