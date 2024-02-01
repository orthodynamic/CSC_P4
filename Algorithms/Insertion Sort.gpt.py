List = [1,6,5,7,2]
for pointer in range(1, len(List)):
        item_to_be_inserted = List[pointer]
        current_item = pointer - 1

        while current_item >= 0 and List[current_item] > item_to_be_inserted:
            List[current_item + 1] = List[current_item]
            current_item -= 1

        List[current_item + 1] = item_to_be_inserted
print(List)