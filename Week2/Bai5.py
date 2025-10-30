def checkDayMonth(day, month):
    dayInMonth = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    isValid = month > 0 and month <= 12 and day > 0 and day <= dayInMonth[month % 12]
    if (isValid == False):
        print("Ngày hoặc tháng không hợp lệ")
        return


def enter():
    day = int(input("Nhập ngày sinh của bạn: "))
    month = int(input("Nhập tháng sinh của bạn: "))
    checkDayMonth(day, month)
    return day, month


def solve(day, month):
    zodiac_in_month = {2: ["Bảo Bình (Aquarius)", "Song Ngư (Pisces)", 18],
                       3: ["Song Ngư (Pisces)", "Bạch Dương (Aries)", 20],
                       4: ["Bạch Dương (Aries)", "Kim Ngưu (Taurus)", 20],
                       5: ["Kim Ngưu (Taurus)", "Song Tử (Gemini)", 20],
                       6: ["Song Tử (Gemini)", "Cự giải (Gemini)", 21],
                       7: ["Cự giải (Gemini)", "Sư tử (Leo)", 22],
                       8: ["Sư tử (Leo)", "Xử Nữ (Virgo)", 22],
                       9: ["Xử Nữ (Virgo)", "Thiên Bình (Libra)", 22],
                       10: ["Thiên Bình (Libra)", "Bọ Cạp (Scorpion)", 23],
                       11: ["Bọ Cạp (Scorpion)", "Nhân Mã (Sagittarius)", 22],
                       12: ["Nhân Mã (Sagittarius)", "Ma Kết (Capricon)", 21],
                       1: ["Ma Kết (Capricon)", "Bảo Bình (Aquarius)", 19],
                       }
    if day <= zodiac_in_month[month][2]:
        print(f"Cung hoàng đạo của bạn là: {zodiac_in_month[month][0]}")
    else:
        print(f"Cung hoàng đạo của bạn là: {zodiac_in_month[month][1]}")


isContinue = True;
while isContinue:
    day, month = enter()
    solve(day, month)
    print("Bạn có muốn tiếp tục không?(y/n):")
    ans = input()
    if ans == 'y' or ans == 'Y':
        isContinue = True
    else:
        isContinue = False
