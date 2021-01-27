import typing as tp
import heapq


def merge(input_streams: tp.Sequence[tp.IO[bytes]],
          output_stream: tp.IO[bytes]) -> None:
    """
    Merge input_streams in output_stream
    :param input_streams: list of input streams. Contains byte-strings
    separated by "\n". Nonempty stream ends with "\n"
    :param output_stream: output stream. Contains byte-strings separated
    by "\n". Nonempty stream ends with "\n"
    :return: None
    """
    fl = False
    heap = []
    ident = 0
    for line in input_streams:
        if line != b'':
            arr_bytes = line.getvalue().split(b'\n')
            arr_digits = [int(s.decode("utf-8"))
                          for s in arr_bytes if s != b'']
            if len(arr_digits):
                heapq.heappush(heap, (arr_digits[0], ident, (arr_digits, 0)))
                ident += 1
    while len(heap) != 0:
        cur_val = heap[0]
        heapq.heappop(heap)
        output_stream.write(str(cur_val[0]).encode("utf-8") + b'\n')
        fl = True
        cur_index = cur_val[2][1]
        cur_arr = cur_val[2][0]
        if cur_index + 1 < len(cur_arr):
            new_index = cur_index + 1
            heapq.heappush(heap, (cur_arr[new_index], ident,
                                  (cur_arr, new_index)))
            ident += 1
    if not fl:
        output_stream.write(b'\n')
    return
