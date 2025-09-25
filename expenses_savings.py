class netincome:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def add_income(self, **incomes):
        print(f'{self.name}\'s income as follows:\n{self.name}\'s salary is {self.salary}')
        self.current_income=self.salary
        for key, value in incomes.items():
            print(f'{key}={value}')
            self.current_income=self.current_income+value
        return self.current_income
    def subtract_expenses(self,**expenses):
        print(f'{self.name}\'s expenses as follows:\n{self.name}\'s total income is {self.current_income}')
        current_savings=self.current_income
        for key, value in expenses.items():
            print(f'{key}={value}')
            current_savings=current_savings-value
        return current_savings
def main():
    input_=[input("Enter name ") if i==0 else input("Enter salary ") for i in range(2) ]
    return input_
if __name__ == "__main__":
    input_=main()
    surya_=netincome(input_[0],int(input_[1]))
    total_income=surya_.add_income(house_rent=1000,interest=1000)
    print(f'{surya_.name}\'s total income is {total_income}')
    total_savings=surya_.subtract_expenses(school_fees=1000,bike_pretrol=1000,emi=3000,other=3000)
    print(f'{surya_.name}\'s total savings is {total_savings}')





    
