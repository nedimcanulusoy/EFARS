function hideUploadView() {
    document.getElementById("upload_view").classList.add("d-none")
}

function hideSpinner() {
    document.getElementById("loading").classList.add("d-none")
}

function hideResultView() {
    document.getElementById("result_view").classList.add("d-none")
}

function hidePageContent() {
    document.getElementById("page-content").classList.add("d-none")
}

function showPageContent() {
    document.getElementById("page-content").classList.remove("d-none")
}


function showSpinner() {
    hideResultView()
    hideUploadView()
    hidePageContent()

    document.getElementById("loading").classList.remove("d-none")
}

function showResultView() {
    hideUploadView()
    hideSpinner();

    showPageContent()
    document.getElementById("result_view").classList.remove("d-none")
}

function showUploadView() {
    hideResultView()
    hideSpinner();

    showPageContent()
    document.getElementById("upload_view").classList.remove("d-none")
}

function downloadPDF() {
    download("/result/" + window.filePath)
    // showUploadView()
}

function showError(message) {
    const alertPlaceholder = document.getElementById('errorAlertPlaceholder')
    const wrapper = document.createElement('div')

    wrapper.innerHTML = `<div class="alert alert-danger alert-dismissible fade-in" role="alert">
                            ${message}
                            <button id="alert-close-btn" type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                        </div>`

    alertPlaceholder.append(wrapper)

    setTimeout(() => {
        fadeOut(wrapper, 500)
    }, 3000)
}

function fadeOut(elem, ms) {
    if (!elem)
        return;

    if (ms) {
        var opacity = 1;
        var timer = setInterval(function () {
            opacity -= 50 / ms;
            if (opacity <= 0) {
                clearInterval(timer);
                opacity = 0;
                elem.style.display = "none";
                elem.style.visibility = "hidden";
            }
            elem.style.opacity = opacity;
            elem.style.filter = "alpha(opacity=" + opacity * 100 + ")";
        }, 50);
    } else {
        elem.style.opacity = 0;
        elem.style.filter = "alpha(opacity=0)";
        elem.style.display = "none";
        elem.style.visibility = "hidden";
    }
}

// https://stackoverflow.com/questions/13733912/javascript-fade-in-fade-out-without-jquery-and-css3
//https://stackoverflow.com/questions/3357553/how-do-i-store-an-array-in-localstorage
