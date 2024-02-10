<?php

class Person {
    public $first_name;
    public $last_name;
    private $age;

    public function __construct($fname, $lname, $age) {
        $this->first_name = $fname;
        $this->last_name = $lname;
        $this->age = $age;
    }

    public function getAge() {
        return $this->age;
    }

    public function ageUp() {
        $this->age += 1;
    }

    public function getFullname() {
        return $this->first_name . " " . $this->last_name;
    }

    public function printFullname() {
        echo $this->first_name . " " . $this->last_name . "\n";
    }
}

class Main {
    public function __construct() {
        echo "Program starting.\n";
        $this->run();
        echo "Program ending.\n";
    }

    private function run() {
        echo "Creating person...\n";
        $person = new Person("John", "Doe", 30);
        echo "Person created.\n";

        echo "Name: " . $person->getFullname() . "\n";
        echo "Age: " . $person->getAge() . "\n";

        echo "Person has now birthday...\n";
        $person->ageUp();
        echo "New age: " . $person->getAge() . "\n";
    }
}

new Main();
