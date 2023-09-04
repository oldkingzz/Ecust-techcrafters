$(document).ready(function () {
            $('.nav-link').click(function (event) {
                event.preventDefault();  // 阻止默认的页面跳转行为

                var url = $(this).attr('href');

                // 使用AJAX请求调用Django视图函数
                $.ajax({
                    url: url,
                    type: 'GET',
                    dataType: 'json',
                    success: function (data) {
                        // 在成功回调中更新页面内容
                        $('#content').html('<p>' + data.content + '</p>');
                    },
                    error: function (error) {
                        console.log(error);
                    }
                });
            });
        });

const courseLinks = document.querySelectorAll('.course-link');

courseLinks.forEach(link => {
    link.addEventListener('click', function(event) {
        event.preventDefault();

        // Save the original href value in a data attribute
        if (!this.hasAttribute('data-href')) {
            this.setAttribute('data-href', this.getAttribute('href'));
        }

        // Get the course name from the link text
        const courseName = this.innerText;

        // Remove the href attribute to disable the link temporarily
        this.removeAttribute('href');

        // Redirect to the course's subdirectory (update this URL as needed)
        window.location.href = `/navi/${courseName}/`;

        // Re-enable the link after a short delay (500ms in this example)
        setTimeout(() => {
            this.setAttribute('href', this.getAttribute('data-href'));
        }, 500);
    });
});

const backButton = document.getElementById('back-button');

backButton.addEventListener('click', function() {
    // Go back to the previous URL in history
    history.back();
});

 // Get references to the iframe and replacement content
const iframe = document.getElementById('course-iframe');
const replacementContent = document.getElementById('replacementContent');

// Get the button reference
const toggleButton = document.getElementById('toggleButton');

// Add a click event listener to the button
toggleButton.addEventListener('click', function () {
// Check if the iframe is visible
if (iframe.style.display === 'none') {
  // If the iframe is hidden, show it and hide the replacement content
  iframe.style.display = 'block';
  replacementContent.style.display = 'none';
} else {
  // If the iframe is visible, hide it and show the replacement content
  iframe.style.display = 'none';
  replacementContent.style.display = 'block';
}
});