file = open("input.txt", "r")

input_raw = file.readlines()
input = [x.strip("\n") for x in input_raw]



def partOne(input):
    highest_seatid = 0

    seats = []
    for i in range(128):
        for j in range(8):
            seats.append((i, j))

    seat_ids = []
    
    for boarding_pass in input:
        row = [x for x in range(128)]
        column = [x for x in range(8)]
        row_instructions = boarding_pass[:7]
        column_instructions = boarding_pass[7:]

        for i in row_instructions:
            if i == "F":
                temp_row = row
                row = temp_row[:len(row)//2]
            if i == "B":
                temp_row = row
                row = temp_row[len(row)//2:]
        row_id = row[0]

        for j in column_instructions:
            if j == "R":
                temp_column = column
                column = temp_column[len(column)//2:]
            if j == "L":
                temp_column = column
                column = temp_column[:len(column)//2]
        column_id = column[0]

        seats.remove((row_id, column_id))
        
        seat_id = row_id * 8 + column_id
        if seat_id > highest_seatid:
            highest_seatid = seat_id
        if row_id == 0 or row_id == 127:
            pass
        else:
            seat_ids.append(seat_id)

    for seat in seats:
        if ((seat[0]* 8 + 6) + 1) in seat_ids and ((seat[0]* 8 + 6) - 1) in seat_ids:
            print(seat)

    print(highest_seatid)
    print(seats)

    

partOne(input)