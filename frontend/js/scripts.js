/* function registrarIngreso() {
  const placa = document.getElementById("placa").value;

  if (!placa) {
    Swal.fire({
      icon: "warning",
      title: "Campo requerido",
      text: "Por favor ingrese el número de placa",
    });
    return;
  }

  Swal.fire({
    title: "Registrando ingreso...",
    text: "Por favor espere",
    allowOutsideClick: false,
    showConfirmButton: false,
    willOpen: () => {
      Swal.showLoading();
    },
  });

  fetch("http://localhost:5000/ingreso", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ placa }),
  })
    .then((res) => res.json())
    .then((data) => {
      Swal.fire({
        icon: "success",
        title: "¡Éxito!",
        text: data.mensaje,
        timer: 2000,
        showConfirmButton: false,
      });
      document.getElementById("placa").value = "";
    })
    .catch((error) => {
      Swal.fire({
        icon: "error",
        title: "Error",
        text: "No se pudo registrar el ingreso",
      });
    });
}

function registrarSalida() {
  const id = document.getElementById("idRegistro").value;

  if (!id) {
    Swal.fire({
      icon: "warning",
      title: "Campo requerido",
      text: "Por favor ingrese el ID del registro",
    });
    return;
  }

  Swal.fire({
    title: "Registrando salida...",
    text: "Por favor espere",
    allowOutsideClick: false,
    showConfirmButton: false,
    willOpen: () => {
      Swal.showLoading();
    },
  });

  fetch(`http://localhost:5000/salida/${id}`, {
    method: "PUT",
  })
    .then((res) => res.json())
    .then((data) => {
      Swal.fire({
        icon: "success",
        title: "¡Éxito!",
        text: data.mensaje,
        timer: 2000,
        showConfirmButton: false,
      });
      document.getElementById("idRegistro").value = "";
    })
    .catch((error) => {
      Swal.fire({
        icon: "error",
        title: "Error",
        text: "No se pudo registrar la salida",
      });
    });
}

function verDiaMasOcupado() {
  fetch("http://localhost:5001/estadisticas/dia-mas-ocupado")
    .then((res) => res.json())
    .then((data) => {
      alert(`Día más ocupado: ${data.dia} con ${data.total} ingresos`);
    });
}

function verPromedio() {
  fetch("http://localhost:5001/estadisticas/promedio-diario")
    .then((res) => res.json())
    .then((data) => {
      const ctx = document.getElementById("grafico").getContext("2d");
      new Chart(ctx, {
        type: "bar",
        data: {
          labels: ["Promedio Diario"],
          datasets: [
            {
              label: "Ingresos",
              data: [data.promedio_diario],
            },
          ],
        },
      });
    });
}
 */

function registrarIngreso() {
  const placa = document.getElementById("placa").value.trim();

  if (!placa) {
    Swal.fire({
      icon: "warning",
      title: "Campo requerido",
      text: "Por favor ingrese el número de placa",
    });
    return;
  }

  Swal.fire({
    title: "Registrando ingreso...",
    allowOutsideClick: false,
    showConfirmButton: false,
    didOpen: () => Swal.showLoading(),
  });

  fetch("http://localhost:5000/ingreso", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ placa }),
  })
    .then((res) => res.json())
    .then((data) => {
      Swal.fire({
        icon: "success",
        title: "¡Éxito!",
        text: data.mensaje,
        timer: 2000,
        showConfirmButton: false,
      });
      document.getElementById("placa").value = "";
    })
    .catch(() => {
      Swal.fire({
        icon: "error",
        title: "Error",
        text: "No se pudo registrar el ingreso",
      });
    });
}

function registrarSalida() {
  const id = document.getElementById("idRegistro").value.trim();

  if (!id) {
    Swal.fire({
      icon: "warning",
      title: "Campo requerido",
      text: "Por favor ingrese el ID del registro",
    });
    return;
  }

  Swal.fire({
    title: "Registrando salida...",
    allowOutsideClick: false,
    showConfirmButton: false,
    didOpen: () => Swal.showLoading(),
  });

  fetch(`http://localhost:5000/salida/${id}`, {
    method: "PUT",
  })
    .then((res) => res.json())
    .then((data) => {
      Swal.fire({
        icon: "success",
        title: "¡Éxito!",
        text: data.mensaje,
        timer: 2000,
        showConfirmButton: false,
      });
      document.getElementById("idRegistro").value = "";
    })
    .catch(() => {
      Swal.fire({
        icon: "error",
        title: "Error",
        text: "No se pudo registrar la salida",
      });
    });
}

function verDiaMasOcupado() {
  fetch("http://localhost:5001/estadisticas/dia-mas-ocupado")
    .then((res) => res.json())
    .then((data) => {
      const mensaje = data.dia
        ? `Día más ocupado: ${data.dia} con ${data.total} ingresos`
        : "No hay datos disponibles";
      Swal.fire({
        icon: "info",
        title: "Estadística",
        text: mensaje,
      });
    })
    .catch(() => {
      Swal.fire({
        icon: "error",
        title: "Error",
        text: "No se pudo obtener la estadística",
      });
    });
}

function verPromedio() {
  fetch("http://localhost:5001/estadisticas/promedio-diario")
    .then((res) => res.json())
    .then((data) => {
      const ctx = document.getElementById("grafico").getContext("2d");

      // Elimina gráfica anterior si existe
      if (window.miGrafico) {
        window.miGrafico.destroy();
      }

      window.miGrafico = new Chart(ctx, {
        type: "bar",
        data: {
          labels: ["Promedio Diario"],
          datasets: [
            {
              label: "Ingresos",
              data: [data.promedio_diario],
              backgroundColor: "#2196f3",
            },
          ],
        },
        options: {
          responsive: true,
          plugins: {
            legend: { display: false },
          },
          scales: {
            y: {
              beginAtZero: true,
              stepSize: 1,
            },
          },
        },
      });
    })
    .catch(() => {
      Swal.fire({
        icon: "error",
        title: "Error",
        text: "No se pudo obtener el promedio",
      });
    });
}
