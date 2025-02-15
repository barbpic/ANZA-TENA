$(document).ready(function() {
    // Load existing users
    loadUsers();

    // User registration form submission
    $('#registrationForm').on('submit', function(e) {
        e.preventDefault();
        const name = $('#userName').val();
        const role = $('#userRole').val();

        $.ajax({
            url: '/api/register',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ name: name, role: role }),
            success: function(response) {
                alert(response.message);
                loadUsers(); // Reload user list
                $('#registrationForm')[0].reset(); // Reset form fields
            },
            error: function(err) {
                alert("Error registering user");
            }
        });
    });

    // Emergency response form submission
    $('#emergencyForm').on('submit', function(e) {
        e.preventDefault();
        const title = $('#emergencyTitle').val();
        const description = $('#emergencyDescription').val();
        const location = $('#emergencyLocation').val();
        const contactInfo = $('#contactInfo').val();

        $.ajax({
            url: '/api/emergency',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ title: title, description: description, location: location, contact_info: contactInfo }),
            success: function(response) {
                alert(response.message);
                $('#emergencyForm')[0].reset(); // Reset form fields
            },
            error: function(err) {
                alert("Error reporting emergency");
            }
        });
    });

    // Other functions for loading and submitting resources, volunteers, healthcare services, and legal aid 
});

// Load users from the backend
function loadUsers() {
    $.get('/api/users', function(data) {
        $('#userList').empty(); // Clear existing list
        data.forEach(function(user) {
            $('#userList').append('<li class="list-group-item">' + user.name + ' - ' + user.role + '</li>');
        });
    });
}
