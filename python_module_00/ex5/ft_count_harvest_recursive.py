def ft_count_harvest_recursive():
    harvest = int(input("Days until harvest: "))
    i = 1

    def ft_helper(harvest, i):
        if (i == harvest + 1):
            return
        else:
            print("Day", i)
            ft_helper(harvest, i + 1)
    ft_helper(harvest, i)
    print("Harvest Day!")
