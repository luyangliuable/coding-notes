mean_girls = [97, 17000000, False]
the_shining = [146, 19000000, True]
gone_with_the_wind = [238, 3977000, False]

star_wars = [125, 1977]
raiders = [115, 1981]
mean_girls = [97, 2004]

# from sklearn.metrics.pairwise import euclidean_distances

def distance(movie1, movie2):
    distance = 0
    for i in range(len(movie1)):
         distance += ( movie1[i] - movie2[i] )**2
    return distance ** 0.5 # math.sqrt(distance)

print( distance(star_wars, raiders) )
print( distance(star_wars, mean_girls) )
