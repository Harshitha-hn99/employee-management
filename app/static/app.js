const API_URL = "/employees";

// Load employees when page opens
window.onload = function () {
    loadEmployees();
};

// Fetch all employees
async function loadEmployees() {

    const response = await fetch(API_URL);
    const employees = await response.json();

    const tableBody = document.getElementById("employeeTable");

    tableBody.innerHTML = "";

    employees.forEach(emp => {

        tableBody.innerHTML += `
            <tr>
                <td>${emp.id}</td>
                <td>${emp.name}</td>
                <td>${emp.email}</td>
                <td>${emp.department}</td>
                <td>${emp.salary}</td>

                <td>
                    <button onclick="editEmployee(${emp.id})">Edit</button>

                    <button onclick="deleteEmployee(${emp.id})">
                        Delete
                    </button>
                </td>
            </tr>
        `;
    });
}
