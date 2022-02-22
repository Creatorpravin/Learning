"use strict"

function checkPalindrome(str) {
    if (typeof str === 'string'){
    // find the length of a string
    const len = str.length;

    // loop through half of the string
    for (let i = 0; i < len / 2; i++) {

        // check if first and last string are same
        if (str[i] !== str[len - 1 - i]) {
            return 'It is not a palindrome';
        }
    }
    return 'It is a palindrome';
}else{
   return str,"Not a string";
}
}


// call the function
console.log(checkPalindrome("redivider"));
console.log(checkPalindrome(5));