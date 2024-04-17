def common_elements(num_list1, num_list2):
    # Tạo một set từ num_list1 để tối ưu việc kiểm tra sự tồn tại của các phần tử
    set_num_list1 = set(num_list1)

    # Khởi tạo một danh sách để lưu trữ các số chung
    common = []

    # Duyệt qua từng phần tử trong num_list2
    for num in num_list2:
        # Kiểm tra xem phần tử có tồn tại trong set_num_list1 không
        if num in set_num_list1:
            # Nếu có, thêm phần tử vào danh sách common
            common.append(num)

    return common

# Ví dụ:
num_list1 = [4,9,5]
num_list2 = [9,4,9,8,4]
print(common_elements(num_list1, num_list2))  
