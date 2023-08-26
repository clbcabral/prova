let n = 100;

for (let i = 1; i <= n; i++) {
    let mod3 = i % 3 == 0;
    let mod5 = i % 5 == 0;
    if (mod3 && mod5) {
        console.log('FizzBuzz');
    } else if (mod3 && !mod5) {
        console.log('Fizz');
    } else if (mod5 && !mod3) {
        console.log('Buzz');
    } else {
        console.log(i);
    }
}