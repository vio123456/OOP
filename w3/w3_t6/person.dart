class Person {
  String firstName;
  String lastName;
  int _age; // Private property with underscore

  Person(this.firstName, this.lastName, this._age);

  int getAge() => _age;

  void ageUp() => _age += 1;

  String getFullname() => "$firstName $lastName";

  void printFullname() => print("$firstName $lastName");
}
