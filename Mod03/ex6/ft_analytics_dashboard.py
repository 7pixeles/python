#!/usr/bin/env python3

def show_dashboard() -> None:
    """Display player statistics and examples of
    list, dict, and set comprehensions."""
    data_game = [
        {"name": "alice",
         "score": 2300, "region": "north", "status": "active"},
        {"name": "bob",
         "score": 1800, "region": "west", "status": "active"},
        {"name": "charlie",
         "score": 4900, "region": "east", "status": "active"},
        {"name": "diana",
         "score": 800, "region": "south", "status": "inactive"},
        {"name": "eve",
         "score": 2300, "region": "central", "status": "inactive"}
    ]

    game_achievements = {
        "alice": {'level_10', 'treasure_hunter', 'speed_demon', 'boss_slayer'},
        "bob": {'first_kill', 'level_10', 'boss_slayer', 'collector'},
        "charlie": {'level_10', 'treasure_hunter', 'perfectionist'},
        "diana": {'speed_demon', 'perfectionist', 'level_10', 'first_kill'},
        "eve": {'first_kill', 'level_10'},
    }

    print("=== Game Analytics Dashboard===")

    # LIST COMPREHENSION
    print("\n=== List Comprehension Examples ===")

    # Filter players with high scores (> 2000)
    top_scores = [
        player['name'] for player in data_game
        if player['score'] > 2000]
    print("High scores (>2000):", top_scores)

    # Transform scores by doubling each value
    double_score = [player['score'] * 2 for player in data_game]
    print("Scores doubled:", double_score)

    # Filter only players that are currently active
    active_players = [
        player['name'] for player in data_game
        if player['status'] == "active"]
    print("Active players:", active_players)

    # DICT COMPREHENSION
    print("\n=== Dict Comprehension Examples ===")

    # Map each player name to their score
    player_scores = {
        player['name']: player['score']
        for player in data_game
        if player['status'] == "active"}
    print("Player scores:", player_scores)

    # Define categories for each score
    score_category = {
        'high': len([player for player in data_game
                    if player['score'] > 2000]),
        'medium': len([player for player in data_game
                       if 1000 <= player['score'] < 2000]),
        'low': len([player for player in data_game
                    if player['score'] < 1000])
    }
    print("Score categories:", score_category)

    # Count avhievements for each player
    count_achievements = {
        player: len(game_achievements[player])
        for player in game_achievements
        }
    print("Achievement counts:", count_achievements)

    # SET COMPREHENSION
    print("\n=== Set Comprehension Examples ===")

    # Extract unique players names
    unique_players = {player['name'] for player in data_game}
    print("Unique players:", unique_players)

    # Collect all unique achievements
    unique_ach = {
        ach
        for player in game_achievements
        for ach in game_achievements[player]
    }
    print("Unique achievements:", unique_ach)

    # Show regions of active players
    active_regions = {
        player['region']
        for player in data_game
        if player['status'] == "active"}
    print("Active regions:", active_regions)

    print("\n=== Combined Analysis ===")

    total_player = len(data_game)
    print("Total Players:", total_player)

    total_uniq_achieve = len(
        [
            ach
            for player in game_achievements
            for ach in game_achievements[player]
        ])
    print("Total unique achievements:", total_uniq_achieve)
    average = sum(player['score'] for player in data_game) / total_player
    print("Average score:", average)
    max_score = max(player['score'] for player in data_game)
    max_player = [
        player for player in data_game
        if player['score'] == max_score][0]
    max_achievements = len(game_achievements[max_player['name']])
    print(f"Top performer: {max_player['name']}", end=" ")
    print(f"{max_score} points, {max_achievements} achievements)")


if __name__ == "__main__":
    show_dashboard()
