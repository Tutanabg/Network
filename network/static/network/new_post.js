document.addEventListener(
  "DOMContentLoaded",
  function () {
    const myform = document.querySelector("#new_form");
    myform.addEventListener("submit", (event) => {
      event.preventDefault();
    const post = document.querySelector('#fill_post').value;
  fetch('/new_post', {
      method: 'POST',
      body: JSON.stringify({
        "post": post,
      }),
    })
    .then(response => response.json())
    .then(result => {
        console.log(result);
        alert("post added");
         });      
         });
});





