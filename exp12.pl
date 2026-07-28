disease(fever,viral_fever).
disease(cough,common_cold).
disease(headache,migraine).
disease(stomach_pain,gastritis).
disease(chest_pain,heart_problem).

medicine(viral_fever,paracetamol).
medicine(common_cold,cetirizine).
medicine(migraine,painkiller).
medicine(gastritis,antacid).
medicine(heart_problem,consult_cardiologist).

diagnosis(Symptom):-
    disease(Symptom,Disease),
    medicine(Disease,Medicine),
    write('Disease : '),write(Disease),nl,
    write('Medicine: '),write(Medicine),nl.