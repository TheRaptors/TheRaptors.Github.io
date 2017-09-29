alert('Js Files')

// name = 'Ghost'   全局变量
// var name = 'Ghost'   局部变量

function Foo(name){
    var arg = arguments[1]
    console.log(name)
    console.log(arg)
}

/*
function Foo(){
    var name = arguments[0]
    var arg = arguments[1]
    console.log(name)
    console.log(arg)
}

*/
Foo('Ghost','Sadan')