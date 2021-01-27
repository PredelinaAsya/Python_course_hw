import typing as tp
import heapq


def merge(seq: tp.Sequence[tp.Sequence[int]]) -> tp.List[int]:
    """
    :param seq: sequence of sorted sequences
    :return: merged sorted list
    """
    k = len(seq)
    heap = []
    ident = 0
    ans = []
    for i in range(k):
        if len(seq[i]) != 0:
            ident += 1
            heapq.heappush(heap, (seq[i][0], ident, (seq[i], 0)))
    while len(heap) != 0:
        index_in_seq = heap[0][2][1]
        ans.append(heap[0][2][0][index_in_seq])
        current_tuple = heapq.heappop(heap)[2]
        current_seq = current_tuple[0]
        if len(current_seq) > index_in_seq + 1:
            ident += 1
            heapq.heappush(heap, (current_seq[index_in_seq + 1],
                                  ident, (current_seq, index_in_seq + 1)))
    return ans
