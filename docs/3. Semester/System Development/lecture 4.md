# Lecture 4
```mermaid
classDiagram

    class carRental {
        String name
        String age
        String carType
    }

    class Person {
        String name
        String age
  
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

    class Reservation {
        String reservationID
        Date startDate
        Date endDate
        cancelReservation()
    }

    class LeaseAgreement {
        String leaseID
        Date startDate
        Date endDate
        String insuranceType
        float deposit
        finalizeLease()
    }



    BusinessCustomer <|-- Customer : Inherits
    privateCustomer <|-- Customer : Inherits
    Customer <|-- Person : Inherits
    Employee <|-- Person : Inherits



```


!!! Question
    Start with event traces for the simple classes


```mermaid
graph TD
  %% Styling nodes
  style car fill:#f9f,stroke:#333,stroke-width:2px

  %% Subgraph for car
  subgraph car
    a1[Car Status]
    a2[Get Me]
  end

  %% Defining relations
  a1 --|getStatus| a1
  a1 --|getMe| a2

```

!!! Question
    Describe behavioural patterns from the event traces


!!! Question 
    Continue with the more complex classes


!!! Question
    If the behavioural pattern becomes too complicated, consider using the stepwise role or stepwise relation pattern – this introduces new classes


!!! Question 
    Make sure there are behavioural patterns that control sequence and some that don’t (structured/unstructured)


!!! Question 
    Add attributes to classes and events


!!! Question 
    Check the behavioural patterns against the class diagram

    