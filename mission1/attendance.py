player_id_list = {}
id_count = 0

# attendance_point_rawdata[사용자ID][요일]
attendance_point_rawdata = [[0] * 100 for _ in range(100)]
total_points = [0] * 100
grade = [0] * 100
names = [''] * 100
wednesday_attendance_count = [0] * 100
weekend_attendance_count = [0] * 100

def process_input_data(input_name, input_day_of_the_week):
    global id_count

    if input_name not in player_id_list:
        add_new_player(input_name)

    curr_player_id = player_id_list[input_name]
    calculate_points(curr_player_id, input_day_of_the_week)


def calculate_points(curr_player_id, input_day_of_the_week):
    add_point = 0
    day_of_the_week_index = 0
    if input_day_of_the_week == "monday":
        day_of_the_week_index = 0
        add_point += 1
    elif input_day_of_the_week == "tuesday":
        day_of_the_week_index = 1
        add_point += 1
    elif input_day_of_the_week == "wednesday":
        day_of_the_week_index = 2
        add_point += 3
        wednesday_attendance_count[curr_player_id] += 1
    elif input_day_of_the_week == "thursday":
        day_of_the_week_index = 3
        add_point += 1
    elif input_day_of_the_week == "friday":
        day_of_the_week_index = 4
        add_point += 1
    elif input_day_of_the_week == "saturday":
        day_of_the_week_index = 5
        add_point += 2
        weekend_attendance_count[curr_player_id] += 1
    elif input_day_of_the_week == "sunday":
        day_of_the_week_index = 6
        add_point += 2
        weekend_attendance_count[curr_player_id] += 1
    attendance_point_rawdata[curr_player_id][day_of_the_week_index] += 1
    total_points[curr_player_id] += add_point


def add_new_player(input_name):
    global id_count
    id_count += 1
    player_id_list[input_name] = id_count
    names[id_count] = input_name


def input_file():
    try:
        with open("attendance_weekday_500.txt", encoding='utf-8') as f:
            for _ in range(500):
                line = f.readline()
                if not line:
                    break
                parts = line.strip().split()
                if len(parts) == 2:
                    process_input_data(parts[0], parts[1])
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")


def add_bonus_point():
    for i in range(1, id_count + 1):
        if attendance_point_rawdata[i][2] > 9:
            total_points[i] += 10
        if attendance_point_rawdata[i][5] + attendance_point_rawdata[i][6] > 9:
            total_points[i] += 10


def update_grade():
    for i in range(1, id_count + 1):
        if total_points[i] >= 50:
            grade[i] = 1
        elif total_points[i] >= 30:
            grade[i] = 2
        else:
            grade[i] = 0


def print_points_and_grade():
    for i in range(1, id_count + 1):
        print(f"NAME : {names[i]}, POINT : {total_points[i]}, GRADE : ", end="")
        if grade[i] == 1:
            print("GOLD")
        elif grade[i] == 2:
            print("SILVER")
        else:
            print("NORMAL")


def print_removed_player():
    print("\nRemoved player")
    print("==============")
    for i in range(1, id_count + 1):
        if grade[i] not in (1, 2) and wednesday_attendance_count[i] == 0 and weekend_attendance_count[i] == 0:
            print(names[i])


if __name__ == "__main__":
    input_file()
    add_bonus_point()
    update_grade()
    print_points_and_grade()
    print_removed_player()
