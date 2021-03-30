
def set_board(render_pieces = [],targets = []):
    row = []
    if(len(render_pieces) == 0 and len(targets) == 0):
        for i in range(0,8):
            col = []
            for j in range(0,8):
                col.append(select_pixcel(i,j,render_pieces,targets))
            row.append(col)
    elif(len(render_pieces) != 0 and len(targets) == 0):
        for i in range(0,8):
            col = []
            for j in range(0,8):
                col.append(select_pixcel(i,j,render_pieces,targets))
            row.append(col)
    elif(len(render_pieces) != 0 and len(targets) != 0):
        for i in range(0,8):
            col = []
            for j in range(0,8):
                col.append(select_pixcel(i,j,render_pieces,targets))
            row.append(col)
    else:
        print("Invalid State")
        return None
    return row

def count_occurances(item,list):
    count = 0
    for i in list:
        if(item == i):
            count+=1
    return count

def select_pixcel(i,j,render_pieces,targets):
    if(count_occurances([i,j],render_pieces) > 1):
        raise Exception("Invalid piece position")
    
    if(count_occurances([i,j],targets) > 1):
        raise Exception("Invalid targer position")

    pixcel = " * "
    if([j,i] in render_pieces):
        pixcel= " @ "
    if([j,i] in targets):
        pixcel= " $ "
    return pixcel


def print_board(name,rows):
    print(name)
    for item in rows:
        for point in item:
            print(point,end="")
        print("\n")

def render_piece(start_x,start_y,end_x,end_y,len):
    block = []
    if(start_y == end_y):
        if(start_x < end_x):
            x_row = [x for x in range(start_x,end_x + 1)]
        else:
            x_row = [x for x in range(end_x,start_x + 1)]
        for item in x_row:
            block.append([item,start_y])
    elif(start_x == end_x):
        if(start_y < end_y):
            y_row = [x for x in range(start_y,end_y + 1)]
        else:
            y_row = [x for x in range(end_y,start_y + 1)]
        for item in y_row:
            block.append([start_x,item])
    
    return block
        

def validate_coordinates(start_x,start_y,end_x,end_y,len):
    if(start_y == end_y):
        if(abs(start_x - end_x) == len - 1 and (start_x >=0 or end_x <= 7 or start_x <=7 or end_x >= 0)):
            return True
        else:
            return False
    elif(start_x == end_x):
        if(abs(start_y - end_y) == len - 1 and (start_y >=0 or end_y <= 7 or start_y <=7 or end_y >= 0)):
            return True
        else:
            return False
    else:
        return False
        

def init_pieces(piece_arr):
    pieces = [2,3,4]
    ren_box = []
    for i in range(3):
        start_x = piece_arr[i][0]
        start_y = piece_arr[i][1]
        end_x = piece_arr[i][2]
        end_y = piece_arr[i][3]
        if(validate_coordinates(start_x,start_y,end_x,end_y,pieces[i])):
            temp = render_piece(start_x,start_y,end_x,end_y,pieces[i])
            for item in temp:
                ren_box.append(item)
        else:
            print("Invalid config")
            return None
    return ren_box




if __name__ == "__main__":
    row_player_1 = set_board()
    row_player_2 = set_board()
    print_board("Player 1",row_player_1)
    print_board("Player 2",row_player_2)
    player_1_pieces = init_pieces([[7,7,6,7],[3,3,3,5],[5,2,2,2]])
    player_2_pieces = init_pieces([[7,7,6,7],[3,3,3,5],[5,2,2,2]])
    row_player_1 = set_board(player_1_pieces)
    row_player_2 = set_board(player_2_pieces)
    print_board("Player 1",row_player_1)
    print_board("Player 2",row_player_2)
    print("&&&&&&&&&&&& Game Start &&&&&&&&&&&&")
    condtion = True
    player_1_target = []
    player_2_target = []
    while(condtion):
        print("Enter player 1 target")
        player_1_target.append(list(map(int,input().split(","))))
        print("Enter player 2 target")
        player_2_target.append(list(map(int,input().split(","))))
        row_player_1 = set_board(player_1_pieces,player_1_target)
        row_player_2 = set_board(player_2_pieces,player_2_target)

        print_board("Player 1",row_player_1)
        print_board("Player 2",row_player_2)
        if(player_2_pieces in player_1_target):
            print("Player 1 wins")
            condtion = False
            break
        
        if(player_1_pieces in player_2_target):
            print("Player 2 wins")
            condtion = False
            break



