#ifndef PERSON_H
#define PERSON_H

#include <string>
#include <iostream>

class Person {
private:
    std::string first_name;
    std::string last_name;
    int age;

public:
    // Constructor
    Person(std::string fname, std::string lname, int age) : first_name(fname), last_name(lname), age(age) {}

    // Getters
    int getAge() const {
        return age;
    }

    std::string getFullname() const {
        return first_name + " " + last_name;
    }

    // Methods
    void ageUp() {
        age += 1;
    }

    void printFullname() const {
        std::cout << first_name << " " << last_name << std::endl;
    }
};

#endif // PERSON_H
