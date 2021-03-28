## Single-Channel-Queuing Problem 
In Single-Channel-Queuing Problem, one customer is served at a single time. If the server is busy then the customers have to wait in queue.<br/><br/>
We have to solve single channel queuing problem in python. Firstly, we have to define inter arrival time by using **Poisson distribution** and Service time are define by using
**Exponential distribution**. This problem is defined for 20 customers.<br/><br/>
First inter arrival time, arrival time, Time service begin, customer wait in queue, idle term of server is defined as 0.<br/><br/>
The value of second to twenty value are find by using this function: <br/><br/>
       ***`arrival_time[i] = arrival time[i-1] + inter_arrival_time[i].`***<br/><br/><br/>
The time_service_begin are find in:<br/><br/> ***`if `<br/> `__  previous customer time_service_end >= present customer_arrival_time`<br/>`then` <br/>`__ Time_Service_Begin (TSB) = Time_Service_end (TSE)`<br/> `else`<br/>`__ Time_Service_Begin (TSB) = Arrival time.`***  <br/><br/><br/>
Customer wait in queue are finding by using this formula: <br/><br/>***`if`<br/> `___ present arrrival time >= previous time_service_end` <br/>`then`<br/> `___ Customer_wait_in_queue = 0`<br/> `else` <br/>`___ Customer_wait_in_queue = previous time_service_end present arrival time.`***<br/><br/>
Now<br/> ***`Time_service_end = arrival_time + service_time + Customer_wait_in_queue.`***<br/><br/>
***`The customer spend in system = Service_time + Customer_wait_in_queue.`*** <br/><br/><br/>
Idle_time_of_Server are finding by using this formula:<br/><br/>
***`if `<br/> `___ present_customer_arrival_time > previous customer time_service_end`<br/> `then`<br/> `___ Idle_time_of_Server = present arrrival time - previous time_service_end`<br/> `else`<br/> `___ Idle_time_of_Server = 0.`***<br/><br/><br/>
Now find average number of customers waiting in the queue and average waiting time:<br/><br/>
	***`Average number of customers waiting in the queue =   (Number of customer waiting in queue)/(Number of customer)`***<br/>
	***`Average waiting time = (Total waiting time)/(Total number of customer)`***<br/>
    

## Team-Safkat members
-  👋 Hi, I’m [Safkat Khan](https://github.com/Safkatlp)
-  👋 Hi, I’m [Mominul Hoque](https://github.com/mominul104)
-  👋 Hi, I’m [M.A. Nabil](https://github.com/nabilcse13)
-  👋 Hi, I’m [Saif Hossain](https://github.com/shfx0096)


## What is Probability Distribution
- ***Probability distribution*** yields the possible outcomes for any ***random event***. It is also defined based on the underlying sample space as a set of possible outcomes of any random experiment. These settings could be a set of real numbers or a set of vectors or set of any entities. It is a part of probability and statistics.

## Short introduction to Poisson Distribution
- ***Poisson random variable*** is typically used to model the number of times an event happened in a time interval. For example, the number of users visited on a website in an interval can be thought of a Poisson process. Poisson distribution is described in terms of the rate ***(μ)*** at which the events happen. An event can occur ***0, 1, 2, …*** times in an interval. The average number of events in an interval is designated ***λ (lambda)***. Lambda is the event rate, also called the ***rate parameter***. The probability of observing ***k*** events in an interval is given by the equation:<br/>
 ![image](https://user-images.githubusercontent.com/74718375/112758781-e2de5f00-9011-11eb-952d-a0859d50300e.png)<br/>

## Short introduction to Exponential Distribution
- ***The exponential*** distribution describes the time between events in a ***Poisson point*** process, i.e., a process in which events occur continuously and independently at a constant average rate. It has a parameter ***λ*** called ***rate parameter***, and its equation is described as :<br/>
 ![image](https://user-images.githubusercontent.com/74718375/112759206-d3601580-9013-11eb-909f-b215e2b6ca32.png)<br/>

## Why Poisson Distribution is used for Inter-Arrival Time
- Poison distribution usually works with a ***discrete*** value. Since inter-arrival time does not come in a sequential way, it comes in a random way, so poison distribution is used in this case

## Why Exponential Distribution is used for Service Time
- Exponential Distribution deals with the time between occurrences of successive events as time flows by
continuously. Here starting and ending of service can be considerred as two successive events.
