class Stack: #tạo thư viện ngăn xếp
    def __init__(self, max_size):#hàm khởi tạo của ngăn xếp
        self.max_size = max_size #tạo giá trị lưu trữ của ngăn xếp
        self.stack = [] #Tạo một list rỗng để lưu trữ
        self.top = -1#khi stack rỗng biến top được đặt về -1


    def is_empty_stack(self):#hàm kiểm tra xem ngăn xếp rỗng hay không
        return self.top == -1 #nếu rỗng trả về true còn không thì trả về false

    def is_full_stack(self): #hàm kiểm tra ngăn xếp đã đầy hay chưa
        return self.top == self.max_size - 1#nếu có thì trả về true ngc lại trả về fale
#ví dụ ngăn xếp có 4096 ptu lưu thì gái trị max_size sẽ là 4095 vì 0-4095 có 4096 gtri
    def push_stack(self, item): #hàm để thêm một giá trị vào ngăn xếp
        if self.is_full_stack():#nếu ngăn xếp đã đầy không thể thêm thì in ra thông báo
            print("Stack overflow, unable to push item onto stack")
        else:#ngược lại
            self.stack.append(item)#thêm 1 phần tử vào vị trí trên cùng của ngăn xếp
            self.top += 1 #tăng giá trị của top lên, top như là 1 biến đếm

    def pop_stack(self):#hàm lấy ra 1 phần tử
        if self.is_empty_stack():#nếu ngăn xếp rỗng thì in ra thông báo
            print("Stack underflow, unable to pop item from stack")
            return None
        else:
            item = self.stack.pop()#ptu lấy bằng cách sử dụng hàm pop()
            self.top -= 1#và giảm biến top đi 1
            return item

    def get_top_stack(self):#hàm lấy ra 1 ptu nhưng không xóa đi nó
        if self.is_empty_stack():
            print("Stack is empty")#ktra và in ra thông báo
            return None
        else:
            return self.stack[self.top]#Phương thức này không làm thay đổi cấu trúc của stack,
            #chỉ trả về giá trị của phần tử trên cùng mà không xóa nó khỏi stack


# Example usage:
stack = Stack(3)  # Tạo một stack với kích thước tối đa là 5
stack.push_stack(1)
stack.push_stack(2)
stack.push_stack(3)
print("get_top_stack se lay ra phan tư :", stack.get_top_stack())  # Hiển thị phần tử đầu tiên của stack
print("pop_stack se lay ra phan tu :", stack.pop_stack())  # Lấy phần tử đầu ra khỏi stack
print("lenh get_top_stack duoc thuc hien lai sau lenh pop_stack se cho ra phan tu:", stack.get_top_stack())  # Hiển thị phần tử đầu tiên của stack sau khi pop
