"""
An implementation of Stonehenge Game.
"""
from typing import Any
from game import Game
from game_state import GameState

class StonehengeGame(Game):
    """
    Abstract class for a game to be played with two players.
    """
    def __init__(self, p1_starts):
        """
        Initialize this Game, using p1_starts to find who the first player is.

        :param p1_starts: A boolean representing whether Player 1 is the first
                          to make a move.
        :type p1_starts: bool
        """
        length = int(input("Enter the side length of the board: "))
        self.current_state = StonehengeState(p1_starts, length)

    def get_instructions(self):
        """
        Return the instructions for this Game.

        :return: The instructions for this Game.
        :rtype: str
        """
        instructions = "Players take turns claiming cells . When a player " \
                       "captures at least half " \
                       "of the cells in a ley-line, then the player captures " \
                       "that ley-line. The first " \
                       "player to capture at least half of the ley-lines is " \
                       "the winner. A ley-line, " \
                       "once claimed, cannot be taken by the other player"
        return instructions

    def is_over(self, state):
        """
        Return whether or not this game is over.

        :return: True if the game is over, False otherwise.
        :rtype: bool
        """
        all_ley = (3 * (state.length) + 3)
        least_ley = int(all_ley / 2) + (all_ley % 2 > 0)

        p1_score = 0
        p2_score = 0
        for i in state.init_ley:
            if state.init_ley[i] == "1":
                p1_score += 1
            elif state.init_ley[i] == "2":
                p2_score += 1


        return (p2_score >= least_ley) or (p1_score >= least_ley)

    def is_winner(self, player):
        """
        Return whether player has won the game.

        Precondition: player is 'p1' or 'p2'.

        :param player: The player to check.
        :type player: str
        :return: Whether player has won or not.
        :rtype: bool
        """
        p1_score = 0
        p2_score = 0
        for i in self.current_state.init_ley:
            if self.current_state.init_ley[i] == "1":
                p1_score += 1
            elif self.current_state.init_ley[i] == "2":
                p2_score += 1

        if player == 'p1' and \
                self.current_state.get_current_player_name() == 'p2' \
                and self.is_over(self.current_state) and \
                p2_score < p1_score:
            return True
        elif player == 'p2' and \
                self.current_state.get_current_player_name() == 'p1' \
                and self.is_over(self.current_state) and \
                p2_score > p1_score:
            return True
        return False

    def str_to_move(self, string):
        """
        Return the move that string represents. If string is not a move,
        return an invalid move.

        :param string:
        :type string:
        :return: string
        :rtype: str
        """
        if not string.strip().isalpha():
            return -1
        return string.strip().upper()




