# ROTATE MATRIX:
## Install: 

Install it using:

             pip install rotate-matrix

Rotate any matrix/multi-dimentional array of any type, either clockwise or anti-clockwise instantly. 

Contains two functions:

### 1)  clockwise(): Takes l as parameter which is of type list, and pases the clockwised rotated version list l.
            import rotate_matrix
            l = [[1,2,4,3],[7,8,5,6],[8,6,5,4]]
            print(rotate_matrix.clockwise(l))
            
 ### Output:
            [(3, 6, 4), (4, 5, 5), (2, 8, 6), (1, 7, 8)]

### 2) anti-clockwise(): Takes l as parameter which is of type list, and passes the anti-clockwise rotated version of list l.
             import rotate_matrix
            l = [[1,2,4,3],[7,8,5,6],[8,6,5,4]]
            print(rotate_matrix.anti_clockwise(l))
### Output:
           [(8, 7, 1), (6, 8, 2), (5, 5, 4), (4, 6, 3)]





