const Person = require('./person');

class Main {
  constructor() {
    console.log("Program starting.");
    this.run();
    console.log("Program ending.");
  }

  run() {
    console.log("Creating person...");
    // In a real-world scenario, you might get these values from user input or another source
    const person = new Person("John", "Doe", 30);
    console.log("Person created.");

    console.log(`Name: ${person.getFullname()}`);
    console.log(`Age: ${person.getAge()}`);

    console.log("Person has now birthday...");
    person.ageUp();
    console.log(`New age: ${person.getAge()}`);
  }
}

new Main(); // Instantiating the Main class object to start the program
