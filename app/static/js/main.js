// main.js
$(document).ready(function() {
    // File upload change handler
    $('#file-upload').change(function() {
        const fileName = $(this).val().split('\\').pop();
        $('#file-name').text(fileName || 'No file chosen');
    });

    // Upload button click handler
    $('#uploadBtn').click(function() {
        const formData = new FormData($('#uploadForm')[0]);

        // Show the loader before sending the request
        $('#loadingSpinner').show();
        $('#detectionResult').removeClass('alert-success alert-danger').addClass('alert-light').text('');
        $('#videoContainer').hide();

        // Ensure the UI updates before sending the AJAX request
        setTimeout(() => {
            $.ajax({
                url: '/upload',
                type: 'POST',
                data: formData,
                contentType: false,
                processData: false,
                success: function(data) {
                    var resultText = 'Detection Result: ' + data.result;
                    var resultImage = data.result === 'Real' ? '/static/images/thumpup.png' : '/static/images/thumpdown.png';

                    // Hide loader and show results
                    $('#loadingSpinner').hide();
                    $('#detectionResult').html('<img src="' + resultImage + '" alt="' + data.result + '" style="height: 64px;"> ' + resultText);

                    // Determine file type
                    var fileType = data.videoUrl.split('.').pop().toLowerCase();
                    

                    if (["mp4", "avi", "mov", "webm"].includes(fileType)) {
                        $('#videoPlayback').attr('src', data.videoUrl).show();
                        $('#imagePreview').hide();
                    } else if (["jpg", "jpeg", "png"].includes(fileType)) {
                        $('#imagePreview').attr('src', data.videoUrl).show();
                        $('#videoPlayback').hide();
                    }

                    $('#videoContainer').show();
                },
                error: function(xhr, status, error) {
                    $('#loadingSpinner').hide();
                    $('#detectionResult').removeClass('alert-light').addClass('alert-danger').text('Error: ' + error);
                }
            });
        }, 100);
    });
});
