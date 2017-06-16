    def _get_next_working_day_by_sla(self,ticket,count,working_days):
        for day in rrule.rrule(rrule.DAILY,
                               dtstart=fields.Datetime.from_string(ticket.create_date) + timedelta(days=1),
                               interval=1, count=count, byweekday=working_days):
            final_day = day
        return final_day

    #add hours regarding working hours
    def _get_next_working_hour_by_sla(self,ticket):
        for hour in rrule.rrule(rrule.HOURLY,
                               dtstart=fields.Datetime.from_string(ticket.create_date) + timedelta(days=1),
                               interval=1, count=18, byhour=[8,9,10,11,12]):
            final_hour = hour
        return final_hour
