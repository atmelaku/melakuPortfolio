console.log("Hello");


const btn = document.getElementById('toggleBtn');
const form = document.getElementById('uploadimgForm');

btn.addEventListener('click', () => {
  // Check the current display state
  const currentDisplay = window.getComputedStyle(form).display;

  if (currentDisplay === 'none') {
    form.style.display = 'block'; // Show it
    btn.innerHTML = '<i class="fa-solid fa-x"></i> Cancle';         // Change text to X
  } else {
    form.style.display = 'none';  // Hide it
    btn.innerHTML = '<i class="fa-solid fa-upload"></i> Upload Image';
  }
});
