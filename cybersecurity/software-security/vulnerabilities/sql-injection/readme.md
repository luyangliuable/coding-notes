# SQL Injection

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [SQL Injection](#sql-injection)

<!-- markdown-toc end -->


SQL Injection is a code injection technique that is used to bypass data-driven applications. It occurs often when malicious sql query is injected into entry field for execution.

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

