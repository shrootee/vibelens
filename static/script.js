const captionOutput = document.querySelector(".output");
const generateButton = document.querySelector("#generateButton");

const messages = [
    "Cooking something viral for you… 🔥",
    "Training my creativity muscles… 🧠",
    "Making it scroll-stopping 👀",
    "Almost ready… polishing the vibe ✨"
];

imageInput.addEventListener("change", function () {
    const file = this.files[0];

    if (file) {
        previewImage.src = URL.createObjectURL(file);
        previewImage.style.display = "block";
        uploadContent.style.display = "none";  // hide +
    }
});


generateButton.addEventListener("click", async () => {

    const imageInput = document.querySelector("#imageInput");
    const file = imageInput.files[0];

    if (!file) {
        alert("Please select an image first!");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    let index = 0;

    // Start loading animation
    captionOutput.innerText = messages[0];

    const interval = setInterval(() => {
        index = (index + 1) % messages.length;
        captionOutput.innerText = messages[index];
    }, 1000);

    try {
        const response = await fetch("/caption", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        clearInterval(interval); // stop rotating
        captionOutput.innerText = data.description;

    } catch (error) {
        clearInterval(interval); // stop rotating
        console.error("Error:", error);
        captionOutput.innerText = "Something went wrong.";
    }
});