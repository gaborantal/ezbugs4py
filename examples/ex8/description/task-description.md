## PrettyPrint class

Create a **PrettyPrint** class that implements the following:

- Its constructor expects 1 parameter, which can be any kind of data, and its default value is an empty string.
- The constructor saves the value of the parameter to the instance's **_prefix** attribute.
    - This attribute has a getter and setter named **prefix**.
- The class includes a **get** method, which expects any parameter.
- The **get** method returns a string based on the type of the parameter and the constructor's parameter. Its
  functionality is as follows:
    - The method checks the type of its parameter, and if it is one of the following, the returned strings include the
      following:
        - Types to check: None, int, float, str, list, dict
        - Returned values: <no returned text!>, "(integer)", "(float)", "(string)", "(list object)", "(dictionary)"
        - If none of these types is true for the parameter, then the method should return the text "(unknown)" for the
          type.
    - Additionally, the method appends the constructor parameter in front of the returned type value as text and
    - appends the value of the parameter passed to the method as text after the type value.
    - Separate these three (or two in the case of None) text data with a space!
    - See the examples for clarification!
- The **get** method invokes a class method for determining the textual value of each type, and these methods are named
  as follows:
    - **get_NoneType**, **get_int**, **get_float**, **get_str**, **get_list**, **get_dict**
