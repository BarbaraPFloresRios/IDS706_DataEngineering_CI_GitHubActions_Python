import requests
from script import aggregate_statistics


def test_aggregate_statistics():

     results = aggregate_statistics(
        'LinkedInTechJobsDataset.csv', 
        ["Total_applicants", "Employee_count", "LinkedIn_Followers"]
        )
     assert results['Total_applicants']["count"] == 811
     assert results['Employee_count']["count"] == 811
     assert results['LinkedIn_Followers']["count"] == 811


def test_github_file_existence():
    name = "nogibjj" 
    repo = "IDS706_DataEngineering_BarbaraFlores_Project1"  
    path_to_file = "output/Total_applicants.png"  
    url = f"https://api.github.com/repos/{name}/{repo}/contents/{path_to_file}"
    
    response1 = requests.get(url)
    
    assert response1.status_code == 200


if __name__ == "__main__":
    test_github_file_existence()
    test_aggregate_statistics()
