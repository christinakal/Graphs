from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

from util import Stack, opp_dir, bfs

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


# SECOND PASS

s = Stack() # stores unexplored nodes as (destination, move)
traversal_graph = dict()
explored = set()

# seed stack
traversal_graph[player.current_room.id] = dict()
print(f"Current Room ID:{player.current_room.id}")

# push directions ? isnide the stack
for direction in player.current_room.get_exits():
    traversal_graph[player.current_room.id][direction] = '?'
    s.push((player.current_room.id, direction))

# get a list with the unexplored rooms
curr_unexplored = None

# begin the big loop!!!
while s.size() > 0:
    # take the last item
    destination, move = s.pop()

    # check if we're in the destination room if we're not go back
    if player.current_room.id != destination:
        # need to backtrack
        print(f'{player.current_room.id} is not {destination}. Time to backtrack!')
        # check id the bfs will work! - find the shortest path from the current room to the destination
        path = bfs(player.current_room.id, destination, traversal_graph)

        print(f"path:{path}")
        # prints this: so I have to make a for loop except the first one cause it's the same
        # 471 is not 88. Time to backtrack!
        # path:[471, 320, 300, 270, 198, 125, 88]

        # turn path into directional moves
        for room in path[1:]:
            # swap directions and rooms, so go to the other direction to find another room
            swapped = {value: key for key, value in traversal_graph[player.current_room.id].items()}
            print(f"SWAPPED: {swapped}")

            # prints:
            # Room 97

            # (12,11)

            # Exits: [n, s, w]

            # SWAPPED: {94: 'n', 110: 's', 153: 'w'}

            # change the room of the player
            player.travel(swapped[room], True)
            traversal_path.append(swapped[room])
    
    player.travel(move, False)
    traversal_path.append(move)

    # if the player steps into a room that isn't in the traversal graph add a ? to that room 
    if player.current_room.id not in traversal_graph:
        traversal_graph[player.current_room.id] = {direction: '?' for direction in player.current_room.get_exits()}

    # if the player steps into a room that's not explored yet, set it to current room
    if player.current_room.id not in explored:
        traversal_graph[destination][move] = player.current_room.id
        traversal_graph[player.current_room.id][opp_dir(move)] = destination

        # check if destination or current are now explored and add them to the explored array
        if '?' not in traversal_graph[destination].values():
            explored.add(destination)
        
        if '?' not in traversal_graph[player.current_room.id].values():
            explored.add(player.current_room.id)
        else:
            # initialize neighbors dictionary
            neighbors = {}

            # find the distance for all neighbors from the current room
            for direction, room in traversal_graph[player.current_room.id].items():
                if room == '?':
                    #  pleaaaaase work!!!!!!!!!
                    distance = abs(player.current_room.get_coords()[0] - 3) + abs(player.current_room.get_coords()[0] - 5)
                    # print(f"COORDINATES_1:{player.current_room.get_coords()[0]}"
                    # print(f"COORDINATES_2:{player.current_room.get_coords()[0]}"
                    # example: 11-3 + 11-5 -> 8 + 6 -> 14

                    neighbors[(player.current_room.id, direction)] = distance
            # sort the neighbors distances from the closest to farest
            sorted_neighbors = sorted(neighbors.items(), reverse=True)

            # add the neighbors at the end of stack, so the next time the algorithm runs it will take the closest room
            for neighbor in sorted_neighbors:
                s.push(neighbor[0])

# --- END



# DON'T TOUCH!!! - TRAVERSAL TEST 
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
