def solution(triangle):
    triangle = [[0] + line + [0] for line in triangle]
    
    for i in range(1, len(triangle)):
        for j in range(1, i + 2):
            triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])
            
    return max(triangle[-1])

''' �ٸ� Ǯ��
def solution(triangle):
    # ù° ���� index�� 0�̹Ƿ�, ��° �ٺ��� ���
    for rows in range(1, len(triangle)):
        # �� ���� index ������ ���Ѵ�.
        for idx in range(rows + 1):
            # ���� ���� ���� ���
            if idx == 0:
                triangle[rows][idx] += triangle[rows-1][idx]
            # ���� ������ ���� ���
            elif idx == rows:
                triangle[rows][idx] += triangle[rows-1][-1]
            else:
                triangle[rows][idx] += max(triangle[rows-1][idx-1], triangle[rows-1][idx])
    # ���� ������ ���� �ִ��� ���ϸ� �ȴ�.
    return max(triangle[-1])
'''    