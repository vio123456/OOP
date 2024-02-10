// In an actual Dart environment, use the following import.
import 'person.dart';

void main() {
  print("Program starting.");
  createAndManagePerson();
  print("Program ending.");
}

void createAndManagePerson() {
  print("Creating person...");
  var person = Person("John", "Doe", 30); // Assuming Person class is defined in person.dart
  print("Person created.");

  print("Name: ${person.getFullname()}");
  print("Age: ${person.getAge()}");

  print("Person has now birthday...");
  person.ageUp();
  print("New age: ${person.getAge()}");
}
