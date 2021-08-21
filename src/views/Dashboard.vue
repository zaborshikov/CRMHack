<template lang="pug">
.v-container.pa-4.mt-12
  // Main content
  v-layout
    v-flex(xs1, md2)
    v-flex(xs10, md8)
      span._headline.pt-4 Дэшборд
      v-layout(v-if='typeof $store.state.AppStore.group_id !== "undefined"')
        span yeah
        LineChart(:chartdata='chartData', :options='chartOptions')
      v-layout(v-else) 
        span Что-то пошло не так. Попробуйте начать сначала.
    v-flex(xs1, md2)
</template>

<script lang="ts">
import Vue from 'vue'
import { create } from '@/utils/api'
import Component from 'vue-class-component'
import { i18n } from '@/plugins/i18n'
import { namespace } from 'vuex-class'
import { Line } from 'vue-chartjs'
import LineChart from '@/components/LineChart.vue'

const AppStore = namespace('AppStore')
const SnackbarStore = namespace('SnackbarStore')

Vue.component('LineChart', LineChart)

@Component
export default class Home extends Vue {
  @SnackbarStore.Mutation setSnackbarError!: (error: string) => void

  gradient: any = "red"
  gradient2: any = "blue"



  chartData = {
    labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
    datasets: [
      {
        label: 'Data One',
        borderColor: '#FC2525',
        pointBackgroundColor: 'white',
        borderWidth: 1,
        pointBorderColor: 'white',
        backgroundColor: this.gradient,
        data: [40, 39, 10, 40, 39, 80, 40],
      },
      {
        label: 'Data Two',
        borderColor: '#05CBE1',
        pointBackgroundColor: 'white',
        pointBorderColor: 'white',
        borderWidth: 1,
        backgroundColor: this.gradient2,
        data: [60, 55, 32, 10, 2, 12, 53],
      },
    ],
  }
  chartOptions = {
    responsive: true,
    maintainAspectRatio: false,
  }

  async delay(ms: number) {
    return new Promise((resolve) => setTimeout(resolve, ms))
  }
}
</script>

<style>
._headline {
  font-size: 3em !important;
  font-family: 'Inter';
  font-weight: 800;
  line-height: 85%;
}
</style>
