document.addEventListener(
  "DOMContentLoaded",
  function () {
  item = document.querySelectorAll(".post_edit");
  item.forEach((element) => {
  element.addEventListener("click", () => {
  id = element.getAttribute("data-id");
   edit_post(id);
  });
});
}); 
function edit_post(id){
  fetch(`/all_posts_edit/${id}`)
  .then(response => response.json())
  .then(post => {
	console.log(post);
   edit_btn = document.querySelector(`#edit-btn-${post.id}`);
   edit_btn.textContent = "Save";
   document.querySelector(`#post-${post.id}`).style.display = "none";
   document.querySelector(`#post-edit-${post.id}`).style.display = "block";
   edit_btn.addEventListener('click', () => { 
     edited(id, document.querySelector(`#post-edit-${post.id}`).value)     
});  
   });
}
function edited(id, post){
  fetch('/edit_post', {
      method: 'POST',
      body: JSON.stringify({
      	"id": id,
        "post": post,
      }),
    })
    .then(response => response.json())
    .then(result => {
    	console.log(result);
        document.querySelector(`#post-${id}`).innerHTML = post;
    document.querySelector(`#post-${id}`).style.display = "block";
    document.querySelector(`#post-edit-${id}`).style.display = "none";
    document.querySelector(`#edit-btn-${id}`).textContent = "Edit"; 
  });
}
 function view_post(id){
  fetch(`/all_posts_edit/${id}`)
.then(response => response.json())
.then(post => {
	console.log(post);
   document.querySelector(`#post-${post.id}`).style.display = "block";
    document.querySelector(`#post-edit-${post.id}`).style.display = "none";
     edi_btn = document.querySelector(`#edit-btn-${post.id}`);
   edi_btn.textContent = "Edit";
      edit_post(post.id);
   });
}


