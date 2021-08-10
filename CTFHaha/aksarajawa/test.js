const read = (s) => s.reduce((a, b) => (a<<1)+b);
function argue(a, b, c){
    console.log((![]+[])[b-2*a]);
    console.log(({}+[]).split(' ')[+[]][c-a]);
    console.log(({}+[]).split(' ')[+[]][b-c]);
}

for (let i = 0; i < 26; i++){
    console.log((![]+[])[i])
}