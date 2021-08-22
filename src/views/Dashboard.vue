<template lang="pug">
.v-container.pa-4.mt-12
  // Main content
  v-layout
    v-flex(xs0, sm1, md1, lg1, xl2)
    v-flex(xs12, sm10, md10, lg10, xl8)
      v-layout(wrap).pt-4
        span._headline {{ $store.state.AppStore.group_name }}, 
          span(style="color: #777") {{ $store.state.AppStore.group_type }}
        v-spacer
        v-progress-circular.mt-n4(:value="80" rotate=128 size="84" width=10 color="#8C52FF")
          span#overall_metric() {{ overall_metric }}
      v-layout(wrap, v-if='typeof $store.state.AppStore.group_id !== "undefined"')
        LineChart(:chartdata='chartData', :options='chartOptions', style="width: 100%; height: auto")
        v-layout.mt-12(style="display: flex; flex-wrap: wrap;")
          p.mr-4.selector_text Показать
          v-select(v-model="type_selector" :items="type_items" item-text="text" item-value="value" return-object)
          p.ml-4.mr-4.selector_text за
          v-select(v-model="date_selector" :items="date_items" item-text="text" item-value="value" return-object)
        
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

  type_selector = {text: "анализ облика компании", type: 0}
  type_items = [
    {text: "анализ облика компании", type: 0},
    {text: "анализ позитивных комментариев", type: 1},
    {text: "анализ негативных комментариев", type: 2},
    {text: "сравнение с другим брендом", type: 3},
    {text: "анализ влияния на найм", type: 4}
  ]

  date_selector = {text: "последний квартал", type: 0}
  date_items = [
    {text: "последний квартал", type: 0},
    {text: "месяц...", type: 1},
    {text: "год...", type: 2},
    {text: "промежуток с ... по ...", type: 3},
  ]


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
  font-weight: 800;
  font-size: 20px;
}

#app.theme--dark > div > main > div > div > div > div.flex > div.layout.pt-4.wrap > div.v-progress-circular > div > #overall_metric{ 
  color: white!important;
}
#app.theme--light > div > main > div > div > div > div.flex > div.layout.pt-4.wrap > div.v-progress-circular > div {
  color: black;
}

.v-select {
  max-width: 370px!important;
  min-width: 250px!important;
  padding-top: 0px!important;
  display: flex;
  align-content: center;
  align-items: center;
}

.v-select__selections > .v-select__selection {
  font-family: 'Inter';
  font-weight: 800;
  font-size: 1.3rem;
  margin: 0 0 0 0!important;
}

.v-select__selections > input {
  width: 0px!important;
}

.v-input__slot::before {
  border-color: rgba(red, green, blue, 0);
}

.selector_text {
  font-family: 'Inter';
  font-weight: 800;
  font-size: 1.3rem;
  display: flex;
  align-items: center;
  align-content: center;
}

.__web-inspector-hide-shortcut__ {
  width: 0px;
}
</style>

