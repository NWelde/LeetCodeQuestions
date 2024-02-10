/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if (x < 0) {
        return false; // Negative numbers cannot be palindromes
    }

    let reversed = 0;
    let original = x;

    // Reverse the number
    while (x > 0) {
        const digit = x % 10;
        reversed = (reversed * 10) + digit;
        x = Math.floor(x / 10);
    }

    // Check if the reversed number is equal to the original number
    return original === reversed;
};

// Test cases
console.log(isPalindrome(121)); // Output: true
console.log(isPalindrome(-121)); // Output: false
console.log(isPalindrome(10)); // Output: false