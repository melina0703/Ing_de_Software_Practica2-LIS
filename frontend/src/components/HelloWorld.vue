<template>
  <div class="animate-fade-in">
    <h1 class="text-3xl font-bold text-slate-800 mb-6">Página Principal</h1>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <button
        v-for="(card, index) in cards"
        :key="index"
        @click="setPage(card.page)"
        class="bg-white p-6 rounded-lg shadow-md hover:shadow-xl transition-shadow duration-300 text-left flex items-center group"
      >
        <div class="bg-blue-100 p-4 rounded-full mr-6">
          <component :is="card.icon" class="w-8 h-8 text-blue-500" />
        </div>
        <div class="flex-grow">
          <h2 class="text-xl font-semibold text-slate-700">{{ card.title }}</h2>
          <p class="text-slate-500 mt-1">{{ card.description }}</p>
        </div>
        <ChevronRightIcon class="w-6 h-6 text-slate-400 group-hover:text-blue-600 transition-colors" />
      </button>
    </div>
  </div>
</template>

<script>
import { LabIcon, PatientIcon, ResultsIcon } from '../components/Icons.js'

export default {
  name: 'DashboardPage',
  props: ['setPage'],
  data() {
    return {
      cards: [
        {
          page: 'PATIENTS',
          title: 'Ingresar Paciente',
          description: 'Registrar y gestionar la información de los pacientes.',
          icon: PatientIcon
        },
        {
          page: 'RESULTS',
          title: 'Ingresar/Consultar Resultados',
          description: 'Añadir y consultar los resultados del perfil lipídico.',
          icon: ResultsIcon
        },
        {
          page: 'LAB_TECHS',
          title: 'Gestión de Laboratorio',
          description: 'Administrar el personal y recursos del laboratorio.',
          icon: LabIcon
        }
      ]
    }
  }
}
</script>
