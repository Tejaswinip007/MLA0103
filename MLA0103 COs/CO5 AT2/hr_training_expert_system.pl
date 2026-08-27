% ============================================
% HR TRAINING RECOMMENDATION EXPERT SYSTEM
% Knowledge Base - Employee Facts
% ============================================

% Employee names
employee(ravi).
employee(priya).
employee(arun).
employee(sneha).
employee(karthik).
employee(divya).

% Job roles
job_role(ravi, developer).
job_role(priya, developer).
job_role(arun, data_analyst).
job_role(sneha, hr_executive).
job_role(karthik, manager).
job_role(divya, software_tester).

% Technical skills
skill(ravi, python).
skill(priya, java).
skill(arun, excel).
skill(sneha, recruitment).
skill(karthik, leadership).
skill(divya, manual_testing).

% Performance levels
performance(ravi, average).
performance(priya, good).
performance(arun, average).
performance(sneha, average).
performance(karthik, good).
performance(divya, poor).

% Experience levels
experience(ravi, junior).
experience(priya, intermediate).
experience(arun, junior).
experience(sneha, junior).
experience(karthik, senior).
experience(divya, junior).

% Competency gaps
competency_gap(ravi, machine_learning).
competency_gap(priya, cloud_computing).
competency_gap(arun, sql).
competency_gap(sneha, communication).
competency_gap(karthik, strategic_management).
competency_gap(divya, automation_testing).

% ============================================
% AVAILABLE TRAINING PROGRAMS
% ============================================

training(machine_learning_fundamentals).
training(cloud_computing_training).
training(sql_database_training).
training(communication_skills_training).
training(strategic_leadership_training).
training(automation_testing_training).
training(performance_improvement_training).

% ============================================
% TRAINING RECOMMENDATION RULES
% ============================================

% Rule 1: Machine Learning Training
recommend_training(Employee, machine_learning_fundamentals) :-
    job_role(Employee, developer),
    competency_gap(Employee, machine_learning).

% Rule 2: Cloud Computing Training
recommend_training(Employee, cloud_computing_training) :-
    job_role(Employee, developer),
    competency_gap(Employee, cloud_computing).

% Rule 3: SQL Database Training
recommend_training(Employee, sql_database_training) :-
    job_role(Employee, data_analyst),
    competency_gap(Employee, sql).

% Rule 4: Communication Skills Training
recommend_training(Employee, communication_skills_training) :-
    job_role(Employee, hr_executive),
    competency_gap(Employee, communication).

% Rule 5: Strategic Leadership Training
recommend_training(Employee, strategic_leadership_training) :-
    job_role(Employee, manager),
    competency_gap(Employee, strategic_management).

% Rule 6: Automation Testing Training
recommend_training(Employee, automation_testing_training) :-
    job_role(Employee, software_tester),
    competency_gap(Employee, automation_testing).

% Rule 7: Performance Improvement Training
recommend_training(Employee, performance_improvement_training) :-
    performance(Employee, poor).

% ============================================
% EXPLANATION MODULE
% ============================================

explain_recommendation(Employee, machine_learning_fundamentals,
    'Recommended because the employee is a developer with a Machine Learning competency gap.') :-
    job_role(Employee, developer),
    competency_gap(Employee, machine_learning).

explain_recommendation(Employee, cloud_computing_training,
    'Recommended because the employee is a developer with a Cloud Computing competency gap.') :-
    job_role(Employee, developer),
    competency_gap(Employee, cloud_computing).

explain_recommendation(Employee, sql_database_training,
    'Recommended because the employee is a Data Analyst with an SQL competency gap.') :-
    job_role(Employee, data_analyst),
    competency_gap(Employee, sql).

explain_recommendation(Employee, communication_skills_training,
    'Recommended because the employee is an HR Executive with a Communication competency gap.') :-
    job_role(Employee, hr_executive),
    competency_gap(Employee, communication).

explain_recommendation(Employee, strategic_leadership_training,
    'Recommended because the employee is a Manager with a Strategic Management competency gap.') :-
    job_role(Employee, manager),
    competency_gap(Employee, strategic_management).

explain_recommendation(Employee, automation_testing_training,
    'Recommended because the employee is a Software Tester with an Automation Testing competency gap.') :-
    job_role(Employee, software_tester),
    competency_gap(Employee, automation_testing).

explain_recommendation(Employee, performance_improvement_training,
    'Recommended because the employee has poor performance and requires performance improvement training.') :-
    performance(Employee, poor).

% ============================================
% COMPLETE TRAINING RECOMMENDATION
% ============================================

get_recommendation(Employee, Training, Reason) :-
    recommend_training(Employee, Training),
    explain_recommendation(Employee, Training, Reason).

% ============================================
% FORWARD CHAINING DEMONSTRATION
% ============================================

forward_chain :-
    employee(Employee),
    recommend_training(Employee, Training),
    write('Employee: '),
    write(Employee),
    write(' -> Recommended Training: '),
    write(Training),
    nl,
    fail.

forward_chain.

% ============================================
% BACKWARD CHAINING DEMONSTRATION
% ============================================

backward_chain(Employee, Training) :-
    recommend_training(Employee, Training).

% ============================================
% TEST CASE EXECUTION WITH PASS STATUS
% ============================================

run_test(Employee) :-
    get_recommendation(Employee, Training, Reason),
    write('Employee: '),
    write(Employee), nl,
    write('Recommended Training: '),
    write(Training), nl,
    write('Reason: '),
    write(Reason), nl,
    write('Status: PASS'), nl.