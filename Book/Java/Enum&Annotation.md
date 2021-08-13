# ENUM
#### Advice 1 : Use enum instead of int constants
1. Enum is _**constant variables**_ that mean we need to recompile the program if enum variable have been changed. The enum make program don't run incorrect state which we want.
2. Enum constants make readable string output.
3. Provide compile-time type safety.
4. Enum is singleton.
5. To associate data with enum constants, declare instance fields and write a constructor that takes the data and stores it in the fields.
6. Some behaviors associated with enum constants may need to be used only from within the class or package in which the enum is defined. Such behaviors are best implemented as private or package-private methods.
7. Declare abstract method if each enum have specific behavior.
Example :
```java
public enum Operation {  
	PLUS {publicdoubleapply(doublex,doubley){returnx+y;}}, 
	MINUS {public double apply(double x, double y){return x - y;}}, 
	TIMES {public double apply(double x, double y){return x * y;}}, 
	DIVIDE{public double apply(double x, double y){return x / y;}};

	public abstract double apply(double x, double y);
}
```

8. Enum types have an automatically generated valueOf(String) method that translates a constant’s name into the constant itself.
9. Don't use switch case or if else if behavior of function change follow enum respectively. Switches on enums are good for augmenting enum types with constant-specific behavior.
10. Use enums any time you need a set of constants whose members are known at compile time. 

#### Advice 2: Use instance field instead of ordinals
```java
// Abuse of ordinal to derive an associated value 
// DON'T DO THIS

 public enum Ensemble {
	 SOLO,   DUET,   TRIO, QUARTET, QUINTET,
     SEXTET, SEPTET, OCTET, NONET,  DECTET; 
     
	 public int numberOfMusicians() { return ordinal() + 1; }
}
```
1. Never derive a value associated with an enum from its ordinal; store it in an instance field instead
```java
public enum Ensemble {
	SOLO(1), DUET(2), TRIO(3), QUARTET(4), QUINTET(5),
    SEXTET(6), SEPTET(7), OCTET(8), DOUBLE_QUARTET(8),
    NONET(9), DECTET(10), TRIPLE_QUARTET(12); 

	private final int numberOfMusicians;  
	Ensemble(int size) { 
		this.numberOfMusicians = size; 
	} 
	public int numberOfMusicians() { 
		return numberOfMusicians; 
	}
}
```

#### Advice 3 : Use EnumSet instead of bit fields (STILL CONFUSE)
#### Advice 4 : Use EnumMap instead of ordinal indexing  (STILL CONFUSE)
#### Advice 5 : Emulate extensible enums with interfaces
```java
public interface Operation {
	double apply(double x, double y);
}

public enum BasicOperation implements Operation {
	PLUS("+") {
		@Override
		public double apply(double x, double y) {
			return x + y;
		}
	}
	// ....
	private final String symbol;
	BasicOperation(String symbol) {
		this.symbol = symbol;
	}
	
	@Override
	public String toString() {
		return this.symbol;
	}
}
```
1. While you cannot write an extensible enum type, you can emulate it by writing an interface to accompany a basic enum type that implements the interface

# ANNOTATION

#### Adi
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTk1Nzc5MzYwMywyMTI5MjIzNjIzLC0xMj
g3MzU4NjQ5LDE1NTMyNjQwOTgsLTIxMzg0MTM3ODNdfQ==
-->