import pandas as pd
import matplotlib.pyplot as plt
from lib import mean_variable, median_variable, count_variable

def aggregate_statistics(path, variable_list):
    results = dict()
    for i in variable_list:
        results[i] = { 
            "mean" : mean_variable(path, i) ,
              "median" : median_variable(path, i) , 
              "count" : count_variable(path, i) }
    return results

def hist_plot(path, variable_list):

    df = pd.read_csv(path) 
    for variable in variable_list:
        plt.hist(df[[variable]], bins=10,)
        plt.xlabel(variable)
        plt.ylabel('frequency')
        plt.title('Histogram of {0} per job posting'.format(variable))
        plt.savefig("output/{}.png".format(variable))
        plt.clf()


if __name__ == "__main__":
    results = aggregate_statistics(
        'data/LinkedInTechJobsDataset.csv', 
        ["Total_applicants", "Employee_count", "LinkedIn_Followers"]
        )
    for key, value in results.items():
        print (f"\n{key}: {value}")
    hist_plot("data/LinkedInTechJobsDataset.csv", 
        ["Total_applicants", "Employee_count", "LinkedIn_Followers"]
        )
