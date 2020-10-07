## Task
Create a script which involves array manipulation described as below.

I have an array of n elements.
I have to reduce the array to length one by deleting the element present
at the location decided by sum of first and last element in each reduction cycle.
If sum > len(array) , reiterate the array.

Eg: original array=`[1,3,2,4,6]`.
sum(1+6) = 7.
Element present at 7th place is 3.So delete 3.
Now the reduced array is `[1,2,4,6]`.
sum(1,6) = 7.
Element present at 7th place is 4.So delete 4.
Now the reduced array is `[1,2,6]`.
sum(1,6) = 7.
Element present at 7th place is 1.So delete 1.
Now the reduced array is `[2,6]`.
sum(2,6) = 8.
Element present at 7th place is 6.So delete 6.
Now the reduced array is `[2]`.

Expected output: `[2]`

Verified inputs:
`[1, 3, 2, 4, 6]`,
`[8, 2, 4, 8]`,
`[-1, -3, -2, -4, -6]`,
`[-1, -3, 2, 4, 6]`,
`[1, -3, 2, -4, -6]`,
`[1, -3, 2, -4, -6.0]`





 
