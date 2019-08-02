import pandas as pd
 
class CreditApplication:
    def __init__(self, ds_ratio, business_age, length_rel, positive_rel, complete_app):
        """Initialize credit application object"""
        self.ds_ratio = ds_ratio
        self.business_age = business_age
        self.length_rel = length_rel
        self.positive_rel = positive_rel
        self.complete_app = complete_app
        

    def calculate_score(self):
        """Calculate credit_score coefficients and credit_score"""
        score = 215
        return score

    def accept_reject(self):
        """Accept or reject credit application based on some criteria"""
        if self.ds_ratio >= 200 or self.business_age >= 4 or self.length_rel >= 6 or self.positive_rel == True or self.complete_app == True:
            print('Reject')
        else:
            score = self.calculate_score()
            if score < 222:
                print("Accept")
            elif score >= 222:
                print("Accept with Caution")
            else:
                print("Reject")




# Test by building an object
my_application=CreditApplication(100, 2, 4, False, False)
my_application.accept_reject()

#Assuming we have a dataset we could import the dataset with pandas and process a batch of 100


