# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
def player(prev_play, opponent_history=[], my_history=[]):
    opponent_history.append(prev_play)
    abbey = ["R", "R", "S", "S", "P", "P", "R", "P", "S"]
    rest_players = ["R", "S", "P"]
    quincy = "P"
    size = len(opponent_history)
    moves = size % 1000
    turn = size // 1000
    # find first 4 moves of player
    key = opponent_history[turn*1000:turn*1000+4]
    # if less than 4 moves
    if moves < 4:
        my_history.append(rest_players[moves % 3])
        return rest_players[moves % 3]
    else:
        if key == ["", "P", "R", "S"]:
            my_history.append(rest_players[moves % 3])
            return rest_players[moves % 3]
        elif key == ["", "R", "P", "P"]:
            my_history.append(quincy)
            return quincy
        elif turn % 3 == 0:
            last_ten = my_history[-10:]
            most_frequent = max(set(last_ten), key=last_ten.count)
            ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
            my_history.append(ideal_response[ideal_response[most_frequent]])
            return ideal_response[ideal_response[most_frequent]]
        elif key == ["", "R", "R", "R"]:
            my_history.append(rest_players[moves % 3])
            return rest_players[moves % 3]
        else:
            my_history.append(abbey[moves % 9])
            return abbey[moves % 9]
