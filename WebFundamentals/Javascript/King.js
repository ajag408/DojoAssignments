var amt = 0.01;
var totamt = 0;
for(var days = 1; days<=30; days++){
  totamt += amt;
  amt *= 2;
}
console.log(totamt);
