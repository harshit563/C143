import csv 

with open("movies.csv") as f:
    reader  = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]
    headers = data[0]

    headers.append("poster_link")

with open("final.csv","a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)

with open("movies_link.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies_links = data[1:]
    
for movie_item in all_movies:
    poster_found = any(movie_item[8] in movies_link_items for movies_link_items in all_movies_links)
    if poster_found:
        for movies_link_item in all_movies_links:
            if movie_item[8] == movies_link_item[0]:
                movie_item.append(movies_link_item[1])
                if len(movie_item) == 28:
                    with open ("final.csv","a+") as f:
                        csvwriter = csvwriter(f)
                        csvwriter.writerow(movie_item)