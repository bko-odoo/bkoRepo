# def fib(x):
# 	a,b=0,1
# 	while b<x:
# 		print b
# 		a,b=b,b+a

# def fib2(x):
# 	a,b=0,1
# 	result=[]
# 	while b<x:
# 		result.append(b)
# 		a,b=b,b+a
# 	return result
# if __name__ == "__main__":
#     import sys
#     fib(int(sys.argv[1]))
from datetime import datetime
import datetime

def sla_days(sla):
 	test_working_days = [0,1,2,3,4]
        test_week_days = [0,1,2,3,4,5,6]
	tic_date = "2017-06-02 08:14:12"
        passing_day = sla
        create_day_week_day = Datetime.from_string(tic_date).weekday()
        for i in range(sla):
            if test_working_days.count((create_day_week_day+i)%len(test_week_days))!=0:
                passing_day+=1
	return passing_day

#[week_days[x] for x in working_days]
 # import pdb; pdb.set_trace()



                # while i<sla.time_days:
                #     w_day = ((create_day_week_day + i) % len(test_week_days)) in test_working_days
                #     print "working day", (create_day_week_day + i) % len(test_week_days)
                #     if not w_day:
                #         passing_day += 1
                #         print "no working day for day ",(create_day_week_day + i+1) % len(test_week_days)
                #     else:
                #         i+=1
                # days_for_ticket = [(create_day_week_day + i+1) % len(test_week_days) for i in range(sla.time_days)]
                # temp = [d for d in days_for_ticket if d not in test_working_days]
                # print "ticket create date ,passing day ",ticket.create_date, passing_day+len(temp)
                # new_deadline = fields.Datetime.from_string(ticket.create_date) +\
                #                      relativedelta.relativedelta(days=passing_day, hours=sla.time_hours, minutes=sla.time_minutes)
                # print "new deadline day of week ",new_deadline.weekday()
                # create_day_week_day=new_deadline.weekday()
                # if create_day_week_day not in test_working_days:
                #     days_for_ticket =  [(create_day_week_day + i+1) % len(test_week_days) for i in range(len(test_week_days))]
                #     temp = [d for d in days_for_ticket if d in test_working_days]
                #     print "new temp",temp
