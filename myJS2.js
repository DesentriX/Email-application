function uploadFile() {
  const fileInput = document.getElementById('file-input');
  const file = fileInput.files[0];
  
  if (file) {
    const bucketName = 'emailbucket-21';
    const key = encodeURIComponent(file.name);

    
    // Create a new FormData object
    const formData = new FormData();
    formData.append('file', file);

    // Create a new XMLHttpRequest object
    const xhr = new XMLHttpRequest();

    // Set up the request
    xhr.open('PUT', `https://${bucketName}.s3.amazonaws.com/${key}`, true);
    xhr.send(file); // Send the file

    // Handles responses
    xhr.onload = function() {
      if (xhr.status === 200) {
        console.log('File uploaded successfully.');
      } else {
        console.error('File upload failed:', xhr.statusText);
      }
    };

    // Track progress
    xhr.upload.onprogress = function(event) {
      const progress = Math.round((event.loaded / event.total) * 100);
      console.log(`File upload progress: ${progress}%`);
    };
  }
}
