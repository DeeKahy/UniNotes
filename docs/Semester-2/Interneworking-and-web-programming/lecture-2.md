## JS functions & objects
function normal "funktions erklæring"
```js
function name(para){
    console.log(para);
}
name("diego");
```
function let "funktions udtryk (anonymt)"

prints entire function in this case change name to function call to run function
```js
let name = function (para){
    console.log(para);
}
console.log(name);
```
arrow function "pile-funktioner"
```js
let name = (para)=>{
    console.log(para);
}
name("diego");
```
if one param paranthesis optional will return if only statement.
```js
const increment = a => a+1;

console.log(increment(5));
```

call-back
```js
document.addEventListener("click",doMyStuff);
```

object serialisering is making an object into a flad (bit streng)