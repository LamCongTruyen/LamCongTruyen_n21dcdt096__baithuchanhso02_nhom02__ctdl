def max_sliding_window(num_list, k):
    if not num_list or k <= 0:#ktra xem biến num_list có rỗng hay số k nhập vào có sai
        #so với yêu cầu hay không
        print("vui long nhap lai!")

    n = len(num_list)
    if k >= n: #nếu k nhập vào lớn hơnkích thước của biến num_list thì trả về giá trị lớn nhất của
        #biến num_list
        return [max(num_list)]

    result = [] #tạo một ds rỗng để lưu kết quả
    window = [] #tạo một danh sách rỗng để đại diện cho cửa sổ trượt

    for i in range(n):#vòng lặp i chạy qua từng ptu trong ds num_list
        # Xóa các phần tử khỏi cửa sổ trượt đã vượt qua
        if window and window[0] <= i - k:# nếu ds rỗng hoặc vượt qua phạm vi của cửa sổ trượt
            window.pop(0)#loại bỏ ptu đấy

        # Xóa các phần tử nhỏ hơn phần tử mới thêm vào từ phải
        while window and num_list[window[-1]] <= num_list[i]:#nếu ds rỗng hoặc ptu ở cuối nhỏ hơn hoặc
            #bằng với phần tử hiện tại
            window.pop()#thì loại bỏ ptu cuối cùng khỏi ds

        window.append(i) #thêm phtu hiện tại nếu lớn hơn biến k vào window

        # Khi đủ kích thước của cửa sổ, thêm số lớn nhất vào kết quả
        if i >= k - 1: #nếu biến i chạy đến k 
            result.append(num_list[window[0]])#thêm số lớn nhất trong window vào biến lưu réult

    return result

# Ví dụ:
num_list = [3,4,5,1,-44,5,10,12,33,1]
k = 3 #k>=1
print(max_sliding_window(num_list, k)) 
