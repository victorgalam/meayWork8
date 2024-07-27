def is_ordered_list(lst):
    start_with_even = False
    if lst[0] % 2 == 0:
        start_with_even = True
    if start_with_even:
        for num in lst:
            if num % 2 != 0:
                now_only_odd = True
