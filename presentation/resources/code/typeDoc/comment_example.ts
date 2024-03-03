/**
 * Calculates the n-th number of the fibonacci sequence
 * @param n The number of the fibonacci sequence to calculate
 * @returns The n-th number of the fibonacci sequence
 * 
 * @see {@link https://en.wikipedia.org/wiki/Fibonacci_number | Fibonacci number}
 * @throws {TypeError} If n is not a positive integer
 * @throws {RangeError} If n is greater than 1476
 * 
 * @example
 * fibonacci(0); // 0
 * fibonacci(1); // 1
 * fibonacci(2); // 1
 * fibonacci(3); // 2
 * fibonacci(4); // 3
 */
declare function fibonacci(n: number): number;