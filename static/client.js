function onSendButton() {
  var Open =  document.getElementById("Open").value;
  var Low = document.getElementById("Low").value;
  var Volume = document.getElementById("Volume").value;

  document.getElementById("price").textContent=Open;


  let params = { L: Low, O: Open, V:Volume };

  fetch( 'http://127.0.0.1:5000/predict', {
      method: 'POST',  
      body: JSON.stringify({ message: params }),
      mode:"cors",
      headers: {
        'Content-Type': 'application/json'
      },
    })
    .then(r => r.json())
    .then(r => {
      let rep =  r.answer;
      alert(rep)

  }).catch((error) => {
      console.error('Error:', error);
    });
}

