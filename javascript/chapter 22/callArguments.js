const persons = {
    fullName: function(city, country) {
    return this.firstName + " " + this.lastName + "," + city + "," + country;
    }
}
const persons1 = {
    firstName:"John",
    lastName: "Doe"
}
let result = persons.fullName.call(persons1, "Oslo", "Norway");
console.log(result);		//John Doe,Oslo,Norway