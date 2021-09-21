import random


def extract_date(month, day):
    if month == "january":
        number_of_days = 0
    elif month == "february":
        number_of_days = 31
    elif month == "march":
        number_of_days = 59
    elif month == "april":
        number_of_days = 90
    elif month == "may":
        number_of_days = 120
    elif month == "june":
        number_of_days = 151
    elif month == "july":
        number_of_days = 181
    elif month == "august":
        number_of_days = 212
    elif month == "september":
        number_of_days = 243
    elif month == "october":
        number_of_days = 273
    elif month == "november":
        number_of_days = 304
    elif month == "december":
        number_of_days = 334
    else:
        number_of_days = None
        print("you inputted an invalid month")

    total = number_of_days+ day
    return total




def convert_date(no_of_days):
    if no_of_days > 0 and no_of_days <= 31:
        month = "january"
        day = no_of_days - 0
    elif no_of_days > 31 and no_of_days <= 59:
        month = "february"
        day = no_of_days - 31
    elif no_of_days > 59 and no_of_days <= 90:
        month = "march"
        day = no_of_days - 59
    elif no_of_days > 90 and no_of_days <= 120:
        month = "april"
        day = no_of_days - 90
    elif no_of_days > 120 and no_of_days <= 151:
        month = "may"
        day = no_of_days - 120
    elif no_of_days > 151 and no_of_days <= 181:
        month = "june"
        day = no_of_days - 151
    elif no_of_days > 181 and no_of_days <= 212:
        month = "july"
        day = no_of_days - 181
    elif no_of_days > 212 and no_of_days <= 243:
        month = "august"
        day = no_of_days - 212
    elif no_of_days > 243 and no_of_days <= 273:
        month = "september"
        day = no_of_days - 243
    elif no_of_days > 273 and no_of_days <= 304:
        month = "october"
        day = no_of_days - 273
    elif no_of_days > 304 and no_of_days <= 334:
        month = "november"
        day = no_of_days - 304
    elif no_of_days > 334 and no_of_days <= 366:
        month = "december"
        day = no_of_days - 334
    else:
        month = "january"
        day = no_of_days - 366
    return [month, day]


def next_period(start_day):
    if cycle_type == "short":
        lower_bound = start_day + 25
        upper_bound = start_day + 27
    elif cycle_type == "regular":
        lower_bound = start_day + 28
        upper_bound = start_day + 31
    elif cycle_type == "long":
        lower_bound = start_day + 32
        upper_bound = start_day + 35
    lower_estimate = convert_date(lower_bound)
    upper_estimate = convert_date(upper_bound)
    return f"Your next period is expected to fall between {lower_estimate[1]}th {lower_estimate[0]} and  {upper_estimate[1]}th {upper_estimate[0]}"

def fertility_window(start_day):
    if cycle_type == "short":
        lower_bound = start_day + 0
        upper_bound = start_day + 8

        lower_lower_bound = start_day + 5
        upper_upper_bound = start_day + 7

    elif cycle_type == "regular":
        lower_bound = start_day + 9
        upper_bound = start_day + 15

        lower_lower_bound = start_day + 12
        upper_upper_bound = start_day + 14

    elif cycle_type == "long":
        lower_bound = start_day + 14
        upper_bound = start_day + 22

        lower_lower_bound = start_day + 19
        upper_upper_bound = start_day + 21

    lower_estimate = convert_date(lower_bound)
    upper_estimate = convert_date(upper_bound)

    lower_lower_estimate = convert_date(lower_lower_bound)
    upper_upper_estimate = convert_date(upper_upper_bound)
    return f"Your fertility window is between {lower_estimate[1]}th {lower_estimate[0]} and {upper_estimate[1]}th {upper_estimate[0]}. But you are most fertile between {lower_lower_estimate[1]}th {lower_lower_estimate[0]} and {upper_upper_estimate[1]}th {upper_upper_estimate[0]}"


def select_tip():
    t1 = "Don't forget to change your sanitary pad regularly"
    t2 = "Always wash yourself properly"
    t3 = "Be hygenic and remember to wear clean undergarments"
    t4 = "Don't forget to dispose your sanitary pads properly"
    t5 = "Consume a balanced diet and stay healthy"
    tip = random.choice([t1, t2, t3, t4, t5])
    return f"TIP OF THE DAY: {tip}"




print("Welcome, I'm your menstrual cycle assistant!")
initial = input("What will you like to know? Type 'next period' OR 'fertility window' OR 'both'").lower()

print("When did you start your last period?")
month = input("Input the month here: ").lower()
day = int(input("Input the day here: "))
cycle_type = input("Do you typically have a short menstrual cycle? (input 'short')? OR a regular menstrual cycle? (input 'regular') OR a long menstrual cycle? (input 'long/'").lower()
start_day = extract_date(month, day)

if initial == "next period":
    print(next_period(start_day))
elif initial == "fertility window":
    print(fertility_window(start_day))
elif initial == "both":
    print(next_period(start_day))
    print(fertility_window(start_day))
print(select_tip())