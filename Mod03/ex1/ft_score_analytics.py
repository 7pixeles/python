#!/usr/bin/env python3
"""
Process player scores from command-line arguments and display basic statistics.

Converts the provided scores to integers and prints total, average,
minimum, maximum, and score range.
"""
import sys

if __name__ == "__main__":
    scores = sys.argv[1:]

    print("=== Player Score Analytics === \n")
    if len(scores) == 0:
        print("No scores provided. "
              "Usage python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        try:
            int_scores = [int(score) for score in scores]
            print("Scores processed:", int_scores)
            print("Total players:", len(int_scores))
            print("Total score:", sum(int_scores))
            print("Average score:", sum(int_scores) / len(int_scores))
            print("High score:", max(int_scores))
            print("Low score:", min(int_scores))
            print("Score range:", max(int_scores) - min(int_scores))

        except ValueError as error:
            print("Error:", error)
