import typing

def quicksort[T](l: list[T], begin: int = 0, end: typing.Optional[int] = None, compare: typing.Callable[[T, T], bool] = lambda a, b: a < b) -> None:
    if end is None:
        end = len(l) - 1
    
    i = begin
    j = end

    # Pivô, nesse caso um elemento no centro da sub-lista
    pivot = l[(begin + end) // 2]

    while i <= j:
        # Procura um elemento para mover para a direita em relação ao pivô
        while compare(l[i], pivot):
            i = i + 1

        # Procura um elemento para mover para a esquerda em relação ao pivô
        while compare(pivot, l[j]):
            j = j - 1
        
        # Se algum elemento tiver que trocar de lugar
        if i <= j:

            # Realiza troca
            tmp = l[i]
            l[i] = l[j]
            l[j] = tmp

            # Vamos mais ao centro da sub-lista
            i = i + 1
            j = j - 1
    
    if begin < j:
        quicksort(l, begin, j, compare)
    
    if i < end:
        quicksort(l, i, end, compare)
