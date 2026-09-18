def chessboard(x):
    row_count = 1
    while row_count <= x:
        col_index = 0
        string = "" # string should be reset every time
        while col_index < x:
            if row_count % 2 == 0: # if row_count is even, starts with 0
                if col_index % 2 == 0: # if index is even, 0 is added next
                    string += "0"
                else: # if index os odd, 0 is added next
                    string += "1"
            else: # if row_count is odd, starts with 1
                if col_index % 2 == 0: # if index is even,starts with 1
                    string += "1"
                else: # if index is odd, starts with 0
                    string += "0"
            col_index += 1
        row_count += 1
        print(string)
if __name__ == "__main__":
    chessboard(4)
