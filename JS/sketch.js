
let alphabetStr = "\n ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzéèàù§\"#$%&'()*+,-./0123456789:;<=>?@¤";
let alphabet = alphabetStr.split('');



function chiffre(text, key) {
  
  var aKey = key.toString().split('');   // Transform the key and the text in array
  var aText = text.split('');
  
  for(let i = 0; i < aText.length; i++) { // Replace each character by a number
	let done;
	for(let j = 0; j < alphabet.length; j++) {
		if(aText[i] == alphabet[j]) {
			aText[i] = j + 1;
			done = 1;
			break;
		}
	}
	if(!done) {
		console.log(aText[i]);
		aText[i] = 500; // If the caracter wasn't found
		
	}
    
  }
  
  
  
  let k = 1;
  for(let i = 0; aKey.length < aText.length; i++) { // Adjust the key size to be as long as the text ...
    if(i > aKey.length) {
      i = 0;
      k++;    
    }
    aKey.push(aKey[i] / k);
	aKey[i] *= 1;
  }
  
  while(aKey.length > aText.length) aText.push(0); // Or adjust the text
  
  let finalC = '';
  
  for(let i = 0; i < aKey.length; i++){
    if(aText[i] == 0) break;
    aText[i] += (3 * aKey[i]) % 4;  // Add 3 times the digit of the key to the text
    
    aText[i] = aText[i].toString();
    while(aText[i].length < 3) aText[i] = '0' + aText[i]; // Make each number made of 3 by adding 0
    
    finalC += aText[i] ;
  
  }

  let size = text.length.toString();
  while(size.length < 3) size = '0' + size;
  finalC = size + finalC;
  
  return finalC;
}





function dechiffre(text, key) {
	
  key = key.toString();

  let chiffred = text.replace(/X/g,'');
  
  let tabChiffre = chiffred.match(/.{1,3}/g); // Separate the text in array each 4
  let tabKey = key.toString().split('');
  
  let size = parseInt(tabChiffre[0], 10);
  
  tabChiffre.splice(0, 1);
  
  while(tabKey.length > tabChiffre.length) tabChiffre.push(0); // Adjust text length
  
 
  
  let k = 1;  
  for(let i = 0; tabKey.length < tabChiffre.length; i++) { // Adjust the key size
    if (i > tabKey.length) {
      i = 0;
      k++;
    }
    tabKey.push(tabKey[i] / k);
	tabKey[i] *= 1;
  }
  
  for(i = 0; i < tabKey.length; i++) tabChiffre[i] -= (3 * tabKey[i]) % 4; // Subtract the key * 3
  
  while(tabChiffre.length > size) { // While the size is not corresponding, reduct the text
    let j = 0;
    for(i = 0; i < tabChiffre.length; i++) {
      if(i <= 0) tabChiffre.splice(j, 1);
      j++;
    }
  }
    
  for(i = 0; i < tabChiffre.length; i++) {  // Change the values by the letters
  
    let done;
	for(let j = 0; j < alphabet.length; j++) {
		if(tabChiffre[i] == j + 1) {
			tabChiffre[i] = alphabet[j];
			done = 1;
			break;
		}
	}
	if(!done) tabChiffre[i] = "~"; // If the caracter wasn't found
    
  }
  
  let final = '';
  
  for(i = 0; i < tabChiffre.length; i++)  final += tabChiffre[i];

  return final;

}