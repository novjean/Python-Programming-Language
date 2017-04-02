from mrjob.job import MRJob
from mrjob.job import MRStep

class CustomerWorth(MRJob):
    
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_cust_amount,
                    reducer=self.reducer_cust_total),
            MRStep(mapper=self.mapper_make_total_key,
                    reducer=self.reducer_output_sorted_customer_total)
        ]
    
    def mapper_get_cust_amount(self, _ , line):
        (customer, item, amount) = line.split(',')
        yield customer,float(amount)
        
    def reducer_cust_total(self, customer, amounts):
        yield customer, sum(amounts)
    
    def mapper_make_total_key(self, customer, total):
        yield '%04.02f'%float(total), customer
        
    def reducer_output_sorted_customer_total(self, total, customers):
        for customer in customers:
            yield total, customer
        
if __name__ == '__main__':
    CustomerWorth.run()