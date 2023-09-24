[![Format](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project1/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project1/actions/workflows/format.yml)
[![Lint](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project1/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project1/actions/workflows/lint.yml)
[![Install](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project1/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project1/actions/workflows/install.yml)
[![Test](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project1/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project1/actions/workflows/test.yml)

IDS706_DataEngineering_BarbaraFlores_Project1
## 🤖 Continuous Integration using GitHub Actions of Python Data Science Project

In this project, we delve into the world of Continuous Integration (CI), harnessing the power of GitHub Actions to streamline and improve the development process of a Python Data Science project. 
As a learning exercise for various data engineering tools, we analyze a database, using the following files:

- Jupyter Notebook [LinkedInTechJobs.ipynb](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project1/blob/main/src/LinkedInTechJobs.ipynb) with:
  - Cells that perform descriptive statistics using **Pandas**.
  - Tested by using nbval plugin for pytest
- Python Script [script.py](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project1/blob/main/src/script.py) performing the same descriptive statistics using **Pandas**
- [lib.py](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project1/blob/main/src/lib.py) file that shares the common code between the script and notebook
- [Makefile](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project1/blob/main/Makefile) with the following:
  - Run all tests (notebook and script and lib)
  - Formats code with Python black
  - Lints code with Ruff
  - Installs code via:  pip install -r requirements.txt
- [test_script.py](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project1/blob/main/test/test_script.py) to test script
- [test_lib.py](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project1/blob/main/test/test_lib.py) to test library
- Pinned [requirements.txt](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project1/blob/main/requirements.txt)
- [GitHub Actions](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project1/tree/main/.github/workflows) performs all four Makefile commands with badges for each one in the README.md

### 🔍 Dataset: 
For this asigment, we will use the [LinkedIn Tech Jobs dataset](https://www.kaggle.com/datasets/joebeachcapital/linkedin-jobs?resource=download&select=final_data.csv) 

The [LinkedInTechJobsDataset.csv](data/LinkedInTechJobsDataset.csv) is a comprehensive collection of job listings and related information sourced from LinkedIn, one of the world's leading professional networking platforms. This dataset provides valuable insights into job opportunities, job market trends, and various attributes associated with job listings .


### 🎥 Demo Video
Here is a videdo explaining the project and demonstrating the functionality of the project.
[Video](https://www.youtube.com/watch?v=VtNXbpcRzgg&ab_channel=B%C3%A1rbaraFloresR%C3%ADos)

### 📊 Results

We can see certain descriptive statistics of the variables:

- Total_applicants
- Employee_count
- LinkedIn_Followers
  

|          |  Total_applicants |   Employee_count  |LinkedIn_Followers | 
|:---------|------------------:|------------------:|------------------:|
| mean     | 23                | 5178              | 1401891           |
| median   | 8                 | 5000              | 270280            |
| count    | 811               | 811               | 811               |



However, measures of central tendency often conceal the true data distribution, so we create a histogram to visualize its distribution more effectively

![Total_applicants](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project1/blob/main/output/Total_applicants.png)

![Employee_count](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project1/blob/main/output/Employee_count.png)

![Total_applicants](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project1/blob/main/output/LinkedIn_Followers.png)
