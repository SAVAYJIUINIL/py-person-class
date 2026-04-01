class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}

    [Person(p_dict["name"], p_dict["age"]) for p_dict in people]

    for p_dict in people:
        current_person = Person.people[p_dict["name"]]

        wife_name = p_dict.get("wife")
        if wife_name:
            current_person.wife = Person.people[wife_name]

        husband_name = p_dict.get("husband")
        if husband_name:
            current_person.husband = Person.people[husband_name]

    return [Person.people[p_dict["name"]] for p_dict in people]
