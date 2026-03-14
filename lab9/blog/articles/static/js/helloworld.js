

var groupmates = [
{
    "name": "Василий",
    "group": "bst2252",
    "age": 25,
    "marks": [4, 3, 5, 5, 4]
},
{
    "name": "Анна",
    "group": "bst2254",
    "age": 24,
    "marks": [5, 5, 3, 4, 4]
},
{
    "name": "Георгий",
    "group": "bst2252",
    "age": 22,
    "marks": [3, 5, 4, 3, 5]
},
{
    "name": "Валентина",
    "group": "bst2254",
    "age": 25,
    "marks": [5, 5, 5, 4, 5]
},
{
    "name": "Афанасий",
    "group": "bst2251",
    "age": 24,
    "marks": [4, 4, 3, 4, 5]
}
];

console.log(groupmates);

var rpad = function(str, length) {
    str = str.toString();
    while (str.length < length) str += " ";
    return str;
};

var printStudents = function(students) {
    console.log(rpad("Имя студента",15), rpad("Группа",8), rpad("Возраст",8), rpad("Оценки",20));
    for (var i=0; i<students.length; i++) {
        console.log(rpad(students[i].name,15), rpad(students[i].group,8), rpad(students[i].age,8), rpad(students[i].marks,20));
    }
};
printStudents(groupmates);

var filterByGroup = function(students, group) {
    return students.filter(function(student) {
        return student.group === group;
    });
};

console.log(filterByGroup(groupmates, "bst2254"));