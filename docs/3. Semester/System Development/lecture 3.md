# Lecture 3





!!! Question

    Find candidates for structural relations between the classes in your event table - do this pair by pair



```mermaid
classDiagram

    class carRental {
        String name
        String age
        String carType
    }

    class Reservation {
        String reservationID
        Date startDate
        Date endDate
        cancelReservation()
    }

    class Person {
        String name
        String age
  
    }

    class LeaseAgreement {
        String leaseID
        Date startDate
        Date endDate
        String insuranceType
        float deposit
        finalizeLease()
    }

    class Customer {
        Boolean goodCustomer
        string driversLicense
        reserve()
        receiveGift()
    }

    class privateCustomer {
        Date rentalDate
    }
  
    class BusinessCustomer {
        String businessName
        String taxID
  
    }

    class Car {
        String model
        String type
        getStatus()
        needsMaintnance()
    }

    class Employee {
        Float Salary
        fire()
        giveGift(Customer)
    }






    BusinessCustomer <|-- Customer : Inherits
    privateCustomer <|-- Customer : Inherits
    Customer <|-- Person : Inherits
    Employee <|-- Person : Inherits
    LeaseAgreement <..> Customer : Relation
    LeaseAgreement <..> Car : Relation
    Reservation <..> Customer : Relation



``` 


!!! Question
     
     Explore if any of the patterns are relevant to your case - do this for each class

| Class Name       | Description      |
|------------------|------------------|
| carRental        ||
| Customer         |Hierarchy|
| privateCustomer  |Hierarchy|
| BusinessCustomer |Hierarchy|
| Car              ||
| Employee         |Hierarchy|
| Reservation      ||
| LeaseAgreement   ||
| person | Hierarchy, roles|

!!! Question
    
    Make a class diagram

See question 1!

!!! Question

    Look for opportunities to simplify and extend the class diagram

incorporate roles

```mermaid
classDiagram

    class carRental {
        String name
        String age
        String carType
    }

    class Reservation {
        String reservationID
        Date startDate
        Date endDate
        cancelReservation()
    }

    class Person {
        String name
        String age
  
    }

    class LeaseAgreement {
        String leaseID
        Date startDate
        Date endDate
        String insuranceType
        float deposit
        finalizeLease()
    }

    class Customer {
        Boolean goodCustomer
        string driversLicense
        reserve()
        receiveGift()
    }



    class Car {
        String model
        String type
        getStatus()
        needsMaintnance()
    }

    class Employee {
        Float Salary
        fire()
        giveGift(Customer)
    }

    class Roles {

    }
    
    class privateCustomer {
        Date rentalDate
    }
  
    class BusinessCustomer {
        String businessName
        String taxID
  
    }







    Roles <|-- Employee
    Roles <|-- Customer
    Person <|-- Roles
    BusinessCustomer --|> Customer : Inherits
    privateCustomer --|> Customer : Inherits
    LeaseAgreement --> Customer



``` 