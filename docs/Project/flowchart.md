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
