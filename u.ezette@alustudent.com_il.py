#!/usr/bin/python3

class Assignment:
    def __init__(self, name, a_type, score, weight):
        self.name = name
        self.a_type = a_type  # FA for Formative, SA for Summative
        self.score = score
        self.weight = weight

    def weighted_score(self):
        return (self.score / 100) * self.weight


class GradeCalculator:
    def __init__(self):
        self.formative_assignments = []
        self.summative_assignments = []

    def add_assignment(self, assignment):
        if assignment.a_type == "FA":
            self.formative_assignments.append(assignment)
        elif assignment.a_type == "SA":
            self.summative_assignments.append(assignment)

    def calculate_totals(self):
        formative_total = sum(a.weighted_score() for a in self.formative_assignments)
        summative_total = sum(a.weighted_score() for a in self.summative_assignments)
        formative_weight = sum(a.weight for a in self.formative_assignments)
        summative_weight = sum(a.weight for a in self.summative_assignments)

        if formative_weight > 60 or summative_weight > 40:
            raise ValueError("Weights exceed allowed limits (60% for Formative, 40% for Summative).")

        return formative_total, summative_total

    def check_progression(self, formative_total, summative_total):
        passed_formative = formative_total >= 30
        passed_summative = summative_total >= 20
        
        if passed_formative and passed_summative:
            return "Congratulations! You have passed and progressed."
        elif not passed_formative and not passed_summative:
            return "Unfortunately, you have failed both sections and must retake the course."
        elif not passed_formative:
            return "You have failed the Formative section and must retake the course."
        else:
            return "You have failed the Summative section and must retake the course."

    def check_resubmission_eligibility(self):
        resubmissions = [a for a in self.formative_assignments if a.score < 50]
        if resubmissions:
            lowest_score = min(resubmissions, key=lambda a: a.score).score
            eligible_resubmissions = [a for a in resubmissions if a.score == lowest_score]
            return eligible_resubmissions
        return []

    def generate_transcript(self, order="ascending"):
        assignments = self.formative_assignments + self.summative_assignments
        assignments.sort(key=lambda a: a.score, reverse=(order == "descending"))

        transcript = f"Transcript Breakdown ({order.capitalize()} Order):\n"
        transcript += "Assignment          Type            Score(%)    Weight (%)\n"
        transcript += "-----------------------------------------------------------\n"

        for a in assignments:
            transcript += f"{a.name:<20} {a.a_type:<15} {a.score:<10} {a.weight}\n"

        transcript += "-----------------------------------------------------------"
        return transcript


# Interactive Application
calculator = GradeCalculator()

# Collect assignments from the user
num_assignments = int(input("Enter the number of assignments: "))

for i in range(num_assignments):
    print(f"\nAssignment {i + 1}")
    name = input("Enter assignment name: ")
    a_type = input("Enter assignment type (FA for Formative, SA for Summative): ").strip().upper()
    while a_type not in {"FA", "SA"}:
        print("Invalid type. Please enter FA for Formative or SA for Summative.")
        a_type = input("Enter assignment type (FA for Formative, SA for Summative): ").strip().upper()
    
    score = float(input("Enter assignment score (0-100): "))
    weight = float(input("Enter assignment weight (e.g., 15 for 15%): "))
    
    assignment = Assignment(name, a_type, score, weight)
    calculator.add_assignment(assignment)

# Calculate totals
try:
    formative_total, summative_total = calculator.calculate_totals()
    
    # Determine course progression
    progression_status = calculator.check_progression(formative_total, summative_total)
    print("\nCourse Progression:", progression_status)
    
    # Check resubmission eligibility
    eligible_resubmissions = calculator.check_resubmission_eligibility()
    if eligible_resubmissions:
        print("\nEligible for resubmission:")
        for resub in eligible_resubmissions:
            print(f"{resub.name} with a score of {resub.score}%")
    else:
        print("\nNo assignments eligible for resubmission.")
    
    # Generate and display transcript
    order = input("\nWould you like the transcript sorted in ascending or descending order? ").strip().lower()
    if order not in {"ascending", "descending"}:
        order = "ascending"  # default to ascending if invalid input
    print("\n" + calculator.generate_transcript(order=order))

except ValueError as e:
    print(f"Error: {e}")
