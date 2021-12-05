# Problem In MicroServices 
- For each service need to authenticate and authorize by them self. If we use common service. The cost of maintain is kind of expensive and problem with different languages in micro services.
- Services only focus do them job, if build logic for authorization & authentication increase time to develop and increase complexity. 

# Authentication 
- [JWT](https://jwt.io/introduction),  [Opaque Token](https://apim.docs.wso2.com/en/3.0.0/learn/api-security/oauth2/access-token-types/opaque-tokens/)

> Refer : [different JWT & Opaque Token](https://medium.com/@piyumimdasanayaka/json-web-token-jwt-vs-opaque-token-984791a3e715)

- [OAuth2](https://oauth.net/2/) (delegate authentication & authorization)

# Access Control 
1. [Access control list](https://www.geeksforgeeks.org/access-lists-acl/)
- Define the matrix of access control. Each role will have permission on each action. (same thing ```chmod``` ). When the system growth up, it's very hard for manage because the matrix of access controls will be too big and complexity. So currently, Access control list is not popular.
2. [Role-Based Access Control](https://auth0.com/docs/authorization/rbac/) (RBAC)

3. [Policy-Based Access Control](https://developer.okta.com/books/api-security/authz/attribute-based/#authz-attribute-based) (PBAC)