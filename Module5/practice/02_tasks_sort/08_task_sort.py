def sort_choice(nums: list) -> None:
    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            if nums[j] < nums[m]:
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1


phones = ["25-17-58", "11-34-85", "54-61-56",
          "34-61-72", "25-17-55", "34-56-56"]
# дефолтная сортировка выбором рабоатет корректно
sort_choice(phones)
print(phones)
