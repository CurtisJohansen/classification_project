# classification_project


Project Objectives:

Document all my code for data acquisition, data preparation, exploration, model & evaluation in a jupyter notebook.
Create and use functions that automate my process.
Construct a machine learning model that can predict customer churn via classification technique.
Deliver a 5 minute presentation via a jupyter notebook walkthrough for my audience, the data science team at CodeUp.
Answer questions about my code, process, model and summary.
Business Goals:

To find drivers of churn for the Telco company.
Create a machine learning model that can predict customer churn.
Document my process and findings in a clean readable notebook.

Audience

CodeUp Data Science Team

Project Deliverables

A final report notebook
A final report notebook presentation
All necessary modules to make my project reproducible
A csv file of prediction probabilities and actual values for species

Project Context

The telco dataset came from the CodeUp database


Data Dictionary

Attribute	Definition	Data Type
payment_type_id	How a customer pays their bill each month	int64
contract_type_id	Which contract type a customer has	int64
internet_service_type_id	Type of internet service a customer has	int64
customer_id	Alpha-numeric ID that identifies each customer	object
gender	Gender of the customer	object
senior_citizen	If customer is 65 or older	int64
partner	If customer is married	object
dependents	If a customer lives with dependents	object
tenure	The length of a customers relationship with Telco™ measured in months	int64
phone_service	If a customer has phone service	object
multiple_lines	If a customer has multiple phone lines	object
online_security	If a customer has online security add-on	object
online_backup	If a customer has online backups add-on	object
device_protection	If a customer has a protection plan for Telco™ devices	object
tech_support	Whether a customer has technical support add-on	object
streaming_tv	If a customer uses internet to stream tv	object
streaming_movies	If a customer uses internet to stream movies	object
paperless_billing	If a customer is enrolled in paperless billing	object
monthly_charges	The amount a customer pays each month	object
total_charges	The total amount a customer has paid for Telco™ services	object
internet_service_type	Type of internet service a customer has	object
contract_type	The type of contract a customer has	object
payment_type	How a customer pays their bill	object
Target	Definition	Data Type
churn	Indicates whether a customer has terminated service

Executive Summary - Conclusions & Next Steps

Findings:

Early analysis showed that rate of churn goes down as tenure increases
Biggest drivers of churn were payment type, contract type, and total charges
Classification model predicts whether a customer will churn with 78% accuracy
Recommendations:

Offer discounts for automatic payment types and one or two-year contracts
Run advertising campaign promoting new discounts
Next steps:

Test out the model on out of sample data to see how well it performs in the wild
Pipeline Stages Breakdown

Plan -> Acquire -> Prepare -> Explore -> Model -> Deliver

Create README.md with data dictionary, project and business goals, come up with initial hypotheses.
Acquire data from the Codeup Database and create a function to automate this process. Save the function in an acquire.py file to import into the Final Report Notebook.
Clean and prepare data for the first iteration through the pipeline, MVP preparation. Create a function to automate the process, store the function in a prepare.py module, and prepare data in Final Report Notebook by importing and using the funtion.
Clearly define two hypotheses, set an alpha, run the statistical tests needed, reject or fail to reject the Null Hypothesis, and document findings and takeaways.
Establish a baseline accuracy and document well.
Train three different classification models.
Evaluate models on train and validate datasets.
Choose the model with that performs the best and evaluate that single model on the test dataset.
Create csv file with the customer id, the probability of churning, and the model's prediction for each observation in my test dataset.
Document conclusions, takeaways, and next steps in the Final Report Notebook.
Plan -> Acquire -> Prepare -> Explore -> Model -> Deliver

Store functions that are needed to acquire data from the telco database on the Codeup data science database server; make sure the acquire.py module contains the necessary imports to run my code.
The final function will return a pandas DataFrame.
Import the acquire function from the acquire.py module and use it to acquire the data in the Final Report Notebook.
Complete some initial data summarization (.info(), .describe(), .value_counts(), ...).
Plot distributions of individual variables.
Plan -> Acquire -> Prepare -> Explore -> Model -> Deliver

Store functions needed to prepare the telco data; make sure the module contains the necessary imports to run the code. The final function should do the following: - Split the data into train/validate/test. - Handle any missing values. - Handle erroneous data and/or outliers that need addressing. - Encode variables as needed. - Create any new features, if made for this project.
Import the prepare function from the prepare.py module and use it to prepare the data in the Final Report Notebook.
Plan -> Acquire -> Prepare -> Explore -> Model -> Deliver

Answer key questions, my hypotheses, and figure out the features that can be used in a classification model to best predict the target variable, species.
Run at least 2 statistical tests in data exploration. Document my hypotheses, set an alpha before running the tests, and document the findings well.
Create visualizations and run statistical tests that work toward discovering variable relationships (independent with independent and independent with dependent). The goal is to identify features that are related to churn (the target), identify any data integrity issues, and understand 'how the data works'. If there appears to be some sort of interaction or correlation, assume there is no causal relationship and brainstorm (and document) ideas on reasons there could be correlation.
Summarize my conclusions, provide clear answers to my specific questions, and summarize any takeaways/action plan from the work above.
Plan -> Acquire -> Prepare -> Explore -> Model -> Deliver

Establish a baseline accuracy to determine if having a model is better than no model and train and compare at least 3 different models. Document these steps well.
Train (fit, transform, evaluate) multiple models, varying the algorithm and/or hyperparameters you use.
Compare evaluation metrics across all the models you train and select the ones you want to evaluate using your validate dataframe.
Feature Selection (after initial iteration through pipeline): Are there any variables that seem to provide limited to no additional information? If so, remove them.
Based on the evaluation of the models using the train and validate datasets, choose the best model to try with the test data, once.
Test the final model on the out-of-sample data (the testing dataset), summarize the performance, interpret and document the results.
Plan -> Acquire -> Prepare -> Explore -> Model -> Deliver

Introduce myself and my project goals at the very beginning of my notebook walkthrough.
Summarize my findings at the beginning like I would for an Executive Summary. (Don't throw everything out that I learned from Storytelling) .
Walk Codeup Data Science Team through the analysis I did to answer my questions and that lead to my findings. (Visualize relationships and Document takeaways.)
Clearly call out the questions and answers I am analyzing as well as offer insights and recommendations based on my findings.
Reproduce My Project

You will need your own env file with database credentials along with all the necessary files listed below to run my final project notebook.

Read this README.md
Download the aquire.py, prepare.py, and final_report.ipynb files into your working directory
Add your own env file to your directory. (user, password, host)
Run the final_report.ipynb notebook