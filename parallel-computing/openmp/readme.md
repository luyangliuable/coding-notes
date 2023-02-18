# Programming with OpenMP

* Compiler directive for multitheraded programming.
* Easy to create threaded Fortran and C/C++ codes.
* Uses the fork-join model
* Work-sharing constructs

## Fork-Join Model
* **Master thread** spawns a **team of threads** as needed.

## Syntax

```c
#pragma omp construct [clause [clause]]
```

* Set the number of threads
    ```c
        set OMP_NUM_THREADS=4
    ```
    * Number of threads = number of processors?


* Print hello world in parallel

```c
#include <stdio.h>
#include <omp.h>

int main()
#pragma omp parallel
{
    int i;
    printf('Hello world');

    #pragma omp for
    for (i=0; i<6; i++)
        printf('Iter: %d\n', i);

    printf('Goodbye.');
}
```
