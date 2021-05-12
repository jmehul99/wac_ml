def calculate_si(principle, time, rate):
    return principle*time*rate/100

def total_amount(principle,time, rate):
    si = calculate_si(principle,time, rate)
    return si + principle

