#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    scores = sys.argv[1:]
    int_scores = []

    print("=== Player Score Analytics === \n")
    if len(scores) == 0:
        print("No scores provided. "
              "Usage python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        try:

            # int_scores = [int(score) for score in scores]

            for score in scores:
                int_scores.append(int(score))

            print("Scores processed:", int_scores)
            print("Total players:", len(int_scores))
            print("Total score:", sum(int_scores))
            print("Average score:", sum(int_scores) / len(int_scores))
            print("High score:", max(int_scores))
            print("Low score:", min(int_scores))
            print("Score range:", max(int_scores) - min(int_scores))

        except ValueError as error:
            print("Error:", error)
