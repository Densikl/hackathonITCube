cities = {
    'firstCity': {
        'secondCity' : 3200,
        'thirdCity': 2599,
        'sixthCity': 1500
    },
    'secondCity': {
        'fourthCity': 1500,
        'fifthCity': 3600
    },
    'sixthCity': {
        'fourthCity': 7000
    },
    'thirdCity': {

    },
    'fourthCity': {

    },
    'fifthCity': {

    }
}

def searchCheapestWay(map, startingCity):
    cities = list(map.keys())
    prices = {
        startingCity: 0
    }
    queue = []
    queue.append(startingCity)
    while len(queue) > 0:
        neighbours = list(map[queue[0]].keys())
        currentCity = queue[0]
        queue = queue + neighbours
        for neighbour in map[currentCity]:
            if prices.get(neighbour, float('inf')) > prices[currentCity] + map[currentCity][neighbour]:
                prices[neighbour] = prices[currentCity] + map[currentCity][neighbour]
        queue.pop(0)


    print(prices)    

searchCheapestWay(cities, 'firstCity')

