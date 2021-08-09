# BASIC CONCEPT
|Term|Definition|
|:---|:---|
|_Join points_|is a _**well-defined**_ point during the execution of application. Eg: call to a method, the method invocation itself, class initialization, and object instantiation.|
|_Advice_|The code that is executed at a particular join point is the advice, defined by a method in class. There are many type of advice, such as before which executes before join point, after which executes after join point|
|_Point cuts_|is a collection of join points that we use to define when advice should be executed. By creating point cuts, we gain fine-grained control over how you apply advice to the components in your application|
|_Aspect_|is the combination of advice and point cuts encapsulated in a class. This combination result in a defination|
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3MjQ4MjUxMDVdfQ==
-->