public class Person {
    private String first_name;
    private String last_name;
    private int age; // Using private access to encapsulate the age property

    // Constructor
    public Person(String fname, String lname, int age) {
        this.first_name = fname;
        this.last_name = lname;
        this.age = age;
    }

    // Getter for age
    public int getAge() {
        return this.age;
    }

    // Method to increment age
    public void ageUp() {
        this.age += 1;
    }

    // Getter for full name
    public String getFullname() {
        return this.first_name + " " + this.last_name;
    }

    // Method to print full name
    public void printFullname() {
        System.out.println(this.first_name + " " + this.last_name);
    }
}
