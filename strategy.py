"""
A module for strategies.

NOTE: Make sure this file adheres to python-ta.
Adjust the type annotations as needed, and implement both a recursive
and an iterative version of minimax.
"""
from typing import Any, List, Union
# TODO: Adjust the type annotation as needed.
def interactive_strategy(game: Any) -> 'move':
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)

# TODO: Implement a recursive version of the minimax strategy.

class Tree:
    """
    A bare-bones Tree ADT that identifies the root with the entire
    tree from lec.
    """
    def __init__(self, game: object = None, state: object = None,
                 score: object = None, children: List['Tree'] = None) -> None:
        """
        Create Tree self with content value and 0 or more children
        """
        self.game = game
        self.state = state
        self.score = score
        # copy children if not None
        self.children = children.copy() if children else []

def helper_isover(game, state) -> int:
    """
    A helper function that determines whether the state is over or not.
    """
    old_state = game.current_state
    game.current_state = state  # the state you want to check here
    if game.current_state.get_current_player_name() == 'p1':
        player = 'p1'
        player2 = 'p2'
    else:
        player = 'p2'
        player2 = 'p1'
    if game.is_winner(player):
        game.current_state = old_state
        return 1
    elif game.is_winner(player2):
        game.current_state = old_state
        return -1

    game.current_state = old_state
    return 0
    # if game.is_winner(state.get_current_player_name()):
    #     return 1
    # elif not game.is_winner(state.get_current_player_name()):
    #     return -1
    # return 0

def helper_moves(game, new_state, m) -> None: #branching
    """
    A Recursive helper function.
    """
    c = helper_rec_state(game, new_state)
    if type(c) == list:
        b = max(c) * -1
    else:
        b = c * -1
    m.extend([b])

def branch_or_not(game, new_state, m) -> None:
    """
    A Recursive helper function
    """
    if type(helper_rec_state(game, new_state)) == int:
        m.append(helper_rec_state(game, new_state) * -1)
    else:
        # c = helper_rec_state(game, new_state)
        # if type(c) == list:
        #     b = max(c) * -1
        # else:
        #     b = c * -1
        # m.extend([b])
        helper_moves(game, new_state, m)

def helper_rec_state(game, state: 'State') -> Union[List[int], int]:
    """
    Recursive helper function
    """
    if game.is_over(state): #base case
        return helper_isover(game, state)
    else:
        possible_moves = state.get_possible_moves()
        l = [] #final List[int] that is returned,
        # corresponding to each moves' score.
        if len(possible_moves) > 1:
            for move in possible_moves:
                m = []
                new_state = state.make_move(move)
                # if type(helper_rec_state(game, new_state)) == int:
                #     m.append(helper_rec_state(game, new_state) * -1)
                # else:
                #     # c = helper_rec_state(game, new_state)
                #     # if type(c) == list:
                #     #     b = max(c) * -1
                #     # else:
                #     #     b = c * -1
                #     # m.extend([b])
                #     helper_moves(game, new_state, m)
                branch_or_not(game, new_state, m)
                m = max(m)
                l.append(m)
            return l
        else: #a state has only one possible moves
            new_state = state.make_move(possible_moves[0])
            a = helper_rec_state(game, new_state)
            if type(a) == list:
                b = a[0] * -1
            else:
                b = -1 * a
            return [b]


def minimax_rec(game: Any) -> 'move':
    """
    A recursive minimax that returns best move.
    """
    score_lst = helper_rec_state(game, game.current_state)
    #List of score (int)
    possible_lst = game.current_state.get_possible_moves()
    #List of corresponding moves
    for i in range(len(score_lst)):
        if score_lst[i] == 1:
            return possible_lst[i] #return move that corresponds to 1
    return possible_lst[-1]

def rough_outcome_strategy(game: Any) -> Any:
    """
    Return a move for game by picking a move which results in a state with
    the lowest rough_outcome() for the opponent.

    NOTE: game.rough_outcome() should do the following:
        - For a state that's over, it returns the score for the current
          player of that state.
        - For a state that's not over:
            - If there is a move that results in the current player winning,
              return 1.
            - If all moves result in states where the other player can
              immediately win, return -1.
            - Otherwise; return a number between -1 and 1 corresponding to how
              'likely' the current player will win from the current state.

        In essence: rough_outcome() will only look 1 or 2 states ahead to
        'guess' the outcome of the game, but no further. It's better than
        random, but worse than minimax.
    """
    current_state = game.current_state
    best_move = None
    best_outcome = -2  # Temporarily -- just so we can replace this easily later
    # Get the move that results in the lowest rough_outcome for the opponent
    for move in current_state.get_possible_moves():
        new_state = current_state.make_move(move)

        # We multiply the below by -1 since a state that's bad for the opponent
        # is good for us.
        guessed_score = new_state.rough_outcome() * -1
        if guessed_score > best_outcome:
            best_outcome = guessed_score
            best_move = move

    # Return the move that resulted in the best rough_outcome
    return best_move

class _Container():
    """
    A bare-bones Tree-like ADT, similar to that from lecture.

    @param int score: current score
    @param object state: [value, player's turn]
    @param list[Tree|None] children: child nodes
    """

    def __init__(self, state: 'State', score: object = None,
                 children: List['Tree'] = None) -> None:
        self.state = state
        self.score = score
        self.children = children.copy() if children else []


def minimax_iter(game: Any) -> Any:
    """
    A itenrative minimax that returns best move.
    """
    old_state = game.current_state
    current = _Container(game.current_state)
    stack = []
    stack.append(current)
    _last = None
    while stack != []:
        _last = stack.pop(0)
        if game.is_over(_last.state):
            game.current_state = _last.state # the state you want to check here
            if game.current_state.get_current_player_name() == 'p1':
                player = 'p1'
                player2 = 'p2'
            else:
                player = 'p2'
                player2 = 'p1'
            if game.is_winner(player):
                game.current_state = old_state
                _last.score = 1
            elif game.is_winner(player2):
                game.current_state = old_state
                _last.score = -1
            else:
                game.current_state = old_state
                _last.score = 0
            # if game.is_winner(_last.state.get_current_player_name()):
            #     _last.score = 1
            # elif not game.is_winner(_last.state.get_current_player_name()):
            #     _last.score = -1
            # else:
            #     _last.score = 0

        elif _last.children == []: #havent look yet
            last_state = _last.state
            temp = [_last]
            for move in last_state.get_possible_moves():
                children_container = _Container(last_state.make_move(move))
                _last.children.append(children_container)
                temp.append(children_container)
            for i in temp:
                stack.insert(0, i)

            # p2 = [c.state.current_total for c in stack]
            # print(p2[:])
            # [print(s.score) for s in stack]
        elif _last.children != []: #has children, looked before
            _last.score = max([(x.score * -1) for x in _last.children])

    # print("stack is empty!!!!!!!!!!!!!!")
    last_children_final = _last.children[-1]
    for c in _last.children:
        if c.score * -1 == _last.score:
            last_children_final = c

    for mm in _last.state.get_possible_moves():
        if repr(_last.state.make_move(mm)) == \
                repr(last_children_final.state):
            return mm

if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
