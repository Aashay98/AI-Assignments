import copy

class AdversarialMaze:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
        self.player1_pos = (0, 0)
        self.player2_pos = (grid_size - 1, grid_size - 1)
        self.walls = set()
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def set_wall(self, position):
        self.walls.add(position)

    def move_player(self, player, direction):
        print(direction)
        current_pos = self.player1_pos if player == 1 else self.player2_pos
        new_pos = (current_pos[0] + direction[0], current_pos[1] + direction[1])

        if self.is_valid_move(new_pos):
            if player == 1:
                self.player1_pos = new_pos
            else:
                self.player2_pos = new_pos

    def remove_player(self, position):
        if position == self.player1_pos:
            self.player1_pos = None
        elif position == self.player2_pos:
            self.player2_pos = None

    def is_valid_move(self, position):
        x, y = position
        if 0 <= x < self.grid_size and 0 <= y < self.grid_size and position not in self.walls:
            return True
        return False

    def is_game_over(self):
        return (self.player1_pos is None or self.player2_pos is None) or (self.player1_pos[1] == self.grid_size - 1 or self.player2_pos[1] == 0) or (self.player1_pos[1] == self.grid_size - 1 and self.player2_pos[1] < self.grid_size - 1)

    def print_grid(self):
        for i in range(self.grid_size):
            print('+---' * self.grid_size + '+')
            for j in range(self.grid_size):
                if (i, j) in self.walls:
                    print('| # ', end='')
                elif (i, j) == self.player1_pos:
                    print('| P1', end='')
                elif (i, j) == self.player2_pos:
                    print('| P2', end='')
                else:
                    print('|   ', end='')
            print('|')
        print('+---' * self.grid_size + '+')

    def get_possible_moves(self, player):
        current_pos = self.player1_pos if player == 1 else self.player2_pos
        possible_moves = []

        for direction in self.directions:
            new_pos = (current_pos[0] + direction[0], current_pos[1] + direction[1])
            if self.is_valid_move(new_pos):
                possible_moves.append(direction)
            else:
                # Check if the position is blocked by a wall
                wall_pos = (current_pos[0] + direction[0], current_pos[1] + direction[1])
                if wall_pos in self.walls:
                    # If there's a wall, check if it's possible to move around it
                    for dir_around_wall in self.directions:
                        new_pos_around_wall = (wall_pos[0] + dir_around_wall[0], wall_pos[1] + dir_around_wall[1])
                        if self.is_valid_move(new_pos_around_wall):
                            possible_moves.append(dir_around_wall)
                            break

        return possible_moves
                    
    def minimax(self, depth, maximizing_player):
        if depth == 0 or self.is_game_over():
            if self.player1_pos is None:
                return -10000  # Lower score for player 1's loss
            elif self.player2_pos is None:
                return 1000   # Higher score for player 2's loss
            else:
                return 0

        if maximizing_player:
            print("max")
            max_eval = float('-inf')
            possible_moves = self.get_possible_moves(2)
            for move in possible_moves:
                temp_board = copy.deepcopy(self)
                temp_board.move_player(2, move)
                eval = temp_board.minimax(depth - 1, False)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            possible_moves = self.get_possible_moves(1)
            for move in possible_moves:
                temp_board = copy.deepcopy(self)
                temp_board.move_player(1, move)
                eval = temp_board.minimax(depth - 1, True)
                min_eval = min(min_eval, eval)
                
            return min_eval

    def get_best_move(self, player):
        best_move = None
        max_eval = float('-inf') if player == 1 else float('inf')
        possible_moves = self.get_possible_moves(player)
        for move in possible_moves:
            temp_board = copy.deepcopy(self)
            temp_board.move_player(player, move)
            eval = temp_board.minimax(3, player == 1)
            if (player == 1 and eval >= max_eval) or (player == 2 and eval <= max_eval):
                max_eval = eval
                best_move = move
        return best_move
    
def main():
    grid_size = 10
    game = AdversarialMaze(grid_size)
    game.set_wall((0, 4))
    game.set_wall((1, 1))
    game.set_wall((1, 2))
    game.set_wall((4, 3))
    game.set_wall((3, 3))
    game.set_wall((3, 4))
    game.set_wall((6, 1))
    game.set_wall((7, 1))
    game.set_wall((8, 3))
    game.set_wall((8, 9))
    game.set_wall((8, 8))
    game.set_wall((8, 7))
    game.set_wall((6, 6))
    game.set_wall((5, 6))
    game.set_wall((4, 6))
    game.set_wall((3, 6))
    game.set_wall((3, 7))
    game.set_wall((5, 5))
    game.set_wall((5, 8))
    
    while not game.is_game_over():
        game.print_grid()
        print("Player 1's turn.")       
        player1_move = game.get_best_move(1)
        print("Player 1 moves to:", player1_move)
        game.move_player(1, player1_move)
        if game.is_game_over():
            break
        game.print_grid()
        print("Player 2's turn.")
        player2_move = game.get_best_move(2)
        print("Player 2 moves to:", player2_move)
        game.move_player(2, player2_move)
    game.print_grid()
    if game.player1_pos is None:
        print("Player 1 captured! Player 2 wins!")
    elif game.player2_pos is None:
        print("Player 2 captured! Player 1 wins!")
    elif game.player1_pos[1] == grid_size - 1:
        print("Player 1 wins!")
    elif game.player2_pos[1] == 0:
        print("Player 2 wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()

 
