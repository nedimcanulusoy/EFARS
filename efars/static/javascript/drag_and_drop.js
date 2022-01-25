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
//    files.forEach(previewFile)
}

//function previewFile(file) {
//    let reader = new FileReader()
//    reader.readAsDataURL(file)
//    reader.onloadend = function () {
//        let img = document.createElement('img')
//        img.src = reader.result
//        document.getElementById('gallery').appendChild(img)
//    }
//}

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
