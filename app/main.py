class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}

    for p_dict in people:
        Person(p_dict["name"], p_dict["age"])

    result_list = []
    for p_dict in people:
        current_person = Person.people[p_dict["name"]]

        if "wife" in p_dict and p_dict["wife"] is not None:
            partner_name = p_dict["wife"]
            current_person.wife = Person.people[partner_name]

        if "husband" in p_dict and p_dict["husband"] is not None:
            partner_name = p_dict["husband"]
            current_person.husband = Person.people[partner_name]

        result_list.append(current_person)

    return result_list
