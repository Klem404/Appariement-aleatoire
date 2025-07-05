import numpy as np

def hungarian_algorithm(cost_matrix):
    cost_matrix = cost_matrix.copy()
    n = cost_matrix.shape[0]

    for i in range(n):
        cost_matrix[i] -= np.min(cost_matrix[i])

    for j in range(n):
        cost_matrix[:, j] -= np.min(cost_matrix[:, j])

    def find_zero(c_matrix, covered_rows, covered_cols):
        for i in range(n):
            for j in range(n):
                if c_matrix[i, j] == 0 and not covered_rows[i] and not covered_cols[j]:
                    return i, j
        return None

    def cover_zeros():
        assigned = [-1] * n
        covered_rows = [False] * n
        covered_cols = [False] * n

        marked_zeros = []
        for _ in range(n):
            zero = find_zero(cost_matrix, covered_rows, covered_cols)
            if zero is None:
                break
            i, j = zero
            marked_zeros.append((i, j))
            covered_rows[i] = True
            covered_cols[j] = True

        return marked_zeros

    def minimal_number_of_lines():
        from scipy.optimize import linear_sum_assignment  # Fallback
        return linear_sum_assignment(cost_matrix)

    try:
        from scipy.optimize import linear_sum_assignment
        row_ind, col_ind = linear_sum_assignment(cost_matrix)
    except:
        raise NotImplementedError("not completed.")

    return dict(zip(row_ind, col_ind))