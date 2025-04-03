# Print an object of the `<intervention>` super-class

```r
## S3 method for class 'intervention'
print(x, ...)

## S3 method for class 'contact_intervention'
print(x, ...)

## S3 method for class 'rate_intervention'
print(x, ...)
```

## Arguments

- `x`: An object that inherits from the `<intervention>` class. For `print.contacts_intervention()`, an object of the `<contacts_intervention>` class. For `print.rate_intervention()`, an object of the `<rate_intervention>` class.
- `...`: Other parameters passed to `print()`.

## Returns

Invisibly returns the object `x`. Called for printing side-effects.

Print an object of the `<intervention>` super-class

Print objects of the `<contact_intervention>` class

Print objects of the `<rate_intervention>` class
