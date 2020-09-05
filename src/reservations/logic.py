# Checks for any reservations made by the user in the current day the timeslot is in
def reservation_exists(user, timeslot):
    customer = user.customer
    day = timeslot.day
    # tslots stands for timeslots
    day_tslots = day.timeslot_set.all()

    # tslot stands for timeslot
    tslot = day_tslots[0]
    tslot_reservations = timeslot.reservation_set.all()

    res_exists = False
    i = 0
    while res_exists is False and i < len(day_tslots):
        n = 0
        while n < len(tslot_reservations) and res_exists == False:
            reservation = tslot_reservations[n]
            if reservation.customer == customer:
                res_exists = True
            n += 1

        i += 1
        tslot = day_tslots[i]
        timesloslot_reservations = timeslot.reservation_set.all()

    i = 0

    return res_exists