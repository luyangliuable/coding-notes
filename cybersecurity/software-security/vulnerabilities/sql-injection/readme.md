# SQL Injection

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [SQL Injection](#sql-injection)
    - [Bypass Method: Injection into Numeric Data](#bypass-method-injection-into-numeric-data)
    - [Bypass Method: Second-order SQL Injection](#bypass-method-second-order-sql-injection)
    - [Countermeasures](#countermeasures)

<!-- markdown-toc end -->


SQL Injection is a code injection technique that is used to bypass data-driven applications. It occurs often when malicious sql query is injected into entry field for execution.

The root cause is SQL treating user data as code.

* There are lots of variants to SQLi exploits
    * Bypassing simple SQLi countermeasures such as character escaping filters.


## Bypass Method: Injection into Numeric Data
* The application accept user input data.
* Numeric data can be passed to database without ' quotes e.g. For vulnerable code like.

```php
$1QueryString = " SELECT * FROM customers WHERE customerID =" . $customerID;
```
* Attacker input 

* No need for quote symbol.
```SQL
123 or 1=1 -
```

## Bypass Method: Second-order SQL Injection

* ` character is used to escape query to execute maliciously injected code.
* A second order vulnerability for string may still be exploitable.

* E.g. Injection code
```sql
bob` OR 1=1 -- ;
```

* Phase 1: No code injection execution in phase 1. Only store code injection. 
* Phase 2: Web app retrieves user's name which is malicious code from database into a variable $username resulting in value:
```sql
$username is bob` OR 5=5 -- ;
```
* No escaping is performed by application since user name is retrieved from database and not from user input.

* Executed Code
```sql
SELECT password 
FROM accounts 
WHERE username = `bob` OR 5=5 --
```

## Countermeasures
* Preferred: Parameterized queries
  * Prepare statements
  * Disallow treating user data as code.
  
* Input validation
  * White list appropriate values.
  * Tricky and not foolproof to implement
* Escaping untrusted inputs so it will not be treated as command.
  * Trick and not foolproof to implement
  

## Parameterized Queries
* Any malicious code being injected will be treated as data instead of code.

1. Pass desired SQL values into placeholders (? Symbols)
```sql
$stmt = $mysqli->prepare("SELECT District FROM City WHERE Name=?");
```

2. Pass data values inserted by user entry fields into placeholders.
```sql
$stmt->bind_param("bob", "$name");
```

3. Execute to get result
```sql
$stmt->execute();
$result->$stmt->get_result();
$stmt->close();
```

* Use Parameterized Queries for every single SQL query
  * To prevent malicious input stored that are executed later
* Easier to misjudge which data is user-controllable.
* Remember to use parameterized query for every data item.
  * Even a single concatenated parameter can be used for injection!
  
  
## Limitations of Parameterized Queries?
* Tables and column names cannot be parameterized. They are user controlled.
  * Need to use whitelist for databases/column names
  * Use strict **validation restriction** (allow only alphanumeric characters, reject spaces and limit length)
* Other parts of query code cannot be parameterized
  * Like ASC and DESC in order by
  * White list options: ASC and DESC
