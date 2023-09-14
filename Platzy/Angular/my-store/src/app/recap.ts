const username: string = 'Carlos';
const sum = (a : number, b : number) =>{
    return a + b;
}
sum(2,4)

class Person{
    age: number;
    lastname: string;

    constructor(age:number, lastname: string){
        this.age = age;
        this.lastname = lastname;
    }
}

const carlos = new Person(32, 'Alvarado');
