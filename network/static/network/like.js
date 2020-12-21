document.addEventListener(
  "DOMContentLoaded",
  function () {
  item = document.querySelectorAll(".post_like");
  item.forEach((post) => {
  	post.addEventListener("click", () => {
  	  id = post.getAttribute("data-id");
   like_post(id);
});
});
});
function like_post(id){
  fetch(`/all_posts_edit/${id}`)
.then(response => response.json())
.then(post => {
	console.log(post);
	document.querySelector(`#like-${id}`).innerHTML = post.likes;
	like_btn = document.querySelector(`#like-btn-${id}`);
    like_btn.textContent = "Like";
    like_btn.style.color ="green";
    document.querySelector(`#like-${id}`).value = post.likes + 1;
   like_btn.addEventListener('click', () => { 
     edited(id, document.querySelector(`#like-${post.id}`).value)
       }); 
   });
}
function edited(id, likes){
  fetch('/like_post', {
      method: 'POST',
      body: JSON.stringify({
      	"id": id,
        "likes": likes,
      }),
    })
    .then(response => response.json())
    .then(result => {
    	console.log(result);
    document.querySelector(`#like-${id}`).innerHTML = likes;
    lik_btn = document.querySelector(`#like-btn-${id}`);
    lik_btn.textContent = "UnLike";
    lik_btn.style.color ="red";
   document.querySelector(`#like-${id}`).value = likes - 1;
   lik_btn.addEventListener('click', () => { 
     like_post(id)
       });
  });
}
function edited_further(id, likes){
  fetch('/like_post', {
      method: 'POST',
      body: JSON.stringify({
      	"id": id,
        "likes": likes,
      }),
    })
    .then(response => response.json())
    .then(result => {
    	console.log(result);
    document.querySelector(`#like-${id}`).innerHTML = likes;
    li_btn = document.querySelector(`#like-btn-${id}`);
    li_btn.textContent = "Like";
    li_btn.style.color ="green";
   document.querySelector(`#like-${id}`).value = likes + 1;
   lik_btn.addEventListener('click', () => { 
     edited(id, document.querySelector(`#like-${id}`).value)
       });
  });
}




		


