#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    scores = sys.argv[1:]
    int_scores = []

    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1:
        print("No scores provided. "
              "Usage python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        try:
            for score in scores:
                n_score = int(score)
                int_scores.append(n_score)
            print("Scores processed:", int_scores)
            print("Total players:", len(int_scores))
            print("Total score:", sum(int_scores))
            print("Average score:", sum(int_scores) / len(int_scores))
            print("High score:", max(int_scores))
            print("Low score:", min(int_scores))
            print("Score range:", max(int_scores) - min(int_scores))
        except ValueError as error:
            print("Error:", error)
