// ************************ Drag and drop ***************** //
let dropArea = document.getElementById("drop-area")

// Prevent default drag behaviors
;['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, preventDefaults, false)
    document.body.addEventListener(eventName, preventDefaults, false)
})

// Highlight drop area when item is dragged over it
;['dragenter', 'dragover'].forEach(eventName => {
    dropArea.addEventListener(eventName, highlight, false)
})

;['dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, unhighlight, false)
})

// Handle dropped files
dropArea.addEventListener('drop', handleDrop, false)

function preventDefaults(e) {
    e.preventDefault()
    e.stopPropagation()
}

function highlight(e) {
    dropArea.classList.add('highlight')
}

function unhighlight(e) {
    dropArea.classList.remove('active')
}

function handleDrop(e) {
    var dt = e.dataTransfer
    var files = dt.files

    handleFiles(files)
}

function handleFiles(files) {
    files = [...files]
    files.forEach(uploadFile)
}

function fileValidation() {
    var fileInput =
        document.getElementById('fileElem');

    var filePath = fileInput.value;

    // Allowing file type
    var allowedExtensions = /(\.csv)$/i;

    if (allowedExtensions.exec(filePath)) {
        return true;
    }

    showError(`"Invalid file type! | Allowed file type: ".csv"`)
    fileInput.value = '';
    return false;

}

// REF=> https://www.geeksforgeeks.org/file-type-validation-while-uploading-it-using-javascript/

function uploadFile(file, i) {
    var url = '/'
    var formData = new FormData()

    formData.append('file', file)

    fetch(url, {
        method: 'POST',
        body: formData
    })
        .then(response => response.json())
        .then((r) => {console.log(r)
        })
        .catch((r) => { console.log(r)
        })
}
