a_arr = list(map(int,input().split()))
c_arr = list(map(int,input().split()))
b_x = (c_arr[0]) - (a_arr[2])
b_y = int((c_arr[1])/(a_arr[1]))
b_z = (c_arr[2]) -(a_arr[0])
print(b_x,b_y,b_z)