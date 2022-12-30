let checking = [0,0,0,74,74,74,21,21,21,20,20,20,0,0,0];

function controlCar(scanArray) {
    let avg = [];
    
    let left = scanArray.slice(0, 8).reduce((a,b) => a + b);
    let center = scanArray[8]
    let right = scanArray.slice(9, 17).reduce((a,b) => a + b);
    
    avg = [ Math.round(left/8), center, Math.round(right/8) ];

    return avg.indexOf(Math.max(...avg)) - 1
}

console.log(controlCar(checking));
