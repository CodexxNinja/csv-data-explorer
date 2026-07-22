// Drag-and-drop file upload UX
const dropZone = document.getElementById('dropZone');
const fileInput = document.getElementById('file');
const dropZoneText = document.getElementById('dropZoneText');

if (dropZone) {
    dropZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropZone.classList.add('dragover');
    });

    dropZone.addEventListener('dragleave', () => {
        dropZone.classList.remove('dragover');
    });

    dropZone.addEventListener('drop', (e) => {
        e.preventDefault();
        dropZone.classList.remove('dragover');
        if (e.dataTransfer.files.length) {
            fileInput.files = e.dataTransfer.files;
            updateFileName();
        }
    });

    fileInput.addEventListener('change', updateFileName);

    function updateFileName() {
        if (fileInput.files.length) {
            dropZoneText.textContent = ` ${fileInput.files[0].name} selected`;
        }
    }
}