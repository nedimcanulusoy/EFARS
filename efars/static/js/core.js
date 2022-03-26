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

