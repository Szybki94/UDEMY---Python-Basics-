from datetime import date

def years_till_endyear():
    
    today = date.today()
    current_year = today.year
    year_end = date(current_year, 12, 31)
    days_left = year_end - today

    return print(f"Untill end of the year, there are {days_left.days} days left :)")

years_till_endyear()
