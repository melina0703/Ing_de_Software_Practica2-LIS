<template>
  <div class="paciente-page">
    <h1 class="title">Ingreso de Paciente</h1>

    <!-- NUEVO PACIENTE -->
    <div class="card">
      <h2>Nuevo Paciente</h2>
      <form @submit.prevent="guardarPaciente" class="form-grid">
        <strong>Documento </strong>
        <strong>Nombres</strong>
        <input v-model="nuevo.documento" type="number" placeholder="Documento (ingresar solo un valor numérico)" />
        <input v-model="nuevo.nombre" type="text" placeholder="Nombre" />
        <strong>Apellidos</strong>
        <strong>Dirección de residencia</strong>
        <input v-model="nuevo.apellidos" type="text" placeholder="Apellidos" />
        <input v-model="nuevo.direccion" type="text" placeholder="Dirección" />
        <strong>Número de Teléfono</strong>
        <text></text>
        <input v-model="nuevo.telefono" type="number" placeholder="Teléfono (ingresar solo un valor numérico)" />

        <div class="button-group">
          <button type="button" class="btn limpiar" @click="limpiarCampos">Limpiar</button>
          <button type="submit" class="btn guardar">Guardar</button>
        </div>
      </form>
    </div>

    <!-- PACIENTES REGISTRADOS -->
    <div class="card">
      <h2>Pacientes Registrados</h2>
      <div class="search-container">
        <input v-model="busqueda" type="text" placeholder="🔍 Buscar..." />
      </div>

      <table>
        <thead>
          <tr>
            <th>Documento</th>
            <th>Nombre Completo</th>
            <th>Código de Ingreso</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(paciente, index) in pacientesFiltrados" :key="index">
            <td>{{ paciente.documento }}</td>
            <td>{{ paciente.nombre }} {{ paciente.apellidos }}</td>
            <td>{{ paciente.codigo }}</td>
            <td>
              <button class="accion editar" @click="editarPaciente(index)">✏️</button>
              <button class="accion borrar" @click="eliminarPaciente(index)">🗑️</button>
            </td>
          </tr>
          <tr v-if="pacientesFiltrados.length === 0">
            <td colspan="4" class="no-data">No hay pacientes registrados</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: "PacienteIngreso",
  data() {
    return {
      nuevo: {
        documento: "",
        nombre: "",
        apellidos: "",
        direccion: "",
        telefono: "",
      },
      pacientes: [],
      busqueda: "",
    };
  },
  computed: {
    pacientesFiltrados() {
      const filtro = this.busqueda.toLowerCase();
      return this.pacientes.filter(
        (p) =>
          p.nombre.toLowerCase().includes(filtro) ||
          p.apellidos.toLowerCase().includes(filtro) ||
          p.documento.toLowerCase().includes(filtro)
      );
    },
  },
  methods: {
    guardarPaciente() {
      if (!this.nuevo.documento || !this.nuevo.nombre) {
        alert("Por favor completa al menos Documento y Nombre");
        return;
      }

      const nuevoCodigo = "ING-" + String(this.pacientes.length + 1).padStart(3, "0");

      this.pacientes.push({
        ...this.nuevo,
        codigo: nuevoCodigo,
      });
      this.limpiarCampos();
    },
    limpiarCampos() {
      this.nuevo = { documento: "", nombre: "", apellidos: "", direccion: "", telefono: "" };
    },
    eliminarPaciente(index) {
      if (confirm("¿Deseas eliminar este paciente?")) {
        this.pacientes.splice(index, 1);
      }
    },
    editarPaciente(index) {
      const p = this.pacientes[index];
      this.nuevo = { ...p };
      this.pacientes.splice(index, 1);
    },
  },
};
</script>

<style scoped>
.paciente-page {
  font-family: "Segoe UI", sans-serif;
  background-color: #f7f9fc;
  padding: 2rem;
}

.title {
  font-size: 1.8rem;
  font-weight: bold;
  margin-bottom: 1.5rem;
  color: #222;
}

.card {
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 3px 8px rgba(0, 0, 0, 0.08);
  padding: 1.5rem;
  margin-bottom: 2rem;
}

h2 {
  font-size: 1.2rem;
  margin-bottom: 1rem;
  color: #333;
}

.form-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.form-grid input {
  background-color: #dbeafe;
  color: #fff;
  border: none;
  padding: 0.6rem;
  border-radius: 5px;
}

.button-group {
  grid-column: span 2;
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
  margin-top: 0.5rem;
}

.btn {
  border: none;
  padding: 0.6rem 1.2rem;
  border-radius: 5px;
  cursor: pointer;
  color: #fff;
  font-weight: 600;
}

.btn.limpiar {
  background-color: #6c757d;
}

.btn.guardar {
  background-color: #4b59f2;
}

.btn:hover {
  opacity: 0.9;
}

.search-container {
  text-align: right;
  margin-bottom: 1rem;
}

.search-container input {
  padding: 0.5rem;
  background-color: #dbeafe;
  color: #fff;
  border: none;
  border-radius: 5px;
}

table {
  width: 100%;
  border-collapse: collapse;
}

thead {
  background-color: #f2f4f8;
  color: #333;
}

th, td {
  padding: 0.75rem;
  text-align: left;
  border-bottom: 1px solid #e6e6e6;
}

.accion {
  border: none;
  background: none;
  cursor: pointer;
  font-size: 1.1rem;
}

.accion.editar {
  color: #4b59f2;
}

.accion.borrar {
  color: #e63946;
}

.no-data {
  text-align: center;
  color: #999;
  font-style: italic;
}

input[type="number"]::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

</style>
