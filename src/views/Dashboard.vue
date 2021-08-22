<template lang="pug">
.v-container.pa-4.mt-12
  // Main content
  v-layout
    v-flex(xs0, sm1, md1, lg1, xl2)
    v-flex(xs12, sm10, md10, lg10, xl8)
      v-layout(wrap).pt-4
        span._headline {{ $store.state.AppStore.group_name }}
        v-spacer
        v-progress-circular(:value="80" rotate=128 size="84" width=10 color="#8C52FF")
          span#overall_metric() {{ overall_metric }}
      v-layout(v-if='typeof $store.state.AppStore.group_id !== "undefined"')
        LineChart(:chartdata='chartData', :options='chartOptions', style="width: 100%; height: auto")
      v-layout(v-else) 
        span Что-то пошло не так. Попробуйте начать сначала.
    v-flex(xs0, sm1, md1, lg1, xl2)
</template>

<script lang="ts">
import Vue from 'vue'
import { create } from '@/utils/api'
import Component from 'vue-class-component'
import { i18n } from '@/plugins/i18n'
import { namespace } from 'vuex-class'
import LineChart from '@/components/LineChart.vue'

const AppStore = namespace('AppStore')
const SnackbarStore = namespace('SnackbarStore')

Vue.component('LineChart', LineChart)

@Component
export default class Home extends Vue {
  @SnackbarStore.Mutation setSnackbarError!: (error: string) => void

  gradient:any = null;
  gradient2:any = null;
  overall_metric:Number = 4.98; 


  chartData = {
    labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
    datasets: [
      {
        label: 'Data One',
        borderColor: '#8C52FF',
        pointBackgroundColor: 'white',
        borderWidth: 1,
        pointBorderColor: 'white',
        backgroundColor: null,
        data: [40, 39, 10, 40, 39, 80, 40],
      },
      {
        label: 'Data Two',
        borderColor: '#A0FFF1',
        pointBackgroundColor: 'white',
        pointBorderColor: 'white',
        borderWidth: 1,
        backgroundColor: null,
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

#overall_metric {
  font-family: 'Inter';
  font-weight: 700;
  font-size: 20px;
}

#app.theme--dark > div > main > div > div > div > div.flex.xs12.sm10.md10.lg8 > div.layout.pt-4.wrap > div.v-progress-circular > div {
  color: white;
}
</style>

