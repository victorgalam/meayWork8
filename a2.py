def phone_num():
    counter = 0
    is_valid_phone = False
    while not is_valid_phone:
        str_phone = input("enter phone number: ")
        counter += 1
        if len(str_phone) != 11:
            continue
        good_nums = ["050", "051", "052", "053", "054", "055", "056", "057", "058", "059"]
        is_valid_phone = True
        if not str_phone[0:3] in good_nums:
            is_valid_phone = False
        if not str_phone[3] == "-":
            is_valid_phone = False
        for i in range(4, len(str_phone)):
            if not str_phone[i].isdigit():
                is_valid_phone = False
    print("Count input:", counter)

phone_num()


# if str_phone[i] in ['0', '1', '2', '3', ....]
