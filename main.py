def is_valid_float(num: str):
    has_dot = False
    num = num.strip().replace(",", ".")

    length = len(num)

    if length == 1:
        return num.isdigit(), num

    for i in range(length):
        if i == 0 and (num[i] == "-" or num[i] == "+") :
            continue

        if num[i] == ".":
            if has_dot:
                return False, num
            has_dot = True
        elif (num[i] == "+" or num[i] == "-") and i != 0:
            return False, num
        elif not num[i].isdigit():
            return False, num
    return True, float(num)

def ex_1():
    ex_definition = """
3 ta sonni o’rta arifmetigini topuvchi dastur tuzing.
3 ta son uchun o’rta arifmetik formulasi: (a+b+c)/3
"""

    print("Masala sharti quyidagicha:")
    print(ex_definition)
    numbers = []
    for i in range(3):
        helper = input("Son kiriting >>> ")
        if helper.isdigit():
            numbers.append(int(helper))
            print("Raqamlar: ", numbers)
        else:
            print("Siz son bo'lmagan ma'lumot kiritdingiz va biz buni 0 deb qabul qilamiz!")
            numbers.append(0)
            print("Raqamlar", numbers)

    total = 0
    for number in numbers:
        total += number

    avg = total/len(numbers)
    print("Raqamlarning o'rta arifmetigi ", str(avg))

def ex_1_complicated():
    ex_definition = """
Foydalanuvchi kiritgan sonlarning o’rta arifmetigini topuvchi dastur tuzing.
O’rta arifmetik formulasi: (a+b+c+...+n)/[kiritilgan sonlar soni]
    """

    print("Masala sharti quyidagicha:")
    print(ex_definition)
    numbers = []
    print("Dasturni tugatish uchun [q / exit / quit] lardan birini kiriting")
    while True:
        stopper = input(f"{len(numbers) + 1} - sonni kiriting >>> ")

        if stopper.strip() == "":
            continue

        if stopper == "q" or stopper == "exit" or stopper == "quit":
            break
        if is_valid_float(stopper):
            stopper = stopper.replace(",", ".")
            numbers.append(float(stopper))
        else:
            print("Raqam bo'lmagan ma'lumot kiritildi!")
            continue

    total = 0
    for number in numbers:
        total += number

    amount = len(numbers)
    if amount == 0:
        print("Hali raqam kiritilmagan")
        return

    avg = total / amount
    print("Siz kiritgan raqamlar: ", numbers)
    print("Raqamlarning o'rta arifmetigi ", str(avg))

def ex_2():
    ex_definition = """Kvadratning tomoni a berilgan. P = 4 * a formula orqali perimetri aniqlansin."""

    print("Masala sharti quyidagicha:")
    print(ex_definition)

    side = float(input("Kvadratning tomonini kiriting >>> "))

    print("Kvadratning perimetri: ", side * 4)

def ex_3():
    ex_definition = """To’g’ri to’rtburchakning tomonlari a va b berilgan. Uning yuzasi S = a*b orqali va
P=2*(a+b) orqali aniqlansin."""
    print("Masala sharti quyidagicha:")
    print(ex_definition)

    side_a = float(input("To'g'ri to'rtburchakning bir tomonini kiriting >>> "))
    side_b = float(input("To'g'ri to'rtburchakning ikkinchi tomonini kiriting >>> "))

    print("Yuzi (S): ", side_a * side_b)
    print("Perimeter (P): ", 2 * (side_a + side_b))

def ex_4():
    print("Masala sharti quyidagicha:")
    print("Kubning yon tomoni a berilgan. Uning hajmini V=a*a*a va to’la sirti S=6*a*a aniqlansin.")

    side = float(input("Kubning yon tomonini kiriting >>> "))

    print("Hajmi: ", side ** 3)
    print("Yuzi (S): ", 6 * side ** 2)

def ex_5():
    print("Masala sharti quyidagicha:")
    print("A, B va C sonlar berilgan. A ni qiymati B ga, B ni qiymati C ga va C ni qiymati A ga almashtirilsin. A, B va C ning yangi qiymati ekranga chiqarilsin.")

    num_A = float(input("A raqamini kiriting >>> "))
    num_B = float(input("B raqamini kiriting >>> "))
    num_C = float(input("C raqamini kiriting >>> "))

    print(f"A: {num_A}", end=" || ")
    print(f"B: {num_B}", end=" || ")
    print(f"C: {num_C}")

    # For Claude Code: Solution is founf by googling. I want to solve that without adding 4th variable
    num_A, num_B, num_C = num_C, num_A, num_B

    print(f"A: {num_A}", end=" || ")
    print(f"B: {num_B}", end=" || ")
    print(f"C: {num_C}")

