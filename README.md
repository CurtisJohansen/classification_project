# Classification Project


<h2>Project Objectives:</h2>

- Document all my code for data acquisition, data preparation, exploration, model & evaluation in a jupyter notebook.
- Construct a machine learning model that can predict customer churn via classification technique.
- Deliver a 5 minute presentation via a jupyter notebook walkthrough for my audience, the data science team at CodeUp.


<h2>Business Goals:</h2>

- To find drivers of churn
- Create a machine learning model that can predict customer churn

<h2>Audience</h2>

- CodeUp Data Science Team

<h2>Project Deliverables</h2>

- A final report notebook
- A final report presentation
- All necessary modules to make my project reproducible
- A csv file of prediction probabilities and actual values for species

<h2>Project Context</h2>

- Use the telco dataset from the CodeUp SQL database


<h2>Data Dictionary</h2>

| Attribute | Definition | Data Type |
|---|---|---|
| payment_type_id | How a customer pays their bill each month | int64 |
| contract_type_id | Which contract type a customer has | int64 |
| internet_service_type_id | Type of internet service a customer has | int64 |
| customer_id | Alpha-numeric ID that identifies each customer | object |
gender | Gender of the customer | object
senior_citizen | If customer is 65 or older | int64
partner | If customer is married | object
dependents| If a customer lives with dependents| object
tenure | The length of a customers relationship with Telco measured in months | int64
phone_service | If a customer has phone service | object
multiple_lines | If a customer has multiple phone lines | object
online_security | If a customer has online security add-on| object
online_backup | If a customer has online backups add-on | object
device_protection | If a customer has a protection plan for Telco™ devices| object
tech_support | Whether a customer has technical support add-on| object
streaming_tv |If a customer uses internet to stream tv | object
streaming_movies| If a customer uses internet to stream movies | object
paperless_billing | If a customer is enrolled in paperless billing | object
monthly_charges | The amount a customer pays each month | object
total_charges | The total amount a customer has paid for Telco services | object
internet_service_type | Type of internet service a customer has | object
contract_type | The type of contract a customer has | object
payment_type | How a customer pays their bill | object
churn | Indicates whether a customer has terminated service | object |

<h2>Hypotheses</h2>

Alpha
- a=.05

<h2>Hypothesis 1</h2>

- Ho: There is no association between contract type and customer churn
- Ha: There is a association between contract type and customer churn

<h2>Hypothesis 2</h2>

- Ho: There is no association between automatic payment type and customer churn.
- Ha: There is a association between automatic payment type and customer churn.


<h2>Executive Summary - Conclusions and Next Steps</h2>

Findings:
- Drivers of churn were contract type, payment type and total charges
- Analysis showed that churn rate goes down as tenure increases
- Classification model predicts whether a customer will churn with 78% accuracy

Recommendations:
- Offer discounts to enroll in automatic payment and in a yearly contract
- Work with marking department to come up with a new discount campain



<h1>Plan -> Acquire -> Prepare -> Explore -> Model -> Deliver</h1>
<h2>Plan</h2>

- Create README.md with data dictionary, project and business goals, come up with initial hypotheses.
- Acquire data from the Codeup Database and create a function to automate this process. Save the function in an acquire.py file to import into the Final Report Notebook.
- Clean and prepare data for the first iteration through the pipeline, MVP preparation. Create a function to automate the process, store the function in a prepare.py module, and prepare data in Final Report Notebook by importing and using the funtion.
- Clearly define two hypotheses, set an alpha, run the statistical tests needed, reject or fail to reject the Null Hypothesis, and document findings and takeaways.
- Establish a baseline accuracy and document well.
- Train three different classification models.
- Evaluate models on train and validate datasets.
- Choose the model with that performs the best and evaluate that single model on the test dataset.
- Create csv file with the customer id, the probability of churning, and the model's prediction for each observation in my test dataset.
- Document conclusions, takeaways, and next steps in the Final Report Notebook.

<h2>Acquire</h2>

- Store functions that are needed to acquire data from the telco database on the Codeup data science database server; make sure the acquire.py module contains the necessary imports to run my code.
- The final function will return a pandas DataFrame.
- Import the acquire function from the acquire.py module and use it to acquire the data in the Final Report Notebook.
- Complete some initial data summarization (.info(), .describe(), .value_counts(), ...).
- Plot distributions of individual variables.

<h2>Prepare</h2>

- Store functions needed to prepare the telco data; make sure the module contains the necessary imports to run the code. The final function should do the following: - Split the data into train/validate/test. - Handle any missing values. - Handle erroneous data and/or outliers that need addressing. - Encode variables as needed. - Create any new features, if made for this project.
- Import the prepare function from the prepare.py module and use it to prepare the data in the Final Report Notebook.

<h2>Explore</h2>

- Answer key questions, my hypotheses, and figure out the features that can be used in a classification model to best predict the target variable, species.
- Run at least 2 statistical tests in data exploration. Document my hypotheses, set an alpha before running the tests, and document the findings well.
- Create visualizations and run statistical tests that work toward discovering variable relationships (independent with independent and independent with dependent). The goal is to identify features that are related to churn (the target), identify any data integrity issues, and understand 'how the data works'. If there appears to be some sort of interaction or correlation, assume there is no causal relationship and brainstorm (and document) ideas on reasons there could be correlation.
- Summarize my conclusions, provide clear answers to my specific questions, and summarize any takeaways/action plan from the work above.

<h2>Model</h2>

- Establish a baseline accuracy to determine if having a model is better than no model and train and compare at least 3 different models. Document these steps well.
- Train (fit, transform, evaluate) multiple models, varying the algorithm and/or hyperparameters you use.
- Compare evaluation metrics across all the models you train and select the ones you want to evaluate using your validate dataframe.
- Feature Selection (after initial iteration through pipeline): Are there any variables that seem to provide limited to no additional information? If so, remove them.
- Based on the evaluation of the models using the train and validate datasets, choose the best model to try with the test data, once.
- Test the final model on the out-of-sample data (the testing dataset), summarize the performance, interpret and document the results.

<h2>Reproduce My Project</h2>

- Python
- SQL
- classification models
Libraries:
- pandas
- numpy
- matplotlib/seaborn
- sklearn
- stats
- You will need your own env file with database credentials along with all the necessary files listed below to run my final project notebook.
- Read this README.md
- Download the aquire.py, prepare.py, and final_report.ipynb files into your working directory
- Add your own env file to your directory. (user, password, host)
- Run the final_report.ipynb notebook