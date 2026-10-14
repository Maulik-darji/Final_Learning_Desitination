class pen{
    String color;
    String type;
    public void write(){
        System.out.println("Writing Something");
    }

    public void printColor(){
        System.out.println(this.color);
    }

    public void printType(){
        System.out.println(this.type);
    }

}

class Student{
    String name;
    int age;
    public void printName(){
        System.out.println(this.name);
    }
    public void printAge(){
        System.out.println(this.age);
    }

    public void printStudentInfo(){
        System.out.println(this.name);
        System.out.println(this.age);
    }
    //parameterized constructor
    Student(String name, int age){
        this.name = name;
        this.age = age;
    }

    //Copy Constructor
    Student(Student other){
        this.name = other.name;
        this.age = other.age;
    }
}

public class main{
    public static void main(String[] args){
        // pen pen1 = new pen();
        // pen1.color = "Blue";
        // pen1.type = "Ballpoint";
        // pen1.write();

        // // Object 2
        // pen pen2 = new pen();
        // pen2.color = "Black";
        // pen2.type = "Gel";
        
        // pen1.printColor();
        // pen2.printColor();

        // print("Using Functin printStudentInfo")
        Student s1 = new Student("Maulik", 21);
        // s1.printStudentInfo();

        Student s2 = new Student(s1);
        s1.printName();
        s1.printAge();

        System.out.println("------");
        s2.printName();
        s2.printAge();
    }
}