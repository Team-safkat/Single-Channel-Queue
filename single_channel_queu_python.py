
print("\t\t\tSIMULATION Assignment 5\n\n")
#no_of_customer = 20

#using poisson distribution
from scipy.stats import *

inter_arrival = poisson.rvs( mu = 5.6,size=20 )
inter_arrival[0] = 0
print(inter_arrival)


arrival_time = [0]
for i in range(1,20):
  arrival_time.append( inter_arrival[i] + arrival_time[i-1] )
print(arrival_time)


print("Customer no.","\tInter_arrival_Time","\tArrival_Time")
for i in range(20):
  print("\t",i,"\t\t ",inter_arrival[i], "\t\t" ,arrival_time[i])
  
  
#using exponential distribution
import math
data_expons =  expon.rvs(size=20,loc=5,scale=1)
#for i in range(20):
  #data_expon[i] = math.trunc(data_expon[i])
  
service_time = [math.trunc(data_expon) for data_expon in data_expons]
print(service_time)


time_service_begin = [0]
customer_wait = [0]
idle_time_server = [0]
time_service_end = []
customer_spend_system = []

value1 = (arrival_time[0] + service_time[0] + customer_wait[0])
time_service_end = [ value1 ]

value2 = (service_time[0] + customer_wait[0])
customer_spend_system = [ value2 ]

print(time_service_end)
print(customer_spend_system)



count_customer_wait = 0
total_waiting_time = 0

for i in range(1,20):
  #value = i-1
  #print(i, "-- ",value)
  #print(time_service_begin)
  
  time_service_begin.append(max(time_service_end[i-1], arrival_time[i]))
  
  if (arrival_time[i] >= time_service_end[i-1 ]):
    customer_wait.append(0)
  else:
    customer_wait.append( time_service_end[i-1] - arrival_time[i] )
    count_customer_wait +=1
    total_waiting_time = total_waiting_time + customer_wait[i]
  
  
  time_service_end.append((arrival_time[i] + service_time[i] + customer_wait[i]))
  customer_spend_system.append((service_time[i] + customer_wait[i]))


  if (arrival_time[i] > time_service_end[i-1 ]):
   idle_time_server.append( arrival_time[i] - time_service_end[i-1] ) 
  else:
    idle_time_server.append(0) 
  
  
  avg_no_of_customer_wait = count_customer_wait / 20
  avg_waiting_time = total_waiting_time / 20
  


print("\t\t\t\t\t\t\t-------------------------- ----------------------")
print("\t\t\t\t\t\t\t|\t\t\t\t\t\t|")
print("\t\t\t\t\t\t\t|\tSingle Channel Queuing Problem\t\t|")
print("\t\t\t\t\t\t\t|\t\t\t\t\t\t|")
print("\t\t\t\t\t\t\t-------------------------------------------------")

print("\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Customer No.","\tInter_Arrival_Time","\tArrival_Time","\tService_Time","\tTime_Service_Begin","\tCustomer_Wait_In_Queue","\tTime_Service_End","\tCustomer_Spend_In_System","\tServer_Idle_Time")
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


for i in range(20):
  print("\t",i,"\t\t",inter_arrival[i],"\t\t  ",arrival_time[i],"\t\t  ",service_time[i],"\t\t\t",time_service_begin[i],"\t\t\t",customer_wait[i],"\t\t\t",time_service_end[i],"\t\t\t",customer_spend_system[i],"\t\t\t\t",idle_time_server[i])


print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
print("Average NO of Customer waiting in the Queue : ",avg_no_of_customer_wait)
print("Average Waiting Time of a Customer : ",avg_waiting_time)