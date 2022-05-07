if __name__ == "__main__":
    
    #Setting up the routers and network graph using a 2D array
    routers = ['U', 'V', 'W', 'X', 'Y', 'Z']
    displaygraph=[[0, 3, 7, 1, 0, 0],
                  [3, 0, 1, 0, 0, 0],
                  [7, 1, 0, 4, 5, 6],
                  [1, 0, 4, 0, 2, 0],
                  [0, 0, 5, 2, 0, 3],
                  [0, 0, 6, 0, 3, 0]]
    
    #Loading a dictionary with the cost of each edge from source router to destination router
    graph = {0:[0, 1, 3], 1:[0, 2, 7], 2:[0, 3, 1], 3:[1, 2, 1], 4:[1, 3, 1], 
             5:[2, 3, 4], 6:[2, 4, 5], 7:[2, 5, 6], 8:[3, 4, 2], 9:[4, 5, 3]}
    
    #Defining infinity for initiial iterations
    infinity = 100000
    
    #Initial value distances from the source router U to other routers in the Network
    dist = [0, infinity, infinity, infinity, infinity, infinity]

    #Displaying the network and the initial distance from Router U
    print('NETWORK DIAGRAM:')
    print('Displaying the Routers and the Edge Cost:\n')
    print(f'{routers}\n')
    for i in displaygraph:
        print(i)
    print('\nThe initial distance from Router U: ', dist)
    print('\n---------------------------------------------------------------------------------------------------------------------------------------')
    
    #Defining a dictionary to store the value of least hop count from the source Router U
    hop = {0: 0}

    #Using Bellman-Ford Algorithm to find the shortest routing path from source router U
    #Looping for N-1 times, where N equals the number of routers in the network
    for i in range(len(graph)-1):
        for val in graph.values():
            #Checking whether a path exists between two Routers and whether the path has a lesser cost
            if dist[val[0]]!= infinity and dist[val[0]] + val[2] < dist[val[1]]:
                dist[val[1]] = dist[val[0]] + val[2]
                hop[val[1]] = hop[val[0]] + 1
                print(f'\nIteration for Edge {routers[val[0]]} to {routers[val[1]]}')
                print('Routing Table for Router U:')
                print('\n\t Source | Destination | Least-Cost Path to Destination')
                print('\t-------------------------------------------------------')
                for i in range(len(displaygraph)):
                    print(f'\t  {routers[0]}     |      {routers[i]}      |        \t{dist[i]}')
                print('\n---------------------------------------------------------------------------------------------------------------------------------------')
        
    #Checking if there exists a Negative Weight Cycle
    for val in graph.values():
        if dist[val[0]]!= infinity and dist[val[0]] + val[2] < dist[val[1]]:
            print("Graph contains Negative Weight Cycle")
            break

    #Aborting after looping for N-1 times and displaying the results
    print('\nAbort Looping after N-1 times: \n\n--> Final Routing Table for Router U:')
    print('\n\t Destination | Least-Cost Path to Destination')
    print('\t----------------------------------------------')
    for i in range(len(displaygraph)):
        print(f'\t      {routers[i]}      | \t\t    {dist[i]}')
    
    hopList = []
    for key in hop.values():
        hopList.append(key)

    print('\n-->Hop Table:')
    print('\n\t Destination | Number of Hops')
    print('\t------------------------------')
    for i in range(len(displaygraph)):
        print(f'\t      {routers[i]}      | \t     {hopList[i]}')
