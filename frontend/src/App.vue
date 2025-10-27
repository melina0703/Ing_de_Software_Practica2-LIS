<template>
  <div class="layout">
    <!-- ===== SIDEBAR ===== -->
    <aside class="sidebar">
      <div class="logo">
        VitalSoft <span class="highlight">LIS</span>
      </div>

      <nav class="nav">
        <button
          @click="setPage('DASHBOARD')"
          :class="['nav-item', { active: page === 'DASHBOARD' }]"
        >
          <span>Página Principal</span>
        </button>

        <button
          @click="setPage('PATIENTS')"
          :class="['nav-item', { active: page === 'PATIENTS' }]"
        >
          <span>Ingresar Paciente</span>
        </button>

        <button
          @click="setPage('RESULTS')"
          :class="['nav-item', { active: page === 'RESULTS' }]"
        >
          <span>Resultados</span>
        </button>

        <button
          @click="setPage('LAB_TECHS')"
          :class="['nav-item', { active: page === 'LAB_TECHS' }]"
        >
          <span>Gestión de Laboratorio</span>
        </button>
      </nav>
    </aside>

    <!-- ===== MAIN CONTENT ===== -->
    <main class="main">
      <DashboardPage
        v-if="page === 'DASHBOARD'"
        @set-page="setPage"
      />
      <PatientsPage v-if="page === 'PATIENTS'" />
      <ResultsPage v-if="page === 'RESULTS'" />
      <LabTechsPage v-if="page === 'LAB_TECHS'" />
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import DashboardPage from './views/DashboardPage.vue';
import PatientsPage from './views/PatientsPage.vue';
import ResultsPage from './views/ResultsPage.vue';
import LabTechsPage from './views/LabTechsPage.vue';

const page = ref('DASHBOARD');
const setPage = (p) => (page.value = p);
</script>

<style>

html, body, #app {
  margin: 0;
  padding: 0;
  height: 100%;
}

/* === LAYOUT === */
.layout {
  display: flex;
  height: 100vh;
  padding: 0;
  margin: 0;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* === SIDEBAR === */
.sidebar {
  top: 0;
  left: 0;
  height: 100vh;
  width: 230px;
  background-color: #1e293b;
  color: #e2e8f0;
  display: flex;
  flex-direction: column;
  padding: 20px;
  box-shadow: 3px 0 8px rgba(0, 0, 0, 0.2);
}

.logo {
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 40px;
}

.logo .highlight {
  color: #3b82f6;
}

/* === NAVIGATION === */
.nav {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 14px;
  border-radius: 8px;
  color: #cbd5e1;
  background: none;
  border: none;
  cursor: pointer;
  text-align: left;
  font-weight: 500;
  transition: background 0.25s, color 0.25s;
}

.nav-item:hover {
  background-color: #334155;
  color: #fff;
}

.nav-item.active {
  background-color: #2563eb;
  color: #fff;
  box-shadow: 0 0 8px rgba(37, 99, 235, 0.4);
}

.icon {
  width: 20px;
  height: 20px;
  opacity: 0.9;
}

/* === MAIN AREA === */
.main {
  flex: 1;
  background-color: #f8fafc;
  padding: 32px;
  overflow-y: auto;
}
</style>
