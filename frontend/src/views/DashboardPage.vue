<template>
  <div class="dashboard">
    <h1 class="main-title">Página Principal</h1>

    <div class="card-container">
      <div class="card" @click="$emit('set-page', 'PATIENTS')">
        <PatientIcon class="card-icon user" />
        <div class="card-info">
          <h2>Ingresar Paciente</h2>
          <p>Registrar y gestionar la información de los pacientes.</p>
        </div>
      </div>

      <div class="card" @click="$emit('set-page', 'RESULTS')">
        <ResultsIcon class="card-icon upload" />
        <div class="card-info">
          <h2>Ingresar/Consultar Resultados</h2>
          <p>Añadir y consultar los resultados del perfil lipídico.</p>
        </div>
      </div>

      <div class="card" @click="$emit('set-page', 'LAB_TECHS')">
        <LabIcon class="card-icon lab" />
        <div class="card-info">
          <h2>Gestión de Laboratorio</h2>
          <p>Administrar el personal y recursos del laboratorio.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.dashboard {
  animation: fadeIn 0.4s ease-in-out;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.main-title {
  font-size: 1.8rem;
  font-weight: 700;
  color: #0f172a;
  margin-bottom: 24px;
}

.card-container {
  display: flex;
  flex-wrap: wrap;
  gap: 24px;
}

.card {
  flex: 1;
  min-width: 280px;
  background: white;
  border-radius: 12px;
  padding: 24px;
  display: flex;
  align-items: center;
  gap: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
}

.card:hover {
  transform: translateY(-3px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12);
}

.card-icon {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background-color: #dbeafe;
  display: flex;
  align-items: center;
  justify-content: center;
}

.card-info h2 {
  font-size: 1.1rem;
  color: #0f172a;
  margin-bottom: 6px;
}

.card-info p {
  color: #64748b;
  font-size: 0.9rem;
}

.card-icon.user::before {
  content: '👤';
  font-size: 22px;
}

.card-icon.upload::before {
  content: '📈';
  font-size: 22px;
}

.card-icon.lab::before {
  content: '🧪';
  font-size: 22px;
}
</style>
