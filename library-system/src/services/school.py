class School:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def display_all(self):
        for person in self.people:
            print(person.display_info())

    def __len__(self):
        return len(self.people)

    def __str__(self):
        return f"School with {len(self.people)} people"
