from Parser import main

cities = main.GetNodes("/Users/denis/code/hackathon/cases.xlsx")

def searchCheapestWay(map, startingCity):
    print(map)
    prices = {
        startingCity: 0
    }
    queue = []
    queue.append(startingCity)
    previousCity = startingCity
    while len(queue) > 0:
        map[queue[0]]
        neighbours = []
        currentCity = queue[0]
        for neighbour in list(map[queue[0]].keys()):
            if neighbour != previousCity:
                neighbours.append(neighbour)
        queue = queue + neighbours
        for neighbour in map[currentCity]:
            if prices.get(neighbour, float('inf')) > prices[currentCity] + map[currentCity][neighbour]:
                prices[neighbour] = prices[currentCity] + map[currentCity][neighbour]
        queue.pop(0)
        previousCity = currentCity


    print(prices)    

searchCheapestWay(cities, 'Город2')

