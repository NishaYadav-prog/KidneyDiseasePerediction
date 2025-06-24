document.getElementById("prediction-form").onsubmit = async function (e) {
  e.preventDefault(); // Prevent form from submitting the traditional way

  let data = {
    age: document.getElementById("age").value,
    bp: document.getElementById("bp").value,
    sg: document.getElementById("sg").value,
    al: document.getElementById("al").value,
    glucose: document.getElementById("glucose").value,
  };

  const response = await fetch("http://localhost:5000/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  const result = await response.json();
  document.getElementById("result").innerText =
    "Prediction: " + result.prediction;
};
