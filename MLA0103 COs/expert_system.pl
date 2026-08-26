% ============================================
% STUDENT ACADEMIC ADVISORY EXPERT SYSTEM
% ============================================

% Student facts
student(student1).
student(student2).
student(student3).
student(student4).
student(student5).

% Attendance facts
attendance(student1, low).
attendance(student2, high).
attendance(student3, medium).
attendance(student4, low).
attendance(student5, high).

% Internal marks facts
internal_marks(student1, low).
internal_marks(student2, high).
internal_marks(student3, medium).
internal_marks(student4, low).
internal_marks(student5, medium).

% Assignment performance facts
assignment_performance(student1, poor).
assignment_performance(student2, excellent).
assignment_performance(student3, good).
assignment_performance(student4, poor).
assignment_performance(student5, good).

% Learning difficulty facts
learning_difficulty(student1, yes).
learning_difficulty(student2, no).
learning_difficulty(student3, no).
learning_difficulty(student4, yes).
learning_difficulty(student5, no).

% Previous academic performance facts
previous_performance(student1, poor).
previous_performance(student2, excellent).
previous_performance(student3, average).
previous_performance(student4, poor).
previous_performance(student5, good).

% ============================================
% PRODUCTION RULES
% ============================================

% Rule 1: Low attendance creates attendance risk
academic_status(Student, attendance_risk) :-
    attendance(Student, low).

% Rule 2: Low internal marks create academic risk
academic_status(Student, academic_risk) :-
    internal_marks(Student, low).

% Rule 3: Poor assignments create assignment risk
academic_status(Student, assignment_risk) :-
    assignment_performance(Student, poor).

% Rule 4: Learning difficulty requires support
academic_status(Student, learning_support_needed) :-
    learning_difficulty(Student, yes).

% Rule 5: Poor previous performance and low marks create high risk
academic_status(Student, high_risk) :-
    previous_performance(Student, poor),
    internal_marks(Student, low).

% Rule 6: Low attendance, low marks, and poor assignments create critical risk
academic_status(Student, critical_risk) :-
    attendance(Student, low),
    internal_marks(Student, low),
    assignment_performance(Student, poor).

% Rule 7: High attendance, high marks, and excellent assignments indicate good progress
academic_status(Student, good_progress) :-
    attendance(Student, high),
    internal_marks(Student, high),
    assignment_performance(Student, excellent).

% Rule 8: Medium attendance and medium marks indicate moderate progress
academic_status(Student, moderate_progress) :-
    attendance(Student, medium),
    internal_marks(Student, medium).

    % ============================================
% RECOMMENDATION RULES
% ============================================

% Low marks require remedial classes
recommendation(Student, attend_remedial_classes) :-
    academic_status(Student, academic_risk).

% Low attendance requires improvement
recommendation(Student, improve_attendance) :-
    academic_status(Student, attendance_risk).

% Poor assignments require regular completion
recommendation(Student, complete_assignments_regularly) :-
    academic_status(Student, assignment_risk).

% Learning difficulty requires additional support
recommendation(Student, provide_learning_support) :-
    academic_status(Student, learning_support_needed).

% High-risk students should meet an academic counselor
recommendation(Student, meet_academic_counselor) :-
    academic_status(Student, high_risk).

% Critical-risk students need immediate intervention
recommendation(Student, immediate_academic_intervention) :-
    academic_status(Student, critical_risk).

% Students with good progress should continue their performance
recommendation(Student, continue_current_performance) :-
    academic_status(Student, good_progress).

% Students with moderate progress require regular monitoring
recommendation(Student, regular_progress_monitoring) :-
    academic_status(Student, moderate_progress).

% ============================================
% DISPLAY STUDENT DETAILS
% ============================================

show_student(Student) :-
    student(Student),

    write('Student: '),
    writeln(Student),

    attendance(Student, Attendance),
    write('Attendance: '),
    writeln(Attendance),

    internal_marks(Student, Marks),
    write('Internal Marks: '),
    writeln(Marks),

    assignment_performance(Student, Assignment),
    write('Assignment Performance: '),
    writeln(Assignment),

    learning_difficulty(Student, Difficulty),
    write('Learning Difficulty: '),
    writeln(Difficulty),

    previous_performance(Student, Previous),
    write('Previous Performance: '),
    writeln(Previous).


% ============================================
% DISPLAY ACADEMIC ANALYSIS
% ============================================

show_diagnosis(Student) :-
    student(Student),

    nl,
    writeln('--- Academic Analysis ---'),

    forall(
        academic_status(Student, Status),
        (
            write('Academic Status: '),
            writeln(Status)
        )
    ),

    nl,
    writeln('--- Recommendations ---'),

    forall(
        recommendation(Student, Advice),
        (
            write('Recommendation: '),
            writeln(Advice)
        )
    ).


% ============================================
% COMPLETE STUDENT ANALYSIS
% ============================================

analyze(Student) :-
    show_student(Student),
    show_diagnosis(Student).

% ============================================
% MAIN PROGRAM
% ============================================

start :-
    nl,
    writeln('========================================='),
    writeln(' STUDENT ACADEMIC ADVISORY EXPERT SYSTEM '),
    writeln('========================================='),
    writeln('Available Students: student1 to student5'),
    nl,
    write('Enter student name: '),
    read(Student),

    (
        student(Student) ->
            nl,
            analyze(Student)
        ;
            writeln('Student not found!')
    ).

    % ============================================
% BACKWARD CHAINING DEMONSTRATION
% ============================================

diagnose(Student, Conclusion) :-
    recommendation(Student, Conclusion).

% ============================================
% FORWARD CHAINING IMPLEMENTATION
% ============================================

:- dynamic known/1.

% Add a derived fact only if it is not already known
add_if_new(Fact) :-
    known(Fact), !.

add_if_new(Fact) :-
    assertz(known(Fact)),
    write('Derived fact: '),
    writeln(Fact).


% Forward chaining process
forward_chain :-
    forall(
        academic_status(Student, Status),
        add_if_new(academic_status(Student, Status))
    ),
    forall(
        recommendation(Student, Advice),
        add_if_new(recommendation(Student, Advice))
    ),

    nl,
    writeln('Forward chaining completed.').