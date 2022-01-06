document.addEventListener("DOMContentLoaded", () => {
  // toggling restaurants

  const toggleLi = (e) => {
    const li = e.target;
    if (li.className === "visited") {
      li.className = "";
    } else {
      li.className = "visited";
    }
  };

  document.querySelectorAll("#restaurants li").forEach((li) => {
    li.addEventListener("click", toggleLi);
  });

  // adding SF places as list items

  // --- your code here!
  document.addEventListener('submit', e => {

    e.preventDefault();
    targetInput = e.target.children[0];
    if(targetInput.value.length > 0){
      targetElementName = `${targetInput.parentElement.parentElement.className == 'list-container' ? 'sf-places' : 'dog-photos'}`;
      const li = document.createElement('li');
      if(targetElementName == 'sf-places'){
        li.textContent = targetInput.value;
      } else {
        const img = document.createElement('img');
        img.src = targetInput.value;
        li.appendChild(img);
      }
      targetElement = targetElementName == 'sf-places' ? document.getElementById(targetElementName) : document.getElementsByClassName(targetElementName)[0];
      targetElement.appendChild(li);
      targetInput.value = "";
    }
  });


  // adding new photos
  // Test: https://1000logos.net/wp-content/uploads/2017/08/Timberwolves_logo_PNG1.png
  // --- your code here!
  document.addEventListener('click', e => {
    const div = document.getElementsByClassName('photo-form-container')[0];
    if(e.target.className == 'photo-show-button'){
      if(div.className == 'photo-form-container'){
        div.className = 'photo-form-container hidden';
      } else {
        div.className = 'photo-form-container';
      }
    }
  });

});
