from abc import ABC, abstractmethod
import datetime


class Competition(ABC):
    @abstractmethod
    def display(self, name, date, location):
        pass

    @abstractmethod
    def distance(self):
        pass


class Normal(Competition, ABC):
    def display(self, name, date, location):
        print(f'{name} diễn ra vào {date} tại {location}')

    def distance(self):
        print("Cự ly 42km \nCự ly 21km \nCự ly 10km \nCự ly 5km")


class NonCompetitive(Competition, ABC):
    def display(self, name, date, location):
        print(f'{name} diễn ra vào {date} tại {location}')

    def distance(self):
        print("Cự ly 10km \nCự ly 5km")


class Trail(Competition, ABC):
    def display(self, name, date, location):
        print(f'{name} diễn ra vào {date} tại {location}')

    def distance(self):
        print("Cự ly 50km \nCự ly 80km \nCự ly 100km")


competitions = {}
list_comp = []
names = []


def get_user_input():
    while more_input():
        print()
        n = input("Tên cuộc thi: ")
        d = input("Ngày tổ chức (Ví dụ: 25 08 2020): ")
        l = input("Địa điểm tổ chức: ")
        c = input("Giải chạy thông thường - 1 / Giải chạy bộ từ thiện - 2 / Giải trail - 3: ")
        classify(c)
        competitions[n] = [n, d, l, c]
        names.append(n)


def more_input():
    m = input("Bạn có muốn nhập thêm cuộc thi không? (y/n) ")
    if m == "y":
        return True
    else:
        return False


def display_all_competitions(n):
    print("\nDANH SÁCH CÁC GIẢI CHẠY BỘ TRONG NĂM 2020:")
    j = 0
    for i in list_comp:
        i.display(competitions[n[j]][0], competitions[n[j]][1], competitions[n[j]][2])
        j += 1


def classify(c):
    if c == "1":
        list_comp.append(Normal())
    elif c == "2":
        list_comp.append(NonCompetitive())
    else:
        list_comp.append(Trail())


participate = {}


def signup():
    sum = 0
    if len(list_comp) < 3:
        print("Danh sách không đủ 3 cuộc thi!")
    else:
        pace = float(input("\nNhập pace trung bình: "))
        print("\nChọn trong danh sách trên 3 cuộc thi.")
        for i in range(3):
            comp = input("\nNhập tên cuộc thi muốn đăng ký: ")
            print("Giải chạy này gồm các cự ly sau:")
            if competitions[comp][3] == "1":
                a = Normal()
                a.distance()
            elif competitions[comp][3] == "2":
                a = NonCompetitive()
                a.distance()
            else:
                a = Trail()
                a.distance()
            dis = int(input("Nhập cự ly muốn đăng ký cho cuộc thi này: "))
            sum += dis * pace
            participate[comp] = competitions[comp][1]
        print("Tổng thời gian (tính bằng giờ) hoàn thành tất cả các cự ly đã đăng ký trong 3 cuộc thi trên:", sum / 60)


can = []


def find_day():
    day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for i in participate:
        date = participate[i]
        day = datetime.datetime.strptime(date, '%d %m %Y').weekday()
        if day_name[day] == "Sunday":
            can.append(i)
        else:
            continue
    print("\nCác giải chạy có thể tham gia được:", can)


get_user_input()
display_all_competitions(names)
signup()
find_day()
