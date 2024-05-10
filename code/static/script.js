document.addEventListener("DOMContentLoaded", function() {
  const menuItems = document.querySelectorAll('.menu-item');
  
  menuItems.forEach(item => {
    const icon = item.querySelector('.menu-icon');
    const subMenu = item.querySelector('.sub-menu');
      let isImageSwapped = false;
      let isSubMenuVisible = false;
  

      function swapImage() {
        if (isImageSwapped) {
          icon.src = "{{ url_for('static', filename='/pics/arrow.png') }}";
        } else {
          icon.src = "{{ url_for('static', filename='/pics/arrowdown.png') }}";
        }
        isImageSwapped = !isImageSwapped;
      }
  
      function toggleSubMenu() {
        if (isSubMenuVisible) {
          subMenu.style.display = 'none';
        } else {
          subMenu.style.display = 'block';
        }
        isSubMenuVisible = !isSubMenuVisible;
      }
  
      item.addEventListener('click', function(event) {
        event.stopPropagation();
        swapImage();
        toggleSubMenu();
      });
      
      
      icon.addEventListener('click', function(event) {
        event.stopPropagation();
        swapImage();
        toggleSubMenu();
      });
      
    });

    // this is broken and not work
    const pictures = document.querySelectorAll(".picture");
    pictures.forEach((picture) => {
    picture.addEventListener("click", function() {
        console.log("s");
        console.log(this)
        // Replace image in the clicked card with the selected picture from the canvas
        const canvasImage = this.querySelector("img");
        console.log(canvasImage)
        const cardImage = document.querySelector(".card[data-bs-target='#offcanvasBottom'] .card-img-top");
        console.log(cardImage)
        cardImage.src = canvasImage.src;
    });
});



// console.log(cardImage)

// Close the offcanvas after selecting the picture
// const offcanvas = document.getElementById("offcanvasBottom");
// const offcanvasInstance = bootstrap.Offcanvas.getInstance(offcanvas);
// offcanvasInstance.hide();
//     });
// });


      
    const saveButton = document.getElementById("saveButton");
    const discardButton = document.getElementById("discardButton");
    saveButton.addEventListener("click", function() {
      console.log("1")
      // save button doesnt do anything besides close canvas
      // Close the offcanvas after selecting the picture
      const offcanvas = document.getElementById("offcanvasBottom");
      const offcanvasInstance = bootstrap.Offcanvas.getInstance(offcanvas);
      offcanvasInstance.hide();
    })
    discardButton.addEventListener("click", function() {
      console.log("1")
      const offcanvas = document.getElementById("offcanvasBottom");
      const offcanvasInstance = bootstrap.Offcanvas.getInstance(offcanvas);
      offcanvasInstance.hide();
    })




    // // Add click event listener to the save button
    // saveButton.addEventListener("click", function() {
    //     // Get the selected image URL
    //     const selectedImage = document.querySelector(".offcanvas-image.selected");
    //     const imageUrl = selectedImage ? selectedImage.getAttribute("src") : null;

    //     // Update the image source in the card
    //     if (imageUrl) {
    //         var cardImage = document.getElementById("selectedImage");
    //         cardImage.setAttribute("src", imageUrl);
    //     }

    //     // Hide the offcanvas after saving the picture
    //     const offcanvasBottom = document.getElementById("offcanvasBottom");
    //     const offcanvas = new bootstrap.Offcanvas(offcanvasBottom);
    //     offcanvas.hide();
    // });

    // // Add click event listener to the discard button
    // discardButton.addEventListener("click", function() {
    //     // Remove the selected class from all images
    //     const offcanvasImages = document.querySelectorAll(".offcanvas-image");
    //     offcanvasImages.forEach(function(image) {
    //         image.classList.remove("selected");
    //     });
    // });



    // // Add click event listener to each offcanvas image
    // const offcanvasImages = document.querySelectorAll(".offcanvas-body");
    // offcanvasImages.forEach(function(image) {
    //     image.addEventListener("click", function() {
    //         // Remove the selected class from all images
    //         offcanvasImages.forEach(function(img) {
    //             img.classList.remove("selected");
    //         });

    //         // Add the selected class to the clicked image
    //         image.classList.add("selected");
    //     });
    // });
  });

