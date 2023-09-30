const addPatientForm = document.getElementById("add-patient-form");
const patientsTableBody = document.querySelector("#patients-table tbody");

addPatientForm.addEventListener("submit", (event) => {
  event.preventDefault();

  const formData = new FormData(addPatientForm);

  fetch("/patients", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((patient) => {
      const row = document.createElement("tr");

      const idCell = document.createElement("td");
      idCell.textContent = patient.id;

      const nameCell = document.createElement("td");
      nameCell.textContent = patient.name;

      const ageCell = document.createElement("td");
      ageCell.textContent = patient.age;

      const genderCell = document.createElement("td");
      genderCell.textContent = patient.gender;

      row.append(idCell, nameCell, ageCell, genderCell);
      patientsTableBody.append(row);

      addPatientForm.reset();
    })
    .catch((error) => console.error(error));
});

fetch("/patients")
  .then((response) => response.json())
  .then((patients) => {
    patients.forEach((patient) => {
      const row = document.createElement("tr");

      const idCell = document.createElement("td");
      idCell.textContent = patient.id;

      const nameCell = document.createElement("td");
      nameCell.textContent = patient.name;

      const ageCell = document.createElement("td");
      ageCell.textContent = patient.age;

      const genderCell = document.createElement("td");
      genderCell.textContent = patient.gender;

      row.append(idCell, nameCell, ageCell, genderCell);
      patientsTableBody.append(row);
    });
  })
  .catch((error) => console.error(error));
