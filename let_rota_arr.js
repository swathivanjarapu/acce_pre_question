let arr=[2,4,5,6,1]
d=4
for(let i=0;i<d;i++){
    let a=arr.shift()
    arr.push(a)
}
console.log(arr)