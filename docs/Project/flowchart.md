``` mermaid
graph TD
    A[User] -- Enters login credentials --> B((Login System))
    B -- Verifies credentials --> C{Authenticated?}
    C -- No --> E(Error Message)
    C -- Yes --> Dashboard[User Dashboard]
    E --> B
    Dashboard --> S((Suggestions))

    S --> plist[Display list&price]
    S --> recipes
    S --> more[base stats]

    Dashboard -.-> Exp[Experation Date Page]
    Dashboard -.-> Recipes
    Dashboard -.-> QuickAdd
    Dashboard -.-> Shopping[Shopping List Page]

    Shopping --> price[estimated price]
    Recipes -.-> search[search makable recipes]
    Recipes --> display
    search -.-> |if found| missing[make list of missing items]
    missing --> price
    Shopping --> list

    QuickAdd --> addProduct

    Exp -.-> addProduct[add item]
    Exp -.-> rem[Remove items]

    rem -.-> eaten
    rem -.-> discarded

    addProduct -.-> barcode[add barcode]
    addProduct -.-> manual[add manually]

```


``` mermaid
graph TB
  A[NodeJS App] --> B[Login System]
  B --> C[/Dashboard]
  C --> D[Home]
  D --> DA[Display Waste Info]
  D --> DB[Display Expiring Items]
  D --> DC[Display Possible Recipes]
  C --> E[Item Tracker]
  E --> EA[Display Inventory]
  E --> EB[Add Items & Expiry Dates]
  C --> F[Statistics]
  F --> FA[Display Food Waste]
  F --> FB[Display CO2 Waste]
  C --> G[Recipes]
  G --> GA[Show Recipes Sorted By Available Items]
  C --> H[Shopping List]
  H --> HA[Create Shopping List]
  H --> HB[Estimate Price via API]
  C --> I[Settings]
  C --> J[Logout]

```
