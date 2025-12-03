// This is a comment in Java script
// ; at the end in java script is optional

// This is equvivalent to print in python
console.log(2+2)
console.log(2-2)
console.log(2*2)
console.log(2/2)


var age = 65
console.log(age)
console.log(age*2)
age = age + 1
console.log(age)

// Dictionary
var xObject = {}
xObject ={
    name : "Pramod",
    age : 99 
}

console.log(xObject.name)
console.log(xObject["name"])
console.log(xObject.age)

console.log(10<10)
console.log(10==10)

// can reassign variable
var age = 12

if (age>=34){
    console.log("age is above 34")
    }
else{
    var a = "tres" 
    console.log("age is less than 34", a)
}

// function
function greet(){
    console.log("Hi How are you?")
}

// calling
greet()

// Json -> JS Object
var response ='{ "name" : "Pramod", "age" : 30, "cars" : ["Audi","BMW"]}'

var parseResponseJS = JSON.parse(response)

console.log(parseResponseJS.cars)
console.log(parseResponseJS["cars"][0])
console.log(parseResponseJS.cars[1])
console.log(parseResponseJS.name)

// JS Object -> JSON
var dict = {
    name : "Amit",
    age : 34
}

var JSONstr = JSON.stringify(dict)
console.log(JSONstr)

var xArray = ["apple", "orange", "banana"]
console.log(xArray[2])
