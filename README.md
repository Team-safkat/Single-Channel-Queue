## Single-Channel-Queuing Problem 
In Single-Channel-Queuing Problem, one customer is served at a single time. If the server is busy then the customers have to wait in queue.<br/><br/>
We have to solve single channel queuing problem in python. Firstly, we have to define inter arrival time by using **Poisson distribution** and Service time are define by using
**Exponential distribution**. This problem is defined for 20 customers.<br/><br/>
First inter arrival time, arrival time, Time service begin, customer wait in queue, idle term of server is defined as 0.<br/><br/>
The value of second to twenty value are find by using this function <br/>
       ***`arrival_time[i] = arrival time[i-1] + inter_arrival_time[i].`***<br/><br/>
The time_service_begin are find in,<br/> ***`if `<br/> `previous customer time_service_end >= present customer_arrival_time`<br/>`then` <br/>`Time_Service_Begin (TSB) = Time_Service_end (TSE)`<br/> `else`<br/>`Time_Service_Begin (TSB) = Arrival time.`***  <br/><br/>
Customer wait in queue are finding by using this formula <br/>***`if`<br/> `present arrrival time >= previous time_service_end` <br/>`then`<br/> `Customer_wait_in_queue = 0`<br/> `else` <br/>`Customer_wait_in_queue = previous time_service_end present arrival time.`***<br/><br/>
Now<br/> ***`Time_service_end = arrival_time + service_time + Customer_wait_in_queue.`***<br/><br/>
***`The customer spend in system = Service_time + Customer_wait_in_queue.`*** <br/><br/>
Idle_time_of_Server are finding by using this formula.<br/>
 If<br/> ***`present_customer_arrival_time > previous customer time_service_end`***<br/> then,<br/> ***`Idle_time_of_Server = present arrrival time - previous time_service_end`***<br/> else<br/> ***`Idle_time_of_Server = 0.`***<br/><br/>
Now find average number of customers waiting in the queue and average waiting time.<br/>
	***`Average number of customers waiting in the queue =   (Number of customer waiting in queue)/(Number of customer)`***<br/>
	***`Average waiting time = (Total waiting time)/(Total number of customer)`***<br/>
    
