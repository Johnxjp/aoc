import re


def read_lines():
    lines = []
    with open("2023/d2.txt") as f:
        for line in f:
            lines.append(line.strip())

    return lines


def parse_game(unparsed_game):
    """
    Returns a tuple with game ID, the number of sets and the number of each colour
    ball in each set in the order (red, blue, green).

    An unparsed game is a string of the form:
    "Game ID: set 1; set 2; set 3; ..."
    where each set is of the form:
    "3 blue, 1 red, 1 green" for example
    """

    sets = []
    n_blue, n_red, n_green = 0, 0, 0
    game_id = int(re.match(r"Game (\d+):", unparsed_game).group(1))
    sets_str = unparsed_game.split(":")[1].split(";")
    for set_str in sets_str:
        match_r = re.search(r"(\d+) red", set_str)
        match_b = re.search(r"(\d+) blue", set_str)
        match_g = re.search(r"(\d+) green", set_str)

        if match_r:
            n_red = int(match_r.group(1))

        if match_g:
            n_green = int(match_g.group(1))

        if match_b:
            n_blue = int(match_b.group(1))

        sets.append([n_red, n_blue, n_green])

    return game_id, sets


def is_valid_game(game_sets, constraint_red, constraint_blue, constraint_green):
    for n_red, n_blue, n_green in game_sets:
        if (
            n_red > constraint_red
            or n_blue > constraint_blue
            or n_green > constraint_green
        ):
            return False

    return True


def p1():
    games = read_lines()
    sum_valid_game_ids = 0
    for game in games:
        game_id, sets = parse_game(game)
        if is_valid_game(sets, 12, 14, 13):
            sum_valid_game_ids += game_id

    print(sum_valid_game_ids)


if __name__ == "__main__":
    p1()
