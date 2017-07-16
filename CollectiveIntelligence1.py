# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 16:10:47 2017

@author: T3
"""
import math #mostly for the square root function right now, but being able to do math is helpful.
import operator #For sorting the list
import numpy #I expect to need it for the book, so I'd rather have this in place when I do.
import matplotlib #I expect to need it for the book, so I'd rather have this in place when I do.
import pydelicious #I expect to need it for the book, so I'd rather have this in place when I do.
"""
#List comprehension
lt = [1,'a',3,'b',5,'c',7,'d',9,'e']
changeLT = dict([(v,v*2) for v in lt])
print(changeLT)
"""
#a dictionary of movie critics and their ratings of a small set of movies
critics = {
        'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me, and Dupree': 2.5, 'The Night Listener': 3.0},
        'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,'Just My Luck': 1.5, 'Superman Returns': 5.0, 'You, Me, and Dupree': 3.5, 'The Night Listener': 3.0},
        'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0, 'Superman Returns': 3.5, 'The Night Listener': 4.0},
        'Claudia Puig': {'Snakes on a Plane': 3.5,'Just My Luck': 3.0, 'Superman Returns': 4.0, 'You, Me, and Dupree': 2.5, 'The Night Listener': 4.5},
        'Mick Lasalle': {'Lady in the Water': 3.0,'Snakes on a Plane': 4.0,'Just My Luck': 2.0, 'Superman Returns': 3.0, 'You, Me, and Dupree': 2.0, 'The Night Listener': 3.0},
        'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 'Superman Returns': 5.0, 'You, Me, and Dupree': 3.5, 'The Night Listener': 3.0},
        'Toby':{'Snakes on a Plane': 4.5, 'Superman Returns': 4.0, 'You, Me, and Dupree': 1.0}
        }

#print(critics['Lisa Rose'])
#print(critics['Lisa Rose']['Lady in the Water'])
#print(critics['Toby'])
#print(critics['Toby']['Snakes on a Plane'])
#critics['Toby']['Snakes on a Plane'] = 4.5
#print(critics['Toby']['Snakes on a Plane'])
"""
Critic1 = input('Critic 1:')
Critic2 = input('Critic 2:')
Movie1 = input('Movie 1:')
Movie2 = input('Movie 2:')
print(Critic1, "vs.", Critic2, ":", Movie1, "vs.", Movie2)
Critic1Movie1 = critics[str(Critic1)][str(Movie1)]
Critic2Movie1 = critics[str(Critic2)][str(Movie1)]
Critic1Movie2 = critics[str(Critic1)][str(Movie2)]
Critic2Movie2 = critics[str(Critic2)][str(Movie2)]
Movie1Dist = Critic1Movie1 - Critic2Movie1
Movie2Dist = Critic1Movie2 - Critic2Movie2
Dist = math.sqrt(Movie1Dist**2 + Movie2Dist**2)
invertDist = 1/(Dist+1)
print("Final inverted distance is", invertDist)
"""

def sim_distance(ranking,Critic1,Critic2):
    sumSquares = 0
#Given two critics we want the euclidean distance between them.
    #print(Critic1, "vs.", Critic2)
#Cycle through the movies in one or the other list
    if ranking[str(Critic1)] != ranking[str(Critic2)]:
        #print('0')
    #else:
        #iterate through critic 1's list
        for movie in ranking[str(Critic1)]:
            if movie in ranking[str(Critic2)]:
                sumSquares += (ranking[str(Critic1)][str(movie)] - ranking[str(Critic2)][str(movie)])**2
        euclideanDistance = math.sqrt(sumSquares)
        finalDistance = 1/(euclideanDistance + 1)
    return finalDistance
        #print(finalDistance)
#print(sim_distance('Lisa Rose', 'Gene Seymour'))

def sim_pearson(ranking, Critic1,Critic2):
 EXY = 0
 EX = 0
 EXS = 0
 SDX = 0
 EY = 0
 EYS = 0
 SDY = 0
 count = 0
 #We are going to calculate peason correlation like a mathematician.
 #Correlation of two random variables is covariance(X,Y)/(standardDeviationX*standardDeviationY)
 #Covariance is defined mathematically as 'Expectaion of XY minus (Expectation of X) times
 # (Expectation of Y). More concisely: E[XY]-(E[X])*(E[Y])
 #So first we find the expectation (weighted average) of the product of the critics' ratings for each movie
 for movie in ranking[str(Critic1)]:
  if movie in ranking[str(Critic2)]:
   EXY += float((ranking[str(Critic1)][str(movie)] * ranking[str(Critic2)][str(movie)]))
   count += 1
 EXY /= count
  #Now we'll find the expectation of the first critic's movie ratings. This is E[X].
 count = 0 
 for movie in ranking[str(Critic1)]:
  if movie in ranking[str(Critic2)]:
   EX += float(ranking[str(Critic1)][str(movie)])
   count += 1
 EX /= count
  #Now we'll find the expectation of the second critic's movie ratings. This is E[Y]
 count = 0 #reset the count variable so that I can use it again.
 for movie in ranking[str(Critic2)]:
  if movie in ranking[str(Critic1)]:
   EY += float(ranking[str(Critic2)][str(movie)])
   count += 1
 EY /= count
 #Find standard deviation. In order to do  this we must find the variance of the ratings given by each critic. Variance is defined as the difference between the expectation of the square of the random variable and the square of the expectation of the random variable. More concisely: V(X) = E[X^2] - (E[X])^2
  #Find E[X^2]
 count = 0
 for movie in ranking[str(Critic1)]:
  if movie in ranking[str(Critic2)]:
   EXS += (float(ranking[str(Critic1)][str(movie)]))**2
   count += 1
 EXS /= count 
  #Find E[Y^2]
 count = 0
 for movie in ranking[str(Critic2)]:
  if movie in ranking[str(Critic1)]:
   EYS += (float(ranking[str(Critic2)][str(movie)]))**2
   count += 1
 EYS /= count
  #Standard Deviation of X. The standard deviation of a random variable is the square root of the variance of that random variable.
 SDX = math.sqrt(EXS - EX**2)
  #Variance of Y
 SDY = math.sqrt(EYS - EY**2)
 #Final Calculation. Use the definition of the pearson correlation coefficient as noted above.
 PCC = (EXY - EX*EY)/(SDX*SDY)
 return PCC
 #Can print out result to assist in debugging
 #print('The correlation coefficient for', Critic1, 'and', Critic2, 'is', PCC)
#print(sim_pearson('Toby', 'Michael Phillips'))

def topMatches(ranking, person, n, similarity):

    #create a list of the correlation coefficients for each other critic in the list.
    scores = [(similarity(ranking, person, other), other) for other in ranking if other != person]
    
    scores.sort() #Sort the results in ascending order. This is least to greatest correlation
    scores.reverse() #Reverse the list so that we see the top correlations first in the list.
    
    print(scores[0:n]) #Show the top 'n' correlations

def getRecommendations(ranking, person, similarity, numberRecommendations, includeNegatives):
    rawScore = {}
    movieSim = {}
    finalRecommendation = {}
    #Loop critics
    for eachCritic in ranking:
        #Not me
        if eachCritic == person:
            continue
        #Skip the step if we don't want negative correlations to affect the outcome.
        if (similarity(ranking, person, eachCritic) <= 0) and (includeNegatives == 'FALSE'):
            continue
        #Loop movies
        for movie in ranking[str(eachCritic)]:
            #That I haven't rated
            if movie in ranking[str(person)]:
                continue
            #Add rating*similarity to scoreDraft array for that movie
            rawScore.setdefault(movie, 0) #make sure we start at zero
            rawScore[movie] += (similarity(ranking, person, eachCritic)*(float(ranking[str(eachCritic)][str(movie)]))) #summing up the product of the coefficient times the rating
            #print(eachCritic, movie, similarity(person, eachCritic), (float(ranking[str(eachCritic)][str(movie)])), similarity(person, eachCritic)*(float(ranking[str(eachCritic)][str(movie)])))
            #Add similarity to movieSim array for that movie
            movieSim.setdefault(movie, 0)
            movieSim[movie] += similarity(ranking, person, eachCritic) #sum up the correlations for that movie. This will allow us to divide the raw score so as to get the weighted average.
    
    #For every movie
    for eachMovie in movieSim:
        #finalRecommendation = Divide scoreDraft for that movie by movieSim for that movie
        finalRecommendation.setdefault(eachMovie, 0)
        finalRecommendation[eachMovie] = (rawScore[eachMovie]/movieSim[eachMovie])
    #Print out top x of the final Recommendations list
    sortedFinalRecommendation = sorted(finalRecommendation.items(), key=operator.itemgetter(1))
    sortedFinalRecommendation.reverse()
    print (sortedFinalRecommendation[0:numberRecommendations])

#getRecommendations(critics, 'Toby', sim_pearson, 3, 'FALSE')

def transformPrefs(prefs):
    movies = {} #start with a blank library
    for eachCritic in prefs: #iterate through all of the critics
        for eachMovie in prefs[eachCritic]: #iterate through each movie rated by that critic
            movies.setdefault(eachMovie, {}) #initiate the dectionary level 1 with the movie name
            movies[eachMovie][eachCritic] = prefs[eachCritic][eachMovie]
    return movies

#print(transformPrefs(critics))

movies = transformPrefs(critics) 
#topMatches(movies, 'Superman Returns', 5, sim_pearson)
#getRecommendations(movies, 'Just My Luck', sim_pearson, 3, 'FALSE')
    