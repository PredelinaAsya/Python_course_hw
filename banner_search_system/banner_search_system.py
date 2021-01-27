import typing as tp

import heapq
import string

from collections import defaultdict


def normalize(
        text: str
        ) -> str:
    """
    Removes punctuation and digits and convert to lower case
    :param text: text to normalize
    :return: normalized query
    """
    text_without_punc = text.translate(text.maketrans("", "",
                                                      string.punctuation))
    text_without_digits = \
        text_without_punc.translate(text_without_punc.maketrans("", "",
                                                                "1234567890"))
    ans = text_without_digits.lower()
    return ans


def get_words(
        query: str
        ) -> tp.List[str]:
    """
    Split by words and leave only words with letters greater than 3
    :param query: query to split
    :return: filtered and split query by words
    """
    ans = [words for words in query.split() if len(words) > 3]
    return ans


def build_index(
        banners: tp.List[str]
        ) -> tp.Dict[str, tp.List[int]]:
    """
    Create index from words to banners ids with preserving order and without
    repetitions
    :param banners: list of banners for indexation
    :return: mapping from word to banners ids
    """
    ans = {}
    current_index = 0
    for s in banners:
        for word in get_words(normalize(s)):
            if ans.get(word) is None:
                ans[word] = []
            length = len(ans[word])
            if length == 0 or (length != 0 and
                               ans[word][length - 1] != current_index):
                ans[word].append(current_index)
        current_index += 1
    return ans


def get_banner_indices_by_query(
        query: str,
        index: tp.Dict[str, tp.List[int]]
        ) -> tp.List[int]:
    """
    Extract banners indices from index, if all words from query contains in
    indexed banner
    :param query: query to find banners
    :param index: index to search banners
    :return: list of indices of suitable banners
    """
    ans = []
    heap = []
    list_of_words = get_words(normalize(query))
    ident = 0
    for word in list_of_words:
        if index.get(word) is not None:
            heapq.heappush(heap, (index[word][0], ident, (index[word], 0)))
            ident += 1
    current_amount = 0
    current_val = -1
    while len(heap) != 0:
        current_edge = heap[0]
        elem_in_cur_edge = current_edge[0]
        arr_in_cur_edge = current_edge[2][0]
        index_in_cur_edge = current_edge[2][1]
        if current_val == -1:
            current_val = elem_in_cur_edge
        if current_val == elem_in_cur_edge:
            current_amount += 1
        else:
            current_amount = 1
            current_val = elem_in_cur_edge
        if current_amount == len(list_of_words):
            ans.append(current_val)
        heapq.heappop(heap)
        if (len(arr_in_cur_edge) > index_in_cur_edge + 1):
            heapq.heappush(heap, (arr_in_cur_edge[index_in_cur_edge + 1],
                                  ident,
                                  (arr_in_cur_edge, index_in_cur_edge + 1)))
            ident += 1
    return ans


#########################
# Don't change this code
#########################

def get_banners(
        query: str,
        index: tp.Dict[str, tp.List[int]],
        banners: tp.List[str]
        ) -> tp.List[str]:
    """
    Extract banners matched to queries
    :param query: query to match
    :param index: word-banner_ids index
    :param banners: list of banners
    :return: list of matched banners
    """
    indices = get_banner_indices_by_query(query, index)
    return [banners[i] for i in indices]

#########################
