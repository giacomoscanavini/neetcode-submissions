class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        waits = 0
        nCustomers = len(customers)

        busy = 0
        for i,customer in enumerate(customers):
            arrive, order = customer
            if arrive < busy:
                extra = busy - arrive
                busy += order
                waits += extra + order
            
            else:
                busy = arrive + order
                waits += order

        return waits / nCustomers
