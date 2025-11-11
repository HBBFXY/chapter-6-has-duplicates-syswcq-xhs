def has_duplicates(lst):
    # 将列表转换为集合（集合自动去重）
    unique_set = set(lst)
    # 若列表长度大于集合长度，说明存在重复元素
    return len(lst) != len(unique_set)

# 测试程序
if __name__ == "__main__":
    # 测试用例1：存在重复元素
    test_list1 = [1, 2, 3, 4, 2]
    print(f"列表 {test_list1} 是否有重复元素：{has_duplicates(test_list1)}")
    
    # 测试用例2：无重复元素
    test_list2 = [5, 6, 7, 8]
    print(f"列表 {test_list2} 是否有重复元素：{has_duplicates(test_list2)}")
