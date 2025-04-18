def blakcjackSolver(dealer, player):
    """
    H   = Hit
    S   = Stand
    D   = Double if allowed, otherwise Hit
    DS  = Double if allowed, otherwise Stand
    N   = Don't split the pair
    Y   = Split the pair
    Y/N = Split only if 'DAS' is offered (Double After Split)
    SUR = Surrender
    """
    action = ""

    dealer_sum = 0
    player_sum = 0
    is_dealer_soft = False
    is_player_soft = False

    is_count = False
    for i in dealer:
        if i in ["J", "Q", "K"]:
            dealer_sum = dealer_sum + 10
        elif i == "A":
            if not is_count and dealer_sum + 11 <= 21:
                dealer_sum = dealer_sum + 11
                is_count = True
                is_dealer_soft = True
            else:
                dealer_sum = dealer_sum + 1
                is_dealer_soft = False
        elif i in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            dealer_sum = dealer_sum + int(i)

    for i in dealer:
        if i == "A":
            if not is_count and dealer_sum + 11 <= 21:
                dealer_sum = dealer_sum + 11
                is_count = True
                is_dealer_soft = True
            else:
                dealer_sum = dealer_sum + 1
                is_dealer_soft = False

    is_count = False
    for i in player:
        if i in ["J", "Q", "K"]:
            player_sum = player_sum + 10
        elif i in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            player_sum = player_sum + int(i)

    for i in player:
        if i == "A":
            if not is_count and player_sum + 11 <= 21:
                player_sum = player_sum + 11
                is_count = True
                is_player_soft = True
            else:
                player_sum = player_sum + 1
                is_player_soft = False

    print(dealer_sum, is_dealer_soft, player_sum, is_player_soft)

    hard = [
        # 2   3   4   5   6   7   8   9  10   A
        ["H", "H", "H", "H", "H", "H", "H", "H", "H", "H"],  # 8
        ["H", "D", "D", "D", "D", "H", "H", "H", "H", "H"],  # 9
        ["D", "D", "D", "D", "D", "D", "D", "D", "H", "H"],  # 10
        ["D", "D", "D", "D", "D", "D", "D", "D", "D", "D"],  # 11
        ["H", "H", "S", "S", "S", "H", "H", "H", "H", "H"],  # 12
        ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H"],  # 13
        ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H"],  # 14
        ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H"],  # 15
        ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H"],  # 16
        ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],  # 17
    ]

    soft = [
        # 2   3   4   5   6   7   8   9  10   A
        ["H", "H", "H", "D", "D", "H", "H", "H", "H", "H"],  # A,2
        ["H", "H", "H", "D", "D", "H", "H", "H", "H", "H"],  # A,3
        ["H", "H", "D", "D", "D", "H", "H", "H", "H", "H"],  # A,4
        ["H", "H", "D", "D", "D", "H", "H", "H", "H", "H"],  # A,5
        ["H", "D", "D", "D", "D", "H", "H", "H", "H", "H"],  # A,6
        ["DS", "DS", "DS", "DS", "DS", "S", "S", "H", "H", "H"],  # A,7
        ["S", "S", "S", "S", "DS", "S", "S", "S", "S", "S"],  # A,8
        ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],  # A,9
    ]

    pair = [
        # 2   3   4   5   6   7   8   9  10   A
        ["Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y"],  # A,A
        ["Y/N", "Y/N", "Y", "Y", "Y", "Y", "N", "N", "N", "N"],  # 2,2
        ["Y/N", "Y/N", "Y", "Y", "Y", "Y", "N", "N", "N", "N"],  # 3,3
        ["N", "N", "N", "Y/N", "Y/N", "N", "N", "N", "N", "N"],  # 4,4
        ["N", "N", "N", "N", "N", "N", "N", "N", "N", "N"],  # 5,5
        ["Y", "Y", "Y", "Y", "Y", "N", "N", "N", "N", "N"],  # 6,6
        ["Y", "Y", "Y", "Y", "Y", "Y", "N", "N", "N", "N"],  # 7,7
        ["Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y"],  # 8,8
        ["Y", "Y", "Y", "Y", "Y", "Y", "N", "Y", "N", "N"],  # 9,9
        ["N", "N", "N", "N", "N", "N", "N", "N", "N", "N"],  # T,T
    ]

    # if can surrend, surrend
    surrend = [
        # 2   3   4   5   6   7   8    9     10    A
        [" ", " ", " ", " ", " ", " ", " ", " ", "SUR", ""],  # 15
        [" ", " ", " ", " ", " ", " ", " ", "SUR", "SUR", "SUR"],  # 16
    ]

    if player[0] == player[1]:
        # pair
        row = player_sum // 2 - 1
        if player[0] == "A":
            row = 0
        if dealer[0] == "A":
            col = 9
        else:
            col = dealer_sum - 2
        action = hard[row][col]
        if action == "N":
            if player_sum < 8:
                action = "H"
            elif player_sum < 18:
                row = player_sum - 8
                action = hard[row][dealer_sum - 2]
            else:
                action = "S"

    elif is_player_soft:
        row = player_sum - 13
        if dealer[0] == "A":
            col = 9
        else:
            col = dealer_sum - 2
        action = hard[row][col]
    else:
        if player_sum < 8:
            action = "H"
        elif player_sum < 18:
            row = player_sum - 8
            if dealer[0] == "A":
                col = 9
            else:
                col = dealer_sum - 2
            action = hard[row][col]
        else:
            action = "S"

    return action


# print(blakcjackSolver(['K', '?'],['5', 'A', 'J']))
