document.addEventListener('DOMContentLoaded', 
function () {
	mb = document.querySelector("#users_followed");
	follow_btn = document.querySelector("#follow-btn");
	follow_btn.addEventListener("click", (e) => {
	foll = follow_btn.getAttribute("data-user");
	cont = follow_btn.textContent;
   fetch('/follow_user', {
      method: 'POST',
      body: JSON.stringify({
      "foll": foll,
      "cont": cont,
})
    })
    .then(res => res.json())
    .then(res => {
     });
   follow_btn.textContent="Unfollow";
     
     });
     });
    
     
   

