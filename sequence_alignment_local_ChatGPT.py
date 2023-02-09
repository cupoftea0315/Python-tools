def local_sequence_alignment(seq1, seq2, match_score, mismatch_score, gap_penalty):
    """
    Computes the local sequence alignment of two sequences.
    author: GhatGPT
    :param seq1: First sequence
    :param seq2: Second sequence
    :param match_score: Score for matching characters
    :param mismatch_score: Score for mismatching characters
    :param gap_penalty: Penalty for gap in the sequence
    :return: Tuple of best alignment score and aligned sequences
    """
    rows = len(seq1) + 1
    cols = len(seq2) + 1
    score_matrix = [[0 for j in range(cols)] for i in range(rows)]
    backtrack_matrix = [[0 for j in range(cols)] for i in range(rows)]

    # Fill the score matrix and backtrack matrix
    for i in range(1, rows):
        for j in range(1, cols):
            match = score_matrix[i - 1][j - 1] + (match_score if seq1[i - 1] == seq2[j - 1] else mismatch_score)
            delete = score_matrix[i - 1][j] + gap_penalty
            insert = score_matrix[i][j - 1] + gap_penalty
            scores = [match, delete, insert, 0]
            score_matrix[i][j] = max(scores)
            backtrack_matrix[i][j] = scores.index(score_matrix[i][j])

    # Find the position with the maximum score in the score matrix
    max_i, max_j = 0, 0
    max_score = 0
    for i in range(1, rows):
        for j in range(1, cols):
            if score_matrix[i][j] >= max_score:
                max_i, max_j = i, j
                max_score = score_matrix[i][j]

    # Initialize the aligned sequences
    align1 = ""
    align2 = ""

    # Backtrack from the position with the maximum score
    i, j = max_i, max_j
    while backtrack_matrix[i][j] != 0:
        if backtrack_matrix[i][j] == 1:
            align1 = seq1[i - 1] + align1
            align2 = "-" + align2
            i -= 1
        elif backtrack_matrix[i][j] == 2:
            align1 = "-" + align1
            align2 = seq2[j - 1] + align2
            j -= 1
        else:
            align1 = seq1[i - 1] + align1
            align2 = seq2[j - 1] + align2
            i -= 1
            j -= 1

    return max_score, align1, align2


if __name__ == "__main__":
    seq1 = "ATCGCG"
    seq2 = "TGCCTG"
    match_score = 1
    mismatch_score = -1
    gap_penalty = -1

    best_score, align1, align2 = local_sequence_alignment(seq1, seq2, match_score, mismatch_score, gap_penalty)
    print("Best score:", best_score)
    print("Aligned sequence 1:", align1)
    print("Aligned sequence 2:", align2)

"""
ChatGPT's answer: 
This code will print the best alignment score, and the two aligned sequences. 
Note that seq1 and seq2 can be replaced with any two sequences you want to align. 
The match_score, mismatch_score, and gap_penalty parameters can be adjusted to set the scoring system for the alignment.
"""
