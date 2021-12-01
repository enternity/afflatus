### Be Small Functions
- Easier for read and understand. Avoid bug.
### Do One Thing.
- Obviously.
### Block And Indenting
- Functions should not be large enough to hold nested structures. Therefore, the indent level of a function should not be greater than one or two. This, of course, makes the functions easier to read and understand.
### One Level of Abstraction per Function
- Mixing levels of abstraction within a function is always confusing. Readers may not be able to tell whether a particular expression is an essential concept or a detail.
### Switch Statements
```java
public Money calculatePay(Employee e) throws InvalidEmployeeType {
    switch (e.type) { 
        case COMMISSIONED:
            return calculateCommissionedPay(e); 
        case HOURLY:
            return calculateHourlyPay(e); 
        case SALARIED:
            return calculateSalariedPay(e); default:
        throw new InvalidEmployeeType(e.type); }
}
```
- Problem on function above:
  - It can be very large, when new employee types are added.
  - Do more one thing. Violated **SRP**(single responsibility principle)
  - Violated **OCP**(open-close principle)
  
> Solution : bury the ```switch``` statement in the basement of an **Abstract Factory** and never let anyone see it :smile: 

### Use Descriptive Names
- Don’t be afraid to spend time choosing a name.
- Be consistent in your names.

## Function Arguments
- The ideal number arguments of function is from 0 to 3.
- Arguments are even harder from a testing point of view.
- Try to avoid any monadic functions that don’t follow these forms, for example, ```void includeSetupPageInto(StringBuffer pageText)```. Using an output argument instead of a return value for a transformation is confusing
- Don't flag arguments. Passing a boolean into a function is a truly terrible practice.
- The two arguments in this case are ordered components of a single value!
- Think very carefully before creating a triad (three arguments).
- Argument objects. When a function seems to need more than two or three arguments, it is likely that some of those arguments ought to be wrapped into a class of their own.
- Argument list. ```public String format(String format, Object... args)```

### Have No Side Effects
- Side effects are lies. Your function promises to do one thing, but it also does other hidden things. Sometimes it will make unexpected changes to the variables of its own class.
- Anything that forces you to check the function signature is equivalent to a double-take. It’s a cognitive break and should be avoided.
- In general output arguments should be avoided. If your function must change the state of something, have it change the state of its owning object.
