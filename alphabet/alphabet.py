import typing as tp
import enum


class Status(enum.Enum):
    NEW = 0
    EXTRACTED = 1
    FINISHED = 2


def extract_alphabet(
        graph: tp.Dict[str, tp.Set[str]]
        ) -> tp.List[str]:
    """
    Extract alphabet from graph
    :param graph: graph with partial order
    :return: alphabet
    """
    used = {}
    for k in graph:
        used[k] = 0
    reverse_sort = []

    def dfs(edge):
        used[edge] = 1
        for new_edge in graph[edge]:
            if used[new_edge] == 0:
                dfs(new_edge)
        used[edge] = 2
        reverse_sort.append(edge)

    for k in graph:
        if used[k] == 0:
            dfs(k)
    reverse_sort.reverse()
    alphabet = reverse_sort
    return alphabet


def build_graph(
        words: tp.List[str]
        ) -> tp.Dict[str, tp.Set[str]]:
    """
    Build graph from ordered words. Graph should contain all letters from words
    :param words: ordered words
    :return: graph
    """
    ans = {}
    n = len(words)
    for i in range(n - 1):
        str1 = []
        str2 = []
        for c in words[i]:
            str1.append(c)
        for c in words[i + 1]:
            if len(str2) >= len(str1):
                break
            str2.append(c)
        for first, second in zip(str1, str2):
            if first != second:
                if ans.get(first) is not None:
                    ans[first].add(second)
                else:
                    ans[first] = set()
                    ans[first].add(second)
                break
    for i in range(n):
        for c in words[i]:
            if ans.get(c) is None:
                ans[c] = set()
    return ans


#########################
# Don't change this code
#########################

def get_alphabet(
        words: tp.List[str]
        ) -> tp.List[str]:
    """
    Extract alphabet from sorted words
    :param words: sorted words
    :return: alphabet
    """
    graph = build_graph(words)
    return extract_alphabet(graph)

#########################
