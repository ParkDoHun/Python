const mark = document.getElementById('mark');

const CLICKED_CLASS = "clicked";

function handleEvent() {
    const hasClass = mark.classList.contains(CLICKED_CLASS);

    mark.classList.toggle(CLICKED_CLASS);

    // if (!hasClass) {
    //     mark.classList.add(CLICKED_CLASS);
    // } else {
    //     mark.classList.remove(CLICKED_CLASS);
    // }
}

function init() {
    mark.addEventListener("click", handleEvent);
}
init();