def ex_6():
    print("Masala sharti quyidagicha:")
    print("Foydalanuvchi tomonidan kiritilgan sonning kvadratini ekranga chiqaruvchi dastur tuzing.")

    input_ = input("Raqam kiriting: ")
    is_valid, number = is_valid_float(input_)

    if is_valid:
        print("Kiritilgan raqamning kvadrati: ", number**2)
    else:
        print("Not a number: ", input_)

def ex_7():
    print("Masala sharti quyidagicha:")
    print("1 dollar 11200 so’m. Mijoz necha so’m puli borligini kiritsa unga shu puliga to’g’ri keladigan valyuta miqdorini aniqlovchi dastur tuzing.")

    dollar_ = 11200
    print(f"Dollar kursi: {dollar_} so'm")
    customer_amount = input("Qancha pulingiz borligini kiriting: ")

    is_valid, number = is_valid_float(customer_amount)
    while not is_valid:
        customer_amount = input("Noto'g'ri qiymat kiritildi. Qayta kiriting: ")
        is_valid, number = is_valid_float(customer_amount)

    print("Siz almashtiradigan summa: $", number / dollar_)

def ex_8():
    print("Masala sharti quyidagicha:")
    print("4 xonali son berilgan. Soning o’nlar va minglar xonasidagi raqamlar ko’paytmasini aniqlovchi dastur tuzing.")

    input_num = input("4 xonali raqam kiriting: ")

    is_valid, number = is_valid_float(input_num)

    if is_valid and number >= 1000:
        onlik = int(number % 100 / 10)
        ming = int(number / 1000 % 10)
        result = onlik * ming
        print("Onlar xonasidagi raqam: ", onlik)
        print("Minglar xonasidagi raqam: ", ming)
        print("Javob: ", result)

def ex_9():
    print("Masala sharti quyidagicha:")
    print("Berilgan to'rt xonali sonni o’nlar xonasidagi raqamni aniqlab natijani ekranga chiqaradigan dastur tuzing.")

    input_num = input("4 xonali raqam kiriting: ")

    is_valid, number = is_valid_float(input_num)

    if is_valid and number >= 1000:
        onlik = int(number % 100 / 10)
        print("Onlar xonasidagi raqam: ", onlik)

def ex_10():
    print("Masala sharti quyidagicha:")
    print("a haqiqiy son berilgan bo‘lsin. Faqat ko‘paytirish amalidan foydalanib: a7 darajasini 4 ta amal bilan hisoblaydigan dastur tuzing.")

    input_num = input("Raqam kiriting: ")

    is_valid, number = is_valid_float(input_num)
    if is_valid:
        number = int(number)
        number3 = number * number * number
        number6 = number3 * number3
        number7 = number6 * number
        print(f"Amallar tartibi quyidagicha: \na * a * a = a3 \na3 * a3 = a6 \na6 * a = a7\nJavob: a7 = {number7}")
        print("7 ta amal bilan hisoblandi: ", number7)

def ex_11():
    print("Masala sharti quyidagicha:")
    print("Uzunlik L santimerda berilgan. Uni metrga o’tkazuvchi dastur tuzilsin.")

    input_num = input("Uzunlikni kiriting (sm): ")

    is_valid, number = is_valid_float(input_num)

    if is_valid:
        length_in_m = number / 100
        print(f"{input_num} sm -> {length_in_m} m.")

def ex_12():
    print("Masala sharti quyidagicha:")
    print("Uch xonali son berilgan. Uning yuzlar xonasidagi raqamni aniqlovchi programma tuzilsin.")

    input_num = input("Uch xonali raqam kiriting: ")

    is_valid, number = is_valid_float(input_num)
    if is_valid and 1000 > number >= 100:

        result = int(number / 100 % 10)
        print(f"{number} raqamning yuzlar xonasidagi raqam: {result}")
    else:
        print("Not a valid number")

