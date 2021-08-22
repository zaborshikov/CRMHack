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
        v-layout(wrap)
          v-spacer
          v-btn-toggle(v-model="toggle_multiple", dense, color="#8C52FF")
            v-btn 1Д
            v-btn 7Д
            v-btn 1М
            v-btn 3М
            v-btn 1Г
        v-layout.mt-12(style="display: flex; flex-wrap: wrap; width: 100%")
          p.mr-4.selector_text Показать
          v-select(v-model="type_selector" :items="type_items" item-text="text" item-value="value" return-object color="#8C52FF" item-color="#8C52FF")
          p.ml-4.mr-4.selector_text за
          v-select(v-model="date_selector" :items="date_items" item-text="text" item-value="value" return-object color="#8C52FF" item-color="#8C52FF")
        v-layout(wrap)
          v-layout(v-if="type_selector.type == 0" wrap)
            span 0
            LineChart(:chartdata='chartData2', :options='chartOptions', style="width: 100%; height: auto")
          v-layout(v-if="type_selector.type == 1")
            v-img(v-if="img_loaded1" :src="img_src1")
          v-layout(v-if="type_selector.type == 2")
            v-img(v-if="img_loaded2" :src="img_src2")
            span 2
          v-layout(v-if="type_selector.type == 3")
            span 3
      v-layout(v-else) 
        span Что-то пошло не так. Попробуйте начать сначала.
    v-flex(xs0, sm1, md1, lg1, xl2)
</template>

<script lang="ts">
import Vue from 'vue'
import { stats, getImgFor } from '@/utils/api'
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
  overall_metric:Number = 4.38; 
  toggle_multiple= 1;

  img_loaded1 = false;
  img_loaded2 = false;
  img_src1 = "";
  img_src2 = "";

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
        label: 'Общая метрика привлекательности',
        borderColor: '#8C52FF',
        pointBackgroundColor: 'white',
        borderWidth: 1,
        pointBorderColor: 'white',
        backgroundColor: null,
        data: [40, 39, 10, 40, 39, 80, 40],
      }
    ],
  }

  chartData2 = {
    labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
    datasets: [
      {
        label: 'Позитивные комментарии',
        borderColor: '#FF52AA',
        pointBackgroundColor: 'white',
        borderWidth: 1,
        pointBorderColor: 'white',
        backgroundColor: null,
        data: [10, 20, 35, 30, 47, 44, 55],
      },
      {
        label: 'Негативные комментарии',
        borderColor: '#8C52FF',
        pointBackgroundColor: 'white',
        borderWidth: 1,
        pointBorderColor: 'white',
        backgroundColor: null,
        data: [40, 39, 10, 40, 39, 80, 40],
      },
      {
        label: 'Нейтральные комментарии',
        borderColor: '#333',
        pointBackgroundColor: 'white',
        borderWidth: 1,
        pointBorderColor: 'white',
        backgroundColor: null,
        data: [10, 20, 10, 25, 19, 30, 20],
      }
    ],
  }

  chartOptions = {
    responsive: true,
    maintainAspectRatio: false,
  }

  mounted() {
    stats(this.$store.state.AppStore.group_id).then(data => {
      console.log(data);
    })
    getImgFor(this.$store.state.AppStore.group_id, true).then(data => {
      console.log(data);
      this.img_src2 = data;
      this.img_loaded1 = true;
    });
    getImgFor(this.$store.state.AppStore.group_id, false).then(data => {
      console.log(data);
      this.img_src2 = data;
      this.img_loaded2 = true;
    });
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
  color: "#8C52FF"!important;
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