class StonehengeState(GameState):
    """
    The state of a game at a certain point in time.
    """

    def __init__(self, is_p1_turn: bool, length: int) -> None:
        """
        Initialize this game state and set the current player based on
        is_p1_turn.
        """
        super().__init__(is_p1_turn)
        self.length = length

        if self.length == 1:
            self.init_alpha = {'A': 'A', 'B': 'B', 'C': 'C'}
            self.init_ley = {'/1': '@', '/2': '@',
                             '\1': '@', '\2': '@',
                             '-1': '@', '-2': '@'}

        elif self.length == 2:
            self.init_alpha = {'A': 'A', 'B': 'B', 'C': 'C',
                               'D': 'D', 'E': 'E', 'F': 'F',
                               'G': 'G'}
            self.init_ley = {'/1': '@', '/2': '@', '/3': '@',
                             '\1': '@', '\2': '@', '\3': '@',
                             '-1': '@', '-2': '@', '-3': '@'}

        elif self.length == 3:
            self.init_alpha = {'A': 'A', 'B': 'B', 'C': 'C',
                               'D': 'D', 'E': 'E', 'F': 'F',
                               'G': 'G', 'H': 'H', 'I': 'I',
                               'J': 'J', 'K': 'K', 'L': 'L'}
            self.init_ley = {'/1': '@', '/2': '@', '/3': '@', '/4': '@',
                             '\1': '@', '\2': '@', '\3': '@', '\4': '@',
                             '-1': '@', '-2': '@', '-3': '@', '-4': '@'}

        elif self.length == 4:
            self.init_alpha = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D',
                               'E': 'E', 'F': 'F', 'G': 'G', 'H': 'H', 'I': 'I',
                               'J': 'J', 'K': 'K', 'L': 'L', 'M': 'M',
                               'N': 'N', 'O': 'O', 'P': 'P', 'Q': 'Q', 'R': 'R'}
            self.init_ley = {'/1': '@', '/2': '@', '/3': '@',
                             '/4': '@', '/5': '@',
                             '\1': '@', '\2': '@', '\3': '@',
                             '\4': '@', '\5': '@',
                             '-1': '@', '-2': '@', '-3': '@',
                             '-4': '@', '-5': '@'}
        else:
            self.init_alpha = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D',
                               'E': 'E', 'F': 'F', 'G': 'G', 'H': 'H', 'I': 'I',
                               'J': 'J', 'K': 'K', 'L': 'L', 'M': 'M',
                               'N': 'N', 'O': 'O', 'P': 'P', 'Q': 'Q', 'R': 'R',
                               'S': 'S', 'T': 'T', 'U': 'U', 'V': 'V',
                               'W': 'W', 'X': 'X', 'Y': 'Y'}

            self.init_ley = {'/1': '@', '/2': '@', '/3': '@',
                             '/4': '@', '/5': '@', '/6': '@',
                             '\1': '@', '\2': '@', '\3': '@',
                             '\4': '@', '\5': '@', '\6': '@',
                             '-1': '@', '-2': '@', '-3': '@',
                             '-4': '@', '-5': '@', '-6': '@'}


    def __str__(self) -> str:
        """
        Return a string representation of the current state of the game.
        >>> s = StonehengeState(True, 2)
        >>> print(s)
        """
        if self.length == 1:
            return "      "+ self.init_ley['/1'] + \
                   "   " + self.init_ley['/2'] + "\n" + \
                   '     ' + '/' + '   ' + '/' + "\n" + \
                   self.init_ley['-1'] + " - " + \
                   self.init_alpha['A'] + " - " + \
                   self.init_alpha['B'] + "\n" + \
                   "     " + "\\" + " /" + " \\" + " \n" + \
                   "  " + self.init_ley['-2'] + " - " + \
                   self.init_alpha['C'] + "   " + \
                   self.init_ley['\2'] + "\n" + \
                   "       " + "\\" + " \n" + \
                   "        " + self.init_ley['\1']

        elif self.length == 2:
            return "        " + self.init_ley['/1'] + "   " + \
                   self.init_ley['/2'] + "\n" + \
                   "       /   / \n" + \
                   "  " + self.init_ley['-1'] + " - " + \
                   self.init_alpha['A'] + " - " + \
                   self.init_alpha['B'] \
                   + "   " + self.init_ley['/3'] + "\n" + \
                   "     " + "/" + " " + "\\" + " /" + " " + \
                   "\\" + " " + "/" + " \n" + \
                   self.init_ley['-2'] + " - " + \
                   self.init_alpha['C'] + " - " + self.init_alpha['D'] + \
                   " - " + self.init_alpha['E'] + "\n" + \
                   "     " + "\\" + " " + "/" + " " + "\\" + " " + \
                   "/" + " " + "\\" + " \n" + \
                   "  " + self.init_ley['-3'] + " - " + \
                   self.init_alpha['F'] + " - " + self.init_alpha['G'] \
                   + "   " + self.init_ley['\3'] + "\n" + \
                   "       " + "\\" + "   " + "\\" + " \n" + \
                   "        " + self.init_ley['\1'] + "   " + \
                   self.init_ley['\2']

        elif self.length == 3:
            return "          " + self.init_ley['/1'] + "   " + \
                   self.init_ley['/2'] + "\n" + \
                   "         /   / \n" + \
                   "    " + self.init_ley['-1'] + " - " + \
                   self.init_alpha['A'] + " - " + self.init_alpha['B'] \
                   + "   " + self.init_ley['/3'] + "\n" + \
                   "       / \ / \ / \n" + \
                   "  " + self.init_ley['-2'] + " - " + \
                   self.init_alpha['C'] + " - " + self.init_alpha['D'] + \
                   " - " + self.init_alpha['E'] + "   " + \
                   self.init_ley['/4'] + "\n" + \
                   "     " + "/" + " \ / \ / \ / \n" + \
                   self.init_ley['-3'] + " - " + \
                   self.init_alpha['F'] + " - " + self.init_alpha['G'] \
                   + " - " + self.init_alpha['H'] + " - " + \
                   self.init_alpha['I'] + "\n" + \
                   "     \ / \ / \ / \ \n" + \
                   "  " + self.init_ley['-4'] + " - " + \
                   self.init_alpha['J'] + " - " + self.init_alpha['K'] \
                   + " - " + self.init_alpha['L'] + "   " + \
                   self.init_ley['\4'] + "\n" + \
                   "       \   \   \ \n" + \
                   "        " + self.init_ley['\1'] + "   " + \
                   self.init_ley['\2'] + "   " + self.init_ley['\3']

        elif self.length == 4:
            return "            " + self.init_ley['/1'] + "   " + \
                   self.init_ley['/2'] + "\n" + \
                   "           /   / \n" + \
                   "      " + self.init_ley['-1'] + " - " + \
                   self.init_alpha['A'] + " - " + self.init_alpha['B'] \
                   + "   " + self.init_ley['/3'] + "\n" + \
                   "         / \ / \ / \n" + \
                   "    " + self.init_ley['-2'] + " - " + \
                   self.init_alpha['C'] + " - " + self.init_alpha['D'] + \
                   " - " + self.init_alpha['E'] + "   " + \
                   self.init_ley['/4'] + "\n" + \
                   "       / \ / \ / \ / \n" + \
                   "  " + self.init_ley['-3'] + " - " + \
                   self.init_alpha['F'] + " - " + self.init_alpha['G'] \
                   + " - " + self.init_alpha['H'] + " - " + \
                   self.init_alpha['I'] + "   " + \
                   self.init_ley['/5'] + "\n" + \
                   "     / \ / \ / \ / \ / \n" + \
                   self.init_ley['-4'] + " - " + self.init_alpha['J'] + \
                   " - " + self.init_alpha['K'] \
                   + " - " + self.init_alpha['L'] + " - " + \
                   self.init_alpha['M'] + " - " + \
                   self.init_alpha['N'] + "\n" + \
                   "     \ / \ / \ / \ / \ \n" + \
                   "  " + self.init_ley['-5'] + " - " + \
                   self.init_alpha['O'] + " - " + self.init_alpha['P'] + \
                   " - " + \
                   self.init_alpha['Q'] + " - " + self.init_alpha['R'] + \
                   "   " + self.init_ley['\5'] + "\n" \
                   + "       \   \   \   \ \n" + \
                   "        " + self.init_ley['\1'] + "   " + \
                   self.init_ley['\2'] + "   " + self.init_ley['\3'] \
                   + "   " + self.init_ley['\4']

        return "              " + self.init_ley['/1'] + "   " + \
               self.init_ley['/2'] + "\n" + \
               "             /   / \n" + \
               "        " + self.init_ley['-1'] + " - " + \
               self.init_alpha['A'] + " - " + self.init_alpha['B'] \
               + "   " + self.init_ley['/3'] + "\n" + \
               "           / \ / \ / \n" + \
               "      " + self.init_ley['-2'] + " - " + \
               self.init_alpha['C'] + " - " + self.init_alpha['D'] + \
               " - " + self.init_alpha['E'] + "   " + \
               self.init_ley['/4'] + "\n" + \
               "         / \ / \ / \ / \n" + \
               "    " + self.init_ley['-3'] + " - " + \
               self.init_alpha['F'] + " - " + self.init_alpha['G'] \
               + " - " + self.init_alpha['H'] + " - " + \
               self.init_alpha['I'] + "   " + self.init_ley['/5'] + "\n" + \
               "       / \ / \ / \ / \ / \n" + \
               "  " + self.init_ley['-4'] + " - " + \
               self.init_alpha['J'] + " - " + self.init_alpha['K'] \
               + " - " + self.init_alpha['L'] + " - " + \
               self.init_alpha['M'] + " - " \
               + self.init_alpha['N'] + "   " + \
               self.init_ley['/6'] + "\n" + \
               "     / \ / \ / \ / \ / \ / \n" + \
               self.init_ley['-5'] + " - " + self.init_alpha['O'] + \
               " - " + self.init_alpha['P'] + " - " + \
               self.init_alpha['Q'] + " - " + self.init_alpha['R'] + \
               " - " + \
               self.init_alpha['S'] + " - " + self.init_alpha['T'] + \
               "\n" \
               + "     \ / \ / \ / \ / \ / \ \n" + \
               "  " + self.init_ley['-6'] + " - " + \
               self.init_alpha['U'] + " - " + self.init_alpha['V'] + \
               " - " + self.init_alpha['W'] + " - " + \
               self.init_alpha['X'] + " - " + \
               self.init_alpha['Y'] + "   " + \
               self.init_ley['\6'] + "\n" + \
               "       \   \   \   \   \ \n" + \
               "        " + self.init_ley['\1'] + "   " + \
               self.init_ley['\2'] + "   " + self.init_ley['\3'] \
               + "   " + self.init_ley['\4'] + "   " +\
               self.init_ley['\5']

    def get_possible_moves(self) -> list:
        """
        Return all possible moves that can be applied to this state.

        >>> s = StonehengeState(True, 1)
        >>> s.get_possible_moves()
        ['A', 'B', 'C']
        >>> s.init_alpha['A'] = str(2)
        >>> s.get_possible_moves()
        ['B', 'C']
        >>> s = StonehengeState(True, 2)
        >>> s.init_alpha['B'] = str(1)
        >>> s.init_alpha['K'] = str(2)
        >>> s.get_possible_moves()
        ['A', 'C', 'D', 'E', 'F', 'G']
        """
        all_ley = (3 * (self.length) + 3)
        least_ley = int(all_ley / 2) + (all_ley % 2 > 0)

        p1_score = 0
        p2_score = 0
        for i in self.init_ley:
            if self.init_ley[i] == "1":
                p1_score += 1
            elif self.init_ley[i] == "2":
                p2_score += 1

        if (p2_score >= least_ley) or (p1_score >= least_ley):
            return []

        return [self.init_alpha[a] for a
                in self.init_alpha if (self.init_alpha[a]
                                       != str(2) and
                                       self.init_alpha[a] != str(1))]


    def make_move(self, move: Any) -> "StonehengeState":
        """
        Return the GameState that results from applying move to this GameState.
        """
        if type(move) == str:
            move.upper()

        new_init_alpha = self.init_alpha.copy()
        new_init_ley = self.init_ley.copy()
        if self.p1_turn:
            player_no = "1"
        else:
            player_no = "2"

        for a in new_init_alpha:
            if new_init_alpha[a] == move:
                new_init_alpha[a] = player_no

        new_state = StonehengeState(not self.p1_turn, self.length)
        new_state.init_alpha = new_init_alpha
        new_state.init_ley = new_init_ley

        if new_state.length == 1:
            if (new_state.init_alpha['A'] == player_no) and \
                    new_state.init_ley['/1'] == '@':
                new_state.init_ley['/1'] = player_no
            if (new_state.init_alpha['B'] == player_no or
                    new_state.init_alpha['C'] == player_no) and \
                    new_state.init_ley['/2'] == '@':
                new_state.init_ley['/2'] = player_no
            if (new_state.init_alpha['B'] == player_no or
                    new_state.init_alpha['A'] == player_no) \
                    and new_state.init_ley['-1'] == '@':
                new_state.init_ley['-1'] = player_no
            if (new_state.init_alpha['C'] == player_no) and \
                    new_state.init_ley['-2'] == '@':
                new_state.init_ley['-2'] = player_no
            if (new_state.init_alpha['A'] == player_no or
                    new_state.init_alpha['C'] == player_no) \
                    and new_state.init_ley['\1'] == '@':
                new_state.init_ley['\1'] = player_no
            if (new_state.init_alpha['B'] == player_no) and \
                    new_state.init_ley['\2'] == '@':
                new_state.init_ley['\2'] = player_no

        elif new_state.length == 2:
            if (new_state.init_alpha['A'] == player_no or
                    new_state.init_alpha['C'] == player_no) \
                    and new_state.init_ley['/1'] == '@':
                new_state.init_ley['/1'] = player_no
            if ([new_state.init_alpha['B'], new_state.init_alpha['D'],
                 new_state.init_alpha['F']].count(player_no) >= 2) and \
                    new_state.init_ley['/2'] == '@':
                new_state.init_ley['/2'] = player_no
            if (new_state.init_alpha['E'] == player_no or
                    new_state.init_alpha['G'] == player_no) and \
                    new_state.init_ley['/3'] == '@':
                new_state.init_ley['/3'] = player_no
            if (new_state.init_alpha['A'] == player_no or
                    new_state.init_alpha['B'] == player_no) \
                    and new_state.init_ley['-1'] == '@':
                new_state.init_ley['-1'] = player_no
            if ([new_state.init_alpha['C'],
                 new_state.init_alpha['D'], new_state.init_alpha['E']].count(
                     player_no) >= 2) and new_state.init_ley['-2'] == '@':
                new_state.init_ley['-2'] = player_no
            if (new_state.init_alpha['F'] == player_no or
                    new_state.init_alpha['G'] == player_no) and \
                    new_state.init_ley['-3'] == '@':
                new_state.init_ley['-3'] = player_no
            if (new_state.init_alpha['C'] == player_no or
                    new_state.init_alpha['F'] == player_no) and \
                    new_state.init_ley['\1'] == '@':
                new_state.init_ley['\1'] = player_no
            if ([new_state.init_alpha['A'], new_state.init_alpha['D'],
                 new_state.init_alpha['G']].count(
                     player_no) >= 2) and new_state.init_ley['\2'] == '@':
                new_state.init_ley['\2'] = player_no
            if (new_state.init_alpha['B'] == player_no or
                    new_state.init_alpha['E'] == player_no) and \
                    new_state.init_ley['\3'] == '@':
                new_state.init_ley['\3'] = player_no

        elif new_state.length == 3:
            if ([new_state.init_alpha['A'], new_state.init_alpha['C'],
                 new_state.init_alpha['F']].count(player_no) >= 2) and \
                    new_state.init_ley['/1'] == '@':
                new_state.init_ley['/1'] = player_no
            if ([new_state.init_alpha['B'], new_state.init_alpha['D'],
                 new_state.init_alpha['G'],
                 new_state.init_alpha['J']].count(player_no) >= 2) and \
                    new_state.init_ley['/2'] == '@':
                new_state.init_ley['/2'] = player_no
            if ([new_state.init_alpha['E'], new_state.init_alpha['H'],
                 new_state.init_alpha['K']].count(player_no) >= 2) and \
                    new_state.init_ley['/3'] == '@':
                new_state.init_ley['/3'] = player_no
            if ([new_state.init_alpha['I'],
                 new_state.init_alpha['L']].count(player_no) >= 1) and \
                    new_state.init_ley['/4'] == '@':
                new_state.init_ley['/4'] = player_no

            if ([new_state.init_alpha['A'],
                 new_state.init_alpha['B']].count(player_no) >= 1)  \
                    and new_state.init_ley['-1'] == '@':
                new_state.init_ley['-1'] = player_no
            if ([new_state.init_alpha['C'], new_state.init_alpha['D'],
                 new_state.init_alpha['E']].count(player_no) >= 2) and \
                    new_state.init_ley['-2'] == '@':
                new_state.init_ley['-2'] = player_no
            if ([new_state.init_alpha['F'], new_state.init_alpha['G'],
                 new_state.init_alpha['H'],
                 new_state.init_alpha['I']].count(player_no) >= 2) and \
                    new_state.init_ley['-3'] == '@':
                new_state.init_ley['-3'] = player_no
            if ([new_state.init_alpha['J'], new_state.init_alpha['K'],
                 new_state.init_alpha['L']].count(player_no) >= 2) and \
                    new_state.init_ley['-4'] == '@':
                new_state.init_ley['-4'] = player_no

            if ([new_state.init_alpha['F'],
                 new_state.init_alpha['J']].count(player_no) >= 1) and \
                    new_state.init_ley['\1'] == '@':
                new_state.init_ley['\1'] = player_no
            if ([new_state.init_alpha['C'], new_state.init_alpha['G'],
                 new_state.init_alpha['K']].count(player_no) >= 2) and \
                    new_state.init_ley['\2'] == '@':
                new_state.init_ley['\2'] = player_no
            if ([new_state.init_alpha['A'], new_state.init_alpha['D'],
                 new_state.init_alpha['H'],
                 new_state.init_alpha['L']].count(player_no) >= 2) and \
                    new_state.init_ley['\3'] == '@':
                new_state.init_ley['\3'] = player_no
            if ([new_state.init_alpha['B'], new_state.init_alpha['E'],
                 new_state.init_alpha['I']].count(player_no) >= 2) and \
                    new_state.init_ley['\4'] == '@':
                new_state.init_ley['\4'] = player_no

        elif new_state.length == 4:
            if ([new_state.init_alpha['A'],
                 new_state.init_alpha['C'], new_state.init_alpha['F'],
                 new_state.init_alpha['J']].count(player_no) >= 2) and \
                    new_state.init_ley['/1'] == '@':
                new_state.init_ley['/1'] = player_no
            if ([new_state.init_alpha['B'], new_state.init_alpha['D'],
                 new_state.init_alpha['G'],
                 new_state.init_alpha['K'],
                 new_state.init_alpha['O']].count(player_no) >= 3) and \
                    new_state.init_ley['/2'] == '@':
                new_state.init_ley['/2'] = player_no
            if ([new_state.init_alpha['E'],
                 new_state.init_alpha['H'], new_state.init_alpha['L'],
                 new_state.init_alpha['P']].count(player_no) >= 2) and \
                    new_state.init_ley['/3'] == '@':
                new_state.init_ley['/3'] = player_no
            if ([new_state.init_alpha['I'], new_state.init_alpha['M'],
                 new_state.init_alpha['Q']].count(player_no) >= 2) and \
                    new_state.init_ley['/4'] == '@':
                new_state.init_ley['/4'] = player_no
            if ([new_state.init_alpha['N'],
                 new_state.init_alpha['R']].count(player_no) >= 1) and \
                    new_state.init_ley['/5'] == '@':
                new_state.init_ley['/5'] = player_no

            if ([new_state.init_alpha['A'],
                 new_state.init_alpha['B']].count(player_no) >= 1)  \
                    and new_state.init_ley['-1'] == '@':
                new_state.init_ley['-1'] = player_no
            if ([new_state.init_alpha['C'],
                 new_state.init_alpha['D'],
                 new_state.init_alpha['E']].count(player_no) >= 2) and \
                    new_state.init_ley['-2'] == '@':
                new_state.init_ley['-2'] = player_no
            if ([new_state.init_alpha['F'], new_state.init_alpha['G'],
                 new_state.init_alpha['H'],
                 new_state.init_alpha['I']].count(player_no) >= 2) and \
                    new_state.init_ley['-3'] == '@':
                new_state.init_ley['-3'] = player_no
            if ([new_state.init_alpha['J'], new_state.init_alpha['K'],
                 new_state.init_alpha['L'],
                 new_state.init_alpha['M'],
                 new_state.init_alpha['N']].count(player_no) >= 3) and \
                    new_state.init_ley['-4'] == '@':
                new_state.init_ley['-4'] = player_no
            if ([new_state.init_alpha['O'], new_state.init_alpha['P'],
                 new_state.init_alpha['Q'],
                 new_state.init_alpha['R']].count(player_no) >= 2) and \
                    new_state.init_ley['-5'] == '@':
                new_state.init_ley['-5'] = player_no

            if ([new_state.init_alpha['J'],
                 new_state.init_alpha['O']].count(player_no) >= 1) and \
                    new_state.init_ley['\1'] == '@':
                new_state.init_ley['\1'] = player_no
            if ([new_state.init_alpha['F'],
                 new_state.init_alpha['K'],
                 new_state.init_alpha['P']].count(player_no) >= 2) and \
                    new_state.init_ley['\2'] == '@':
                new_state.init_ley['\2'] = player_no
            if ([new_state.init_alpha['C'], new_state.init_alpha['G'],
                 new_state.init_alpha['L'],
                 new_state.init_alpha['Q']].count(player_no) >= 2) and \
                    new_state.init_ley['\3'] == '@':
                new_state.init_ley['\3'] = player_no
            if ([new_state.init_alpha['A'], new_state.init_alpha['D'],
                 new_state.init_alpha['H'],
                 new_state.init_alpha['M'],
                 new_state.init_alpha['R']].count(player_no) >= 3) and \
                    new_state.init_ley['\4'] == '@':
                new_state.init_ley['\4'] = player_no
            if ([new_state.init_alpha['B'], new_state.init_alpha['E'],
                 new_state.init_alpha['I'],
                 new_state.init_alpha['N']].count(player_no) >= 2) and \
                    new_state.init_ley['\5'] == '@':
                new_state.init_ley['\5'] = player_no

        else:
            if ([new_state.init_alpha['A'], new_state.init_alpha['C'],
                 new_state.init_alpha['F'],
                 new_state.init_alpha['J'],
                 new_state.init_alpha['O']].count(player_no) >= 3) and \
                    new_state.init_ley['/1'] == '@':
                new_state.init_ley['/1'] = player_no
            if ([new_state.init_alpha['B'], new_state.init_alpha['D'],
                 new_state.init_alpha['G'],
                 new_state.init_alpha['K'], new_state.init_alpha['P'],
                 new_state.init_alpha['U']].count(player_no) >= 3) and \
                    new_state.init_ley['/2'] == '@':
                new_state.init_ley['/2'] = player_no
            if ([new_state.init_alpha['E'], new_state.init_alpha['H'],
                 new_state.init_alpha['L'],
                 new_state.init_alpha['Q'],
                 new_state.init_alpha['V']].count(player_no) >= 3) and \
                    new_state.init_ley['/3'] == '@':
                new_state.init_ley['/3'] = player_no
            if ([new_state.init_alpha['I'], new_state.init_alpha['M'],
                 new_state.init_alpha['R'],
                 new_state.init_alpha['W']].count(player_no) >= 2) and \
                    new_state.init_ley['/4'] == '@':
                new_state.init_ley['/4'] = player_no
            if ([new_state.init_alpha['N'], new_state.init_alpha['S'],
                 new_state.init_alpha['X']].count(player_no) >= 2) and \
                    new_state.init_ley['/5'] == '@':
                new_state.init_ley['/5'] = player_no
            if ([new_state.init_alpha['T'],
                 new_state.init_alpha['Y']].count(player_no) >= 1) and \
                    new_state.init_ley['/6'] == '@':
                new_state.init_ley['/6'] = player_no

            if ([new_state.init_alpha['A'],
                 new_state.init_alpha['B']].count(player_no) >= 1)  \
                    and new_state.init_ley['-1'] == '@':
                new_state.init_ley['-1'] = player_no
            if ([new_state.init_alpha['C'], new_state.init_alpha['D'],
                 new_state.init_alpha['E']].count(player_no) >= 2) and \
                    new_state.init_ley['-2'] == '@':
                new_state.init_ley['-2'] = player_no
            if ([new_state.init_alpha['F'], new_state.init_alpha['G'],
                 new_state.init_alpha['H'],
                 new_state.init_alpha['I']].count(player_no) >= 2) and \
                    new_state.init_ley['-3'] == '@':
                new_state.init_ley['-3'] = player_no
            if ([new_state.init_alpha['J'], new_state.init_alpha['K'],
                 new_state.init_alpha['L'],
                 new_state.init_alpha['M'],
                 new_state.init_alpha['N']].count(player_no) >= 3) and \
                    new_state.init_ley['-4'] == '@':
                new_state.init_ley['-4'] = player_no
            if ([new_state.init_alpha['O'], new_state.init_alpha['P'],
                 new_state.init_alpha['Q'],
                 new_state.init_alpha['R'], new_state.init_alpha['S'],
                 new_state.init_alpha['T']].count(player_no) >= 3) and \
                    new_state.init_ley['-5'] == '@':
                new_state.init_ley['-5'] = player_no
            if ([new_state.init_alpha['U'], new_state.init_alpha['V'],
                 new_state.init_alpha['W'],
                 new_state.init_alpha['X'],
                 new_state.init_alpha['Y']].count(player_no) >= 3) and \
                    new_state.init_ley['-6'] == '@':
                new_state.init_ley['-6'] = player_no

            if ([new_state.init_alpha['O'],
                 new_state.init_alpha['U']].count(player_no) >= 1) and \
                    new_state.init_ley['\1'] == '@':
                new_state.init_ley['\1'] = player_no
            if ([new_state.init_alpha['J'], new_state.init_alpha['P'],
                 new_state.init_alpha['V']].count(player_no) >= 2) and \
                    new_state.init_ley['\2'] == '@':
                new_state.init_ley['\2'] = player_no
            if ([new_state.init_alpha['F'], new_state.init_alpha['K'],
                 new_state.init_alpha['Q'],
                 new_state.init_alpha['W']].count(player_no) >= 2) and \
                    new_state.init_ley['\3'] == '@':
                new_state.init_ley['\3'] = player_no
            if ([new_state.init_alpha['C'], new_state.init_alpha['G'],
                 new_state.init_alpha['L'],
                 new_state.init_alpha['R'],
                 new_state.init_alpha['X']].count(player_no) >= 3) and \
                    new_state.init_ley['\4'] == '@':
                new_state.init_ley['\4'] = player_no
            if ([new_state.init_alpha['A'], new_state.init_alpha['D'],
                 new_state.init_alpha['H'],
                 new_state.init_alpha['M'], new_state.init_alpha['S'],
                 new_state.init_alpha['Y']].count(player_no) >= 3) and \
                    new_state.init_ley['\5'] == '@':
                new_state.init_ley['\5'] = player_no
            if ([new_state.init_alpha['B'], new_state.init_alpha['E'],
                 new_state.init_alpha['I'],
                 new_state.init_alpha['N'],
                 new_state.init_alpha['T']].count(player_no) >= 3) and \
                    new_state.init_ley['\5'] == '@':
                new_state.init_ley['\5'] = player_no


        return new_state



    def __repr__(self) -> str:
        """
        Return a representation of this state (which can be used for
        equality testing).
        """
        pass

    def rough_outcome(self) -> float:
        """
        Return an estimate in interval [LOSE, WIN] of best outcome the current
        player can guarantee from state self.
        """
        pass



if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
