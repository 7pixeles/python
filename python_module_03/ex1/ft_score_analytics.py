#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    scores = sys.argv[1:]
    valid_scores = []

    print("=== Player Score Analytics ===")

    if len(scores) == 0:
        print("No scores provided.", end=" ")
        print("Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        i = 0
        while i < len(scores):
            try:
                num = int(scores[i])
                valid_scores.append(num)
            except ValueError:
                print(f"Invalid parameter: '{scores[i]}'")
            i += 1

        if len(valid_scores) == 0:
            print("No scores provided.", end=" ")
            print("Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        else:
            total = sum(valid_scores)
            print("Scores processed:", valid_scores)
            print("Total players:", len(valid_scores))
            print("Total score:", total)
            print("Average score:", total / len(valid_scores))
            print("High score:", max(valid_scores))
            print("Low score:", min(valid_scores))
            print("Score range:", max(valid_scores) - min(valid_scores))
