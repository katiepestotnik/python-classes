//dog class

class Dog {
    constructor(name, age = 0) {
        this.name = name
        this.age = age
    }
    bark() {
        console.log(`${this.name} barked woof woof`)
    }
}
Dog.age > 0
const klondike = new Dog('Klondike', 5)
console.log(klondike)
klondike.bark()