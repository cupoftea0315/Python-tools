import numpy as np


def global_sequence_alignment(seq1, seq2, match_score, mismatch_score, gap_penalty):
    """
    Global sequence alignment algorithm for two sequences.
    author: GhatGPT
    :param seq1: First sequence
    :param seq2: Second sequence
    :param match_score: Score for a match
    :param mismatch_score: Score for a mismatch
    :param gap_penalty: Penalty for inserting a gap
    :return: The best alignment score and the aligned sequences
    """
    m, n = len(seq1), len(seq2)
    # Initialize the dynamic programming matrix
    dp = np.zeros((m + 1, n + 1))
    # Fill in the dynamic programming matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Calculate the scores for matching, mismatching, and inserting a gap
            match = dp[i - 1][j - 1] + match_score if seq1[i - 1] == seq2[j - 1] else dp[i - 1][j - 1] + mismatch_score
            delete = dp[i - 1][j] + gap_penalty
            insert = dp[i][j - 1] + gap_penalty
            # Choose the maximum score
            dp[i][j] = max(match, delete, insert)
    # Trace back the best alignment
    align1, align2 = "", ""
    i, j = m, n
    while i > 0 and j > 0:
        current_score = dp[i][j]
        diagonal_score = dp[i - 1][j - 1]
        up_score = dp[i][j - 1]
        left_score = dp[i - 1][j]
        # Check which direction the maximum score came from
        if current_score == diagonal_score + match_score and seq1[i - 1] == seq2[j - 1]:
            align1 += seq1[i - 1]
            align2 += seq2[j - 1]
            i -= 1
            j -= 1
        elif current_score == diagonal_score + mismatch_score:
            align1 += seq1[i - 1]
            align2 += seq2[j - 1]
            i -= 1
            j -= 1
        elif current_score == left_score + gap_penalty:
            align1 += seq1[i - 1]
            align2 += "-"
            i -= 1
        elif current_score == up_score + gap_penalty:
            align1 += "-"
            align2 += seq2[j - 1]
            j -= 1
    # Add remaining sequence to the alignment
    while i > 0:
        align1 += seq1[i - 1]
        align2 += "-"
        i -= 1
    while j > 0:
        align1 += "-"
        align2 += seq2[j - 1]
        j -= 1
    # Reverse the aligned sequences
    align1 = align1[::-1]
    align2 = align2[::-1]
    return dp[m][n], align1, align2


if __name__ == "__main__":
    seq1 = "ATCGCGGCCCGGGGATTCTAACGAGCACTGTGCGCATGTAGCTTATGCGGCGAGAACGACGAAGTTGGCAGCCGCGGACAGGACTAAGCATACCAGTGCA"
    seq2 = "TGCCTGCATAGGGAAGTGATGGTTCCCTTCTCAGAGGGAACCAATTTTGTCAAGAGAAGTAAGAACGCGCACGTTCCTACGAGGAGAGCGCAAATAGAGG"
    match_score = 2
    mismatch_score = -1
    gap_penalty = -1

    best_score, align1, align2 = global_sequence_alignment(seq1, seq2, match_score, mismatch_score, gap_penalty)
    print("Best score:", best_score)
    print("Aligned sequence 1:", align1)
    print("Aligned sequence 2:", align2)

"""
ChatGPT's answer: 
This code defines the sequence_alignment function, which takes two sequences, match score, mismatch score, and gap penalty as input, and returns the best alignment score and the aligned sequences. 
In the if __name__ == "__main__" block, it defines two sample sequences, match score, mismatch score, and gap penalty, and calls the sequence_alignment function. 
Finally, it prints the best alignment score and the aligned sequences.
"""