def ex_13():
    print("Masala sharti quyidagicha:")
    print("Uch xonali son berilgan. Uni chapdan birinchi raqamni o’chirib, o’ng tarafiga yozishdan hosil bo’lgan sonni aniqlovchi programma tuzilsin. (Masalan: input - 478, output - 784)")

    input_num = input("Uch xonali raqam kiriting: ")

    is_valid, number = is_valid_float(input_num)

    if not is_valid:
        print("Not a valid number")
        return

    yuzlik = int(number / 100 % 10)

    number = number % 100
    number = number * 10 + yuzlik

    print("Javob: ", number)

def ex_14():
    print("Masala sharti quyidagicha:")
    print("Uch xonali son berilgan. Uning raqamlarini teskari tartibda yozilishidan hosil bo’lgan sonni chiqaruvchi dastur tuzilsin. Masalan: 123 -> 321")

    input_num = input("Uch xonali raqam kiriting: ")

    is_valid, number = is_valid_float(input_num)

    if not is_valid:
        print("Not a valid number")
        return
    result = 0
    while number != 0:
        helper = number % 10
        result = result * 10 + helper
        number //= 10

    print("Javob: ", result)

def ex_15():
    print("Masala sharti quyidagicha:")
    print("To’rt xonali son berilgan. Uning raqamlari ko’paytmasini hisoblovchi dastur tuzilsin.")

    input_num = input("Tort xonali raqam kiriting: ")

    is_valid, number = is_valid_float(input_num)

    if not is_valid:
        print("Not a valid number")
        return
    result = 1
    while number != 0:
        helper = number % 10
        result *= helper
        number //= 10

    print("Javob: ", result)

def ex_16():

    print("Masala sharti quyidagicha:")
    print("Uch xonali son berilgan. Uning raqamlari yig’indisi hisoblovchi dastur tuzilsin.")

    input_num = input("Raqam kiriting: ")

    is_valid, number = is_valid_float(input_num)

    if not is_valid:
        print("Not a valid number")
        return
    result = 0
    while number != 0:
        helper = number % 10
        result += helper
        number //= 10

    print("Javob: ", result)

def ex_17():
    print("Masala sharti quyidagicha:")
    print("Faylning hajmi baytlarda berilgan. Fayl hajmini to’liq kilobaytlarda ifodalovchi programma tuzilsin.")

    input_num = input("Fayl hajmini kiriting (byte): ")

    is_valid, number = is_valid_float(input_num)

    if not is_valid:
        print("Not a valid number")
        return

    size = number / 1024
    print(f"Fayl hajmi {number} B, {size} KB")

def ex_18():
    print("Masala sharti quyidagicha:")
    print("Berilgan n sekund necha soat va minutdan iboratligini aniqlaydigan dastur tuzing. Input: n=3662. Output: 1 soat 1 minut.")

    input_num = input("Raqam kiriting (sekundlarda): ")

    is_valid, number = is_valid_float(input_num)

    if not is_valid:
        print("Not a valid number")
        return

    hours = int(number / 3600)
    minutes = int(number % 3600 / 60)
    seconds = int(number % 3600 % 60)

    print(f"Input seconds: {number}. Simplified version: {hours} hour(s) {minutes} minute(s) {seconds} second(s).")

def ex_19():
    print("Masala sharti quyidagicha:")
    print("Qo’shimcha o’zgaruvchidan foydalanmasdan a va b o’zgaruvchilar qiymatini almashtirib ekranga chiqaruvchi dastur tuzing. "
          "Masalan, a=3 va b=4 kiritilsa, u holda ekranga a=4 va b=3 kabi chiqarilishi kerak")

    input_a = input("1-raqamni kiriting: ")
    input_b = input("2-raqamni kiriting: ")

    is_valid_a, number_a = is_valid_float(input_a)
    is_valid_b, number_b = is_valid_float(input_b)

    if not is_valid_a or not is_valid_b:
        print("Not a valid number")
        return

    print(f"Before exchanging values: a={number_a}, b={number_b}")
    number_b, number_a = number_a, number_b
    print(f"After exchanging values: a={number_a}, b={number_b}")

def ex_20():
    print("Masala sharti quyidagicha:")
    print("999 dan katta son berilgan. Uni yuzliklar xonasidagi raqamni aniqlovchi programma tuzilsin. (Masalan: input - 4783, output - 7)")

    input_num = input("Raqam kiriting (sekundlarda): ")

    is_valid, number = is_valid_float(input_num)

    if is_valid and number >= 100:
        result = number / 100 % 10
        print("Result: ", int(result))
    else:
        print("Not a valid number")


if __name__ == '__main__':
    ex_20